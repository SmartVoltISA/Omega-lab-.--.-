from dataclasses import dataclass, asdict
from typing import Any

@dataclass(frozen=True)
class Event:
    event_id: str
    kind: str
    payload: Any
    cycle: int

class EventBus:
    def __init__(self) -> None:
        self._events: list[Event] = []
        self._counter = 0

    def publish(self, kind: str, payload: Any, cycle: int) -> Event:
        self._counter += 1
        event = Event(f"event-{self._counter}", kind, payload, cycle)
        self._events.append(event)
        return event

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        return [asdict(e) for e in self._events[-limit:]]
