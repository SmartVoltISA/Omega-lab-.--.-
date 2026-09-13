"""Ω-PRESENT-1: minimal, append-only current-state model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping
from uuid import uuid4


def _copy_map(value: Mapping[str, Any] | None) -> dict[str, Any]:
    return dict(value or {})


def _copy_list(value: list[str] | tuple[str, ...] | None) -> tuple[str, ...]:
    return tuple(value or ())


@dataclass(frozen=True)
class CurrentState:
    """Operational PRESENT state; no future intent is stored here."""

    state_id: str
    cycle_id: str
    timestamp: str
    status: str
    active_work: tuple[str, ...] = ()
    active_organs: tuple[str, ...] = ()
    available_data: tuple[str, ...] = ()
    missing_data: tuple[str, ...] = ()
    known: Mapping[str, Any] = field(default_factory=dict)
    unknown: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()
    last_result: Mapping[str, Any] | None = None
    memory_refs: tuple[str, ...] = ()
    graph_ref: str | None = None

    @classmethod
    def create(
        cls,
        *,
        cycle_id: str,
        status: str,
        active_work: list[str] | None = None,
        active_organs: list[str] | None = None,
        available_data: list[str] | None = None,
        missing_data: list[str] | None = None,
        known: Mapping[str, Any] | None = None,
        unknown: list[str] | None = None,
        constraints: list[str] | None = None,
        last_result: Mapping[str, Any] | None = None,
        memory_refs: list[str] | None = None,
        graph_ref: str | None = None,
    ) -> "CurrentState":
        return cls(
            state_id=f"state-{uuid4().hex}",
            cycle_id=cycle_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            status=status,
            active_work=_copy_list(active_work),
            active_organs=_copy_list(active_organs),
            available_data=_copy_list(available_data),
            missing_data=_copy_list(missing_data),
            known=_copy_map(known),
            unknown=_copy_list(unknown),
            constraints=_copy_list(constraints),
            last_result=_copy_map(last_result) if last_result is not None else None,
            memory_refs=_copy_list(memory_refs),
            graph_ref=graph_ref,
        )


@dataclass(frozen=True)
class StateTransition:
    """Immutable edge between two PRESENT states."""

    transition_id: str
    predecessor_id: str
    successor_id: str
    cycle_id: str
    timestamp: str
    delta: Mapping[str, Any]


def transition(
    previous: CurrentState,
    *,
    cycle_id: str | None = None,
    **changes: Any,
) -> tuple[CurrentState, StateTransition]:
    """Create a new state and explicit delta without mutating ``previous``."""

    allowed = {
        "status",
        "active_work",
        "active_organs",
        "available_data",
        "missing_data",
        "known",
        "unknown",
        "constraints",
        "last_result",
        "memory_refs",
        "graph_ref",
    }
    unexpected = set(changes) - allowed
    if unexpected:
        raise ValueError(f"unsupported state fields: {sorted(unexpected)}")

    next_cycle_id = cycle_id or previous.cycle_id
    values = {
        "cycle_id": next_cycle_id,
        "status": previous.status,
        "active_work": previous.active_work,
        "active_organs": previous.active_organs,
        "available_data": previous.available_data,
        "missing_data": previous.missing_data,
        "known": previous.known,
        "unknown": previous.unknown,
        "constraints": previous.constraints,
        "last_result": previous.last_result,
        "memory_refs": previous.memory_refs,
        "graph_ref": previous.graph_ref,
    }

    for key, value in changes.items():
        if key in {
            "active_work", "active_organs", "available_data", "missing_data",
            "unknown", "constraints", "memory_refs"
        }:
            value = _copy_list(value)
        elif key == "known":
            value = _copy_map(value)
        elif key == "last_result" and value is not None:
            value = _copy_map(value)
        values[key] = value

    successor = CurrentState(
        state_id=f"state-{uuid4().hex}",
        timestamp=datetime.now(timezone.utc).isoformat(),
        **values,
    )

    changed_fields = set(changes)
    if next_cycle_id != previous.cycle_id:
        changed_fields.add("cycle_id")

    delta = {
        key: {"from": getattr(previous, key), "to": getattr(successor, key)}
        for key in changed_fields
        if getattr(previous, key) != getattr(successor, key)
    }

    edge = StateTransition(
        transition_id=f"transition-{uuid4().hex}",
        predecessor_id=previous.state_id,
        successor_id=successor.state_id,
        cycle_id=successor.cycle_id,
        timestamp=successor.timestamp,
        delta=delta,
    )
    return successor, edge
