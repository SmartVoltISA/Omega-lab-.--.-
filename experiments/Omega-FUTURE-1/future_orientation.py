"""Ω-FUTURE-1: deterministic, structured future orientation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping
from uuid import uuid4


HORIZONS = ("NEXT", "NEAR", "FAR")


@dataclass(frozen=True)
class CandidateAction:
    action_id: str
    description: str
    expected_result: str
    required_data: tuple[str, ...] = ()


@dataclass(frozen=True)
class FutureOrientation:
    orientation_id: str
    desired_state: str
    next_result: str
    data_gap: tuple[str, ...]
    data_needed: tuple[str, ...]
    candidate_actions: tuple[CandidateAction, ...]
    horizon: str = "NEXT"


def orient(
    *,
    current: Mapping[str, Any],
    memory: Mapping[str, Any],
    goal: str,
    available_data: tuple[str, ...] = (),
    constraints: tuple[str, ...] = (),
    desired_state: str,
    next_result: str,
    data_needed: tuple[str, ...] = (),
    candidate_actions: tuple[CandidateAction, ...] = (),
    horizon: str = "NEXT",
) -> FutureOrientation:
    """Produce orientation only; no action is executed."""
    if not goal.strip():
        raise ValueError("goal is required")
    if not desired_state.strip() or not next_result.strip():
        raise ValueError("desired_state and next_result are required")
    if horizon not in HORIZONS:
        raise ValueError(f"unsupported horizon: {horizon}")

    available = set(available_data)
    needed = tuple(dict.fromkeys(data_needed))
    gap = tuple(item for item in needed if item not in available)

    # Inputs are accepted explicitly so the organ's provenance contract is visible.
    # The first implementation does not infer hidden facts from them.
    _ = current, memory, constraints

    return FutureOrientation(
        orientation_id=f"orientation-{uuid4().hex}",
        desired_state=desired_state,
        next_result=next_result,
        data_gap=gap,
        data_needed=needed,
        candidate_actions=candidate_actions,
        horizon=horizon,
    )
