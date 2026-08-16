"""Circulatory system: distributes resources and exposes organism health."""
from dataclasses import dataclass, field
from time import time
from typing import Any

@dataclass
class ResourcePool:
    name: str
    capacity: float
    available: float

@dataclass(frozen=True)
class Pulse:
    timestamp: float
    cycle: int
    health: str
    pending_signals: int
    resources: dict[str, float]

class CirculatorySystem:
    def __init__(self) -> None:
        self.resources: dict[str, ResourcePool] = {}
        self.health = "UNKNOWN"
        self._pulses: list[Pulse] = []

    def register(self, name: str, capacity: float, available: float | None = None) -> None:
        self.resources[name] = ResourcePool(name, capacity, capacity if available is None else available)

    def consume(self, name: str, amount: float) -> bool:
        pool = self.resources[name]
        if amount < 0 or pool.available < amount:
            return False
        pool.available -= amount
        return True

    def replenish(self, name: str, amount: float) -> None:
        pool = self.resources[name]
        pool.available = min(pool.capacity, pool.available + max(0, amount))

    def pulse(self, cycle: int, pending_signals: int = 0, health: str | None = None) -> Pulse:
        if health is not None:
            self.health = health
        values = {name: pool.available for name, pool in self.resources.items()}
        pulse = Pulse(time(), cycle, self.health, pending_signals, values)
        self._pulses.append(pulse)
        return pulse

    def latest_pulse(self) -> Pulse | None:
        return self._pulses[-1] if self._pulses else None
