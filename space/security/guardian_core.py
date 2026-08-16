from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "ALLOW"
    RESTRICT = "RESTRICT"
    BLOCK = "BLOCK"


@dataclass(frozen=True)
class SecurityEvidence:
    space_id: str
    device_key_id: str
    key_attested: bool
    integrity_ok: bool
    request_fresh: bool
    revoked: bool = False
    recovery_mode: bool = False
    foundation_ok: bool = True


class GuardianCore:
    """Deterministic policy core. It evaluates evidence; it does not collect secrets."""

    def decide(self, evidence: SecurityEvidence) -> Decision:
        # The Ω-Lab foundation is a protected invariant. It is never bypassed
        # by a request, recovery mode, or capability. A mismatch blocks the
        # boundary until the pinned foundation identity is restored.
        if not evidence.foundation_ok:
            return Decision.BLOCK
        if evidence.revoked:
            return Decision.BLOCK
        if not evidence.space_id or not evidence.device_key_id:
            return Decision.BLOCK
        if not evidence.key_attested:
            return Decision.RESTRICT
        if not evidence.integrity_ok:
            return Decision.RESTRICT
        if not evidence.request_fresh:
            return Decision.BLOCK
        if evidence.recovery_mode:
            return Decision.RESTRICT
        return Decision.ALLOW
