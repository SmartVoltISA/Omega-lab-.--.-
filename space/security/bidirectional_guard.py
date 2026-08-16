"""Bidirectional security gate.

The gate deliberately separates direction, identity evidence, capability and
scope. It is a policy boundary, not a network implementation.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any

from space.security.guardian_core import Decision, GuardianCore, SecurityEvidence

class Direction(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

@dataclass(frozen=True)
class BoundaryRequest:
    request_id: str
    direction: Direction
    source: str
    target: str
    capability_id: str
    operation: str
    payload: Any = None
    scope: str = "default"

@dataclass(frozen=True)
class BoundaryDecision:
    decision: Decision
    reason: str
    request_id: str

class BidirectionalGuardian:
    """One policy gate for both external ingress and organism egress."""
    def __init__(self, guardian: GuardianCore | None = None) -> None:
        self.guardian = guardian or GuardianCore()
        self._blocked_scopes: set[str] = set()

    def block_scope(self, scope: str) -> None:
        self._blocked_scopes.add(scope)

    def allow_scope(self, scope: str) -> None:
        self._blocked_scopes.discard(scope)

    def inspect(self, request: BoundaryRequest, evidence: SecurityEvidence) -> BoundaryDecision:
        if request.scope in self._blocked_scopes:
            return BoundaryDecision(Decision.BLOCK, "scope quarantined", request.request_id)
        if not request.source or not request.target or not request.capability_id:
            return BoundaryDecision(Decision.BLOCK, "incomplete boundary identity", request.request_id)
        decision = self.guardian.decide(evidence)
        if decision != Decision.ALLOW:
            return BoundaryDecision(decision, "guardian policy denied boundary crossing", request.request_id)
        return BoundaryDecision(Decision.ALLOW, f"authorized {request.direction.value.lower()} interaction", request.request_id)
