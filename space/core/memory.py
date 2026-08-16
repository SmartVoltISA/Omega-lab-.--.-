"""Distributed structural memory for Ω-Space.

The store keeps local traces and whole-system events separately while exposing
one query surface. It is deterministic and dependency-free so it can later be
backed by a durable store without changing the organism interface.
"""
from dataclasses import dataclass, asdict
from time import time
from typing import Any


@dataclass(frozen=True)
class MemoryTrace:
    trace_id: str
    owner: str
    kind: str
    value: Any
    source: str
    created_at: float
    cycle: int


class DistributedMemory:
    def __init__(self) -> None:
        self._traces: dict[str, MemoryTrace] = {}
        self._counter = 0

    def remember(self, owner: str, kind: str, value: Any, source: str, cycle: int = 0) -> MemoryTrace:
        self._counter += 1
        trace = MemoryTrace(
            trace_id=f"mem-{self._counter}", owner=owner, kind=kind,
            value=value, source=source, created_at=time(), cycle=cycle,
        )
        self._traces[trace.trace_id] = trace
        return trace

    def get(self, trace_id: str) -> MemoryTrace:
        return self._traces[trace_id]

    def related(self, owner: str | None = None, kind: str | None = None, limit: int | None = None) -> list[MemoryTrace]:
        items = [
            t for t in self._traces.values()
            if (owner is None or t.owner == owner) and (kind is None or t.kind == kind)
        ]
        items.sort(key=lambda t: t.created_at, reverse=True)
        return items[:limit] if limit is not None else items

    def snapshot(self) -> list[dict[str, Any]]:
        return [asdict(t) for t in self._traces.values()]

    def latest(self, owner: str) -> MemoryTrace | None:
        items = self.related(owner=owner, limit=1)
        return items[0] if items else None
