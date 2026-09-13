"""Ω-PRESENT-1: append-only MEMORY ↔ PRESENT bridge."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping
from uuid import uuid4

from current_state import CurrentState


@dataclass(frozen=True)
class MemoryEvent:
    event_id: str
    predecessor_state_id: str
    successor_state_id: str
    cycle_id: str
    timestamp: str
    kind: str
    delta: Mapping[str, Any] = field(default_factory=dict)


@dataclass
class MemoryPresentLedger:
    """Minimal append-only evidence store for MEMORY ↔ PRESENT."""

    states: dict[str, CurrentState] = field(default_factory=dict)
    events: list[MemoryEvent] = field(default_factory=list)

    def append(self, state: CurrentState) -> None:
        if state.state_id in self.states:
            raise ValueError("state already exists; overwrite is forbidden")
        self.states[state.state_id] = state

    def link(self, previous: CurrentState, current: CurrentState, *, kind: str = "STATE_CHANGE") -> MemoryEvent:
        if previous.state_id not in self.states or current.state_id not in self.states:
            raise ValueError("both states must be appended before linking")
        event = record_state_change(previous, current, kind=kind)
        self.events.append(event)
        return event

    def reconstruct(self, start_state_id: str, end_state_id: str) -> CurrentState:
        state = self.states[start_state_id]
        while state.state_id != end_state_id:
            candidates = [e for e in self.events if e.predecessor_state_id == state.state_id]
            if len(candidates) != 1:
                raise ValueError("memory chain is missing or ambiguous")
            state = self.states[candidates[0].successor_state_id]
        return state


def record_state_change(previous: CurrentState, current: CurrentState, *, kind: str = "STATE_CHANGE") -> MemoryEvent:
    if previous.state_id == current.state_id:
        raise ValueError("memory event requires distinct states")
    if previous.cycle_id != current.cycle_id:
        raise ValueError("cross-cycle transition requires an explicit cycle event")

    fields = (
        "status", "active_work", "active_organs", "available_data",
        "missing_data", "known", "unknown", "constraints", "last_result",
        "memory_refs", "graph_ref",
    )
    delta = {
        name: {"from": getattr(previous, name), "to": getattr(current, name)}
        for name in fields
        if getattr(previous, name) != getattr(current, name)
    }
    return MemoryEvent(
        event_id=f"memory-event-{uuid4().hex}",
        predecessor_state_id=previous.state_id,
        successor_state_id=current.state_id,
        cycle_id=current.cycle_id,
        timestamp=datetime.now(timezone.utc).isoformat(),
        kind=kind,
        delta=delta,
    )
