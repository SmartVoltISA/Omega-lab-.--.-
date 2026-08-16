"""Guardian-mediated communication boundary for autonomous organs."""
from dataclasses import dataclass

from space.integration.space_guardian_bridge import SpaceAction, SpaceGuardianBridge
from space.organs.autonomous_organ import OrganMessage, OrganRuntime
from space.organs.quarantine import OrganQuarantine
from space.prototype.capability_registry import Capability
from space.security.guardian_core import Decision, SecurityEvidence


@dataclass(frozen=True)
class OrganDispatchResult:
    decision: Decision
    executed: bool
    target: str
    operation: str


class OrganGuardianRouter:
    """Routes organ messages only after quarantine and Guardian authorization."""

    def __init__(
        self,
        runtime: OrganRuntime,
        bridge: SpaceGuardianBridge | None = None,
        quarantine: OrganQuarantine | None = None,
    ) -> None:
        self.runtime = runtime
        self.bridge = bridge or SpaceGuardianBridge()
        self.quarantine = quarantine or OrganQuarantine(runtime)

    def dispatch(
        self,
        message: OrganMessage,
        capabilities: list[Capability],
        evidence: SecurityEvidence,
    ) -> OrganDispatchResult:
        if message.target not in self.runtime.organs:
            raise ValueError("target organ is not registered")
        target = self.runtime.organs[message.target]
        if self.quarantine.is_isolated(target.organ_id):
            return OrganDispatchResult(Decision.BLOCK, False, target.organ_id, message.operation)
        action = SpaceAction(
            action_id=f"organ:{message.source}:{message.target}:{message.operation}",
            required_capabilities=(message.capability,) if message.capability else (),
        )
        authorization = self.bridge.authorize(action, capabilities, evidence)
        if authorization.decision != Decision.ALLOW:
            return OrganDispatchResult(authorization.decision, False, target.organ_id, message.operation)
        if message.operation not in target.allowed_operations:
            return OrganDispatchResult(Decision.RESTRICT, False, target.organ_id, message.operation)
        if message.operation not in target.handlers or not target.running:
            return OrganDispatchResult(Decision.RESTRICT, False, target.organ_id, message.operation)
        target.handle_local(message.operation, message.payload)
        return OrganDispatchResult(Decision.ALLOW, True, target.organ_id, message.operation)
