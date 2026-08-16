"""Low-resource local semantic bus for communication inside one SPACE.

The bus carries references and semantic deltas instead of copying full state.
It is event-driven: subscribers are activated only for matching topics.
"""
from dataclasses import dataclass, field
from time import time
from typing import Callable

@dataclass(frozen=True)
class SemanticEvent:
    event_id: str
    topic: str
    source: str
    meaning: str
    place: str
    reference: str | None = None
    delta: dict = field(default_factory=dict)
    priority: int = 0
    created_at: float = field(default_factory=time)

class InternalSemanticBus:
    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[SemanticEvent], None]]] = {}
        self._queue: list[SemanticEvent] = []

    def subscribe(self, topic: str, handler: Callable[[SemanticEvent], None]) -> None:
        self._subscribers.setdefault(topic, []).append(handler)

    def publish(self, event: SemanticEvent) -> None:
        self._queue.append(event)
        self._queue.sort(key=lambda e: -e.priority)

    def dispatch_one(self) -> bool:
        if not self._queue:
            return False
        event = self._queue.pop(0)
        for handler in self._subscribers.get(event.topic, []):
            handler(event)
        return True

    def pending(self) -> int:
        return len(self._queue)
