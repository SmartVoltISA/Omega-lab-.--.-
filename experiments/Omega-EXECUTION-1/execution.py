"""Ω-EXECUTION-1: bounded PLAN → GUARDIAN → ACTION → RESULT boundary.

The executor never interprets free-form text as executable code. Actions must be
registered explicitly, and authorization must be supplied by Guardian.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Mapping, Any
from uuid import uuid4


@dataclass(frozen=True)
class Authorization:
    authorization_id: str
    plan_id: str
    step_id: str
    authorized_by: str
    reason: str
    granted: bool


@dataclass(frozen=True)
class ExecutionResult:
    execution_id: str
    plan_id: str
    step_id: str
    action: str
    status: str
    actual_result: Any
    timestamp: str
    authorization_id: str


class Guardian:
    """Narrow authorization gate between plan and execution."""

    def authorize(self, plan_id: str, step_id: str, *, authorized_by: str, reason: str) -> Authorization:
        if not authorized_by.strip():
            raise ValueError("authorized_by is required")
        if not reason.strip():
            raise ValueError("authorization reason is required")
        return Authorization(
            authorization_id=f"auth-{uuid4().hex}",
            plan_id=plan_id,
            step_id=step_id,
            authorized_by=authorized_by,
            reason=reason,
            granted=True,
        )


class BoundedExecutor:
    """Execute only registered operations after explicit Guardian authorization."""

    def __init__(self) -> None:
        self._actions: dict[str, Callable[[], Any]] = {}

    def register(self, action: str, operation: Callable[[], Any]) -> None:
        if not action.strip():
            raise ValueError("action name is required")
        if action in self._actions:
            raise ValueError("action already registered")
        self._actions[action] = operation

    def execute(self, plan: Any, step: Any, authorization: Authorization) -> ExecutionResult:
        if not authorization.granted:
            raise PermissionError("Guardian authorization denied")
        if authorization.plan_id != plan.plan_id or authorization.step_id != step.step_id:
            raise PermissionError("authorization does not match plan step")
        if step.action not in self._actions:
            raise PermissionError(f"unregistered action: {step.action}")

        operation = self._actions[step.action]
        try:
            actual = operation()
            status = "SUCCESS"
        except Exception as exc:  # result records failure; it is not hidden
            actual = {"error_type": type(exc).__name__, "message": str(exc)}
            status = "FAILED"

        return ExecutionResult(
            execution_id=f"exec-{uuid4().hex}",
            plan_id=plan.plan_id,
            step_id=step.step_id,
            action=step.action,
            status=status,
            actual_result=actual,
            timestamp=datetime.now(timezone.utc).isoformat(),
            authorization_id=authorization.authorization_id,
        )
