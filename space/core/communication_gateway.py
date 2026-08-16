from dataclasses import dataclass
from typing import Any, Callable

from space.core.audience_policy import AudiencePolicy, AudienceRequest

@dataclass(frozen=True)
class CommunicationDecision:
    allowed: bool
    reason: str
    scope: str

class CommunicationGateway:
    """Single outbound communication gate for SPACE.

    Audience policy is checked first; Guardian is the final authorization gate.
    """
    def __init__(self, audience: AudiencePolicy, guardian_authorize: Callable[[AudienceRequest], bool]) -> None:
        self.audience = audience
        self.guardian_authorize = guardian_authorize

    def authorize(self, request: AudienceRequest) -> CommunicationDecision:
        audience_decision = self.audience.evaluate(request)
        if not audience_decision.allowed:
            return CommunicationDecision(False, audience_decision.reason, request.scope.value)
        if not self.guardian_authorize(request):
            return CommunicationDecision(False, "Guardian denied communication", request.scope.value)
        return CommunicationDecision(True, "communication authorized", request.scope.value)
