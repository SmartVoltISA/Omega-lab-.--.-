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


def record_state_change(
    previous: CurrentState,
    current: CurrentState,
    *,
    kind: str = "STATE_CHANGE",
) -> MemoryEvent:
    """Create a durable memory event linking two PRESENT states."""
    if previous.state_id == current.state_id:
        raise ValueError("memory event requires distinct states")
    if previous.cycle_id != current.cycle_id:
        raise ValueError("cross-cycle transition must be explicitly represented by a new cycle event")

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


def reconstruct_state(start: CurrentState, events: list[MemoryEvent]) -> CurrentState:
    """Replay a verified same-cycle event chain onto a starting state."""
    state = start
    for event in events:
        if event.predecessor_state_id != state.state_id:
            raise ValueError("memory chain has a broken predecessor link")
        if event.cycle_id != state.cycle_id:
            raise ValueError("memory chain crosses cycle boundary")
        # The event is provenance; the successor itself remains the authoritative state.
        # Replay therefore requires the caller to provide the actual successor through an
        # attached transition store in a full implementation. This function intentionally
        # refuses to invent state from a delta-only historical record.
        raise ValueError(
            "reconstruction requires successor state records; delta-only events are not enough"
        )
    return state
