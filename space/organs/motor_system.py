"""Motor system: safe output boundary for displays, audio, devices and other actuators."""
from dataclasses import dataclass
from time import time
from typing import Any, Callable

@dataclass(frozen=True)
class Actuation:
    action_id: str
    actuator: str
    payload: Any
    timestamp: float
    committed: bool

class MotorSystem:
    def __init__(self) -> None:
        self._handlers: dict[str, Callable[[Any], Any]] = {}
        self._counter = 0
        self._history: list[Actuation] = []

    def register(self, actuator: str, handler: Callable[[Any], Any]) -> None:
        if actuator in self._handlers:
            raise ValueError("duplicate actuator")
        self._handlers[actuator] = handler

    def execute(self, actuator: str, payload: Any, authorized: bool = False) -> Actuation:
        self._counter += 1
        if not authorized:
            event = Actuation(f"act-{self._counter}", actuator, payload, time(), False)
            self._history.append(event)
            return event
        self._handlers[actuator](payload)
        event = Actuation(f"act-{self._counter}", actuator, payload, time(), True)
        self._history.append(event)
        return event

    def actuators(self) -> list[str]:
        return list(self._handlers)

    def history(self) -> list[Actuation]:
        return list(self._history)
