"""Small deterministic multi-organ exchange coordinator.

The coordinator deliberately delegates every cross-organ operation to the
Guardian router; it never grants direct organ-to-organ execution authority.
"""
from dataclasses import dataclass
from typing import Any

from space.integration.organ_guardian_router import OrganGuardianRouter
from space.organs.autonomous_organ import OrganMessage
from space.prototype.capability_registry import Capability
from space.security.guardian_core import SecurityEvidence


@dataclass(frozen=True)
class ExchangeStep:
    source: str
    target: str
    operation: str
    executed: bool


class MultiOrganExchange:
    def __init__(self, router: OrganGuardianRouter) -> None:
        self.router = router
        self.history: list[ExchangeStep] = []

    def send(
        self,
        source: str,
        target: str,
        operation: str,
        payload: Any,
        capability: str,
        capabilities: list[Capability],
        evidence: SecurityEvidence,
    ) -> ExchangeStep:
        message = OrganMessage(source, target, operation, payload, capability)
        result = self.router.dispatch(message, capabilities, evidence)
        step = ExchangeStep(source, target, operation, result.executed)
        self.history.append(step)
        return step
