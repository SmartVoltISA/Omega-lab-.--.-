"""Ω-PLAN-1: deterministic conversion of future orientation into an auditable plan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping
from uuid import uuid4


@dataclass(frozen=True)
class PlanStep:
    step_id: str
    action: str
    expected_result: str
    required_data: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()


@dataclass(frozen=True)
class Plan:
    plan_id: str
    source_future_id: str
    source_state_id: str
    desired_state: str
    next_result: str
    steps: tuple[PlanStep, ...]
    constraints: tuple[str, ...] = ()
    status: str = "PROPOSED"


def build_plan(
    *,
    source_future_id: str,
    source_state_id: str,
    desired_state: str,
    next_result: str,
    steps: list[Mapping[str, Any]],
    constraints: list[str] | None = None,
) -> Plan:
    """Convert a future orientation into a plan; reject untestable steps."""
    if not desired_state.strip() or not next_result.strip():
        raise ValueError("desired_state and next_result are required")
    if not steps:
        raise ValueError("plan requires at least one step")

    built: list[PlanStep] = []
    for raw in steps:
        action = str(raw.get("action", "")).strip()
        expected = str(raw.get("expected_result", "")).strip()
        if not action:
            raise ValueError("each plan step requires an action")
        if not expected:
            raise ValueError(f"step {action!r} has no expected_result")
        built.append(
            PlanStep(
                step_id=f"step-{uuid4().hex}",
                action=action,
                expected_result=expected,
                required_data=tuple(raw.get("required_data", ())),
                constraints=tuple(raw.get("constraints", ())),
            )
        )

    return Plan(
        plan_id=f"plan-{uuid4().hex}",
        source_future_id=source_future_id,
        source_state_id=source_state_id,
        desired_state=desired_state,
        next_result=next_result,
        steps=tuple(built),
        constraints=tuple(constraints or ()),
    )
