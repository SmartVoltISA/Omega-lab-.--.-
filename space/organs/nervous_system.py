"""Nervous system: routes signals between organs without doing their work."""
from dataclasses import dataclass, field
from time import time
from typing import Any, Callable
import heapq

@dataclass(order=True, frozen=True)
class Signal:
    priority: int
    sequence: int
    kind: str = field(compare=False)
    source: str = field(compare=False)
    payload: Any = field(compare=False)
    created_at: float = field(default_factory=time, compare=False)

class NervousSystem:
    def __init__(self) -> None:
        self._queue: list[Signal] = []
        self._handlers: dict[str, list[Callable[[Signal], None]]] = {}
        self._sequence = 0

    def connect(self, kind: str, handler: Callable[[Signal], None]) -> None:
        self._handlers.setdefault(kind, []).append(handler)

    def emit(self, kind: str, source: str, payload: Any, priority: int = 100) -> Signal:
        self._sequence += 1
        signal = Signal(priority, self._sequence, kind, source, payload)
        heapq.heappush(self._queue, signal)
        return signal

    def dispatch_one(self) -> int:
        if not self._queue:
            return 0
        signal = heapq.heappop(self._queue)
        for handler in self._handlers.get(signal.kind, []):
            handler(signal)
        return 1

    def dispatch_all(self, limit: int = 100) -> int:
        count = 0
        while self._queue and count < limit:
            count += self.dispatch_one()
        return count

    def pending(self) -> int:
        return len(self._queue)
