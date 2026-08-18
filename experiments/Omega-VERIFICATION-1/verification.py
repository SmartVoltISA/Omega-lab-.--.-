"""Ω-VERIFICATION-1: compare expected and actual execution results."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import uuid4


STATUSES = ("CONFIRMED", "PARTIAL", "FAILED", "UNKNOWN")


@dataclass(frozen=True)
class Verification:
    verification_id: str
    execution_id: str
    expected: Any
    actual: Any
    status: str
    reason: str


def verify(*, execution_id: str, expected: Any, actual: Any) -> Verification:
    if not execution_id.strip():
        raise ValueError("execution_id is required")

    if actual == expected:
        status = "CONFIRMED"
        reason = "actual result equals expected result"
    elif actual is None:
        status = "UNKNOWN"
        reason = "actual result is unavailable"
    else:
        status = "FAILED"
        reason = "actual result differs from expected result"

    return Verification(
        verification_id=f"verification-{uuid4().hex}",
        execution_id=execution_id,
        expected=expected,
        actual=actual,
        status=status,
        reason=reason,
    )
