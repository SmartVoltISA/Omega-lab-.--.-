"""Minimal deterministic Space ↔ Guardian integration bridge.

The bridge deliberately contains no model, network or secret handling. It
connects a Space capability snapshot to Guardian's policy decision so the
components can be tested independently and together.
"""
from dataclasses import dataclass
from typing import Iterable

from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, GuardianCore, SecurityEvidence


@dataclass(frozen=True)
class SpaceAction:
    action_id: str
    required_capabilities: tuple[str, ...] = ()


@dataclass(frozen=True)
class IntegrationResult:
    decision: Decision
    missing_capabilities: tuple[str, ...]
    executed: bool


class SpaceGuardianBridge:
    def __init__(self, guardian: GuardianCore | None = None) -> None:
        self.guardian = guardian or GuardianCore()

    @staticmethod
    def _verified_ids(capabilities: Iterable[Capability]) -> set[str]:
        return {c.capability_id for c in capabilities if c.verification_state == "VERIFIED"}

    def authorize(
        self,
        action: SpaceAction,
        capabilities: Iterable[Capability],
        evidence: SecurityEvidence,
    ) -> IntegrationResult:
        verified = self._verified_ids(capabilities)
        missing = tuple(cid for cid in action.required_capabilities if cid not in verified)
        decision = self.guardian.decide(evidence)
        if missing and decision == Decision.ALLOW:
            decision = Decision.RESTRICT
        return IntegrationResult(
            decision=decision,
            missing_capabilities=missing,
            executed=decision == Decision.ALLOW,
        )
