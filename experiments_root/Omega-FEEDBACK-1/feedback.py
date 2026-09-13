"""Ω-FEEDBACK-1: convert verified results into the next PRESENT state delta."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping
from uuid import uuid4

from verification import Verification


@dataclass(frozen=True)
class Feedback:
    feedback_id: str
    verification_id: str
    state_changes: Mapping[str, Any]
    next_cycle_required: bool
    reason: str


def derive_feedback(verification: Verification) -> Feedback:
    """Produce state-directed feedback without mutating PRESENT itself."""
    if verification.status == "CONFIRMED":
        changes = {"last_verification": "CONFIRMED", "last_result": verification.actual}
        next_cycle = True
        reason = "confirmed result can update PRESENT and continue the cycle"
    elif verification.status == "FAILED":
        changes = {"last_verification": "FAILED", "last_result": verification.actual}
        next_cycle = True
        reason = "failure is retained and requires re-planning or repair"
    else:
        changes = {"last_verification": verification.status}
        next_cycle = True
        reason = "uncertain/partial evidence must remain visible"

    return Feedback(
        feedback_id=f"feedback-{uuid4().hex}",
        verification_id=verification.verification_id,
        state_changes=changes,
        next_cycle_required=next_cycle,
        reason=reason,
    )
