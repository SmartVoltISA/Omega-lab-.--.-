"""Audience scoping for SPACE messages.

Audience selection is a security boundary. Family, trusted contacts, groups,
and broadcast are distinct scopes and never collapse into one generic send.
Guardian remains the final authorization layer.
"""
from dataclasses import dataclass
from enum import Enum

class AudienceScope(str, Enum):
    SELF = "SELF"
    FAMILY = "FAMILY"
    GROUP = "GROUP"
    TRUSTED_CONTACTS = "TRUSTED_CONTACTS"
    SPECIFIC_RECIPIENTS = "SPECIFIC_RECIPIENTS"
    PUBLIC = "PUBLIC"

@dataclass(frozen=True)
class AudienceRequest:
    sender: str
    scope: AudienceScope
    recipients: tuple[str, ...]
    purpose: str
    capability_id: str
    sensitivity: str = "NORMAL"
    requires_consent: bool = False

@dataclass(frozen=True)
class AudienceDecision:
    allowed: bool
    reason: str
    scope: AudienceScope

class AudiencePolicy:
    def __init__(self) -> None:
        self._memberships: dict[str, set[str]] = {}
        self._trusted: dict[str, set[str]] = {}
        self._consents: set[tuple[str, str, AudienceScope]] = set()

    def add_family_member(self, owner: str, member: str) -> None:
        self._memberships.setdefault(owner, set()).add(member)

    def add_trusted_contact(self, owner: str, contact: str) -> None:
        self._trusted.setdefault(owner, set()).add(contact)

    def grant_consent(self, owner: str, recipient: str, scope: AudienceScope) -> None:
        self._consents.add((owner, recipient, scope))

    def evaluate(self, request: AudienceRequest) -> AudienceDecision:
        if request.scope == AudienceScope.SELF:
            allowed = request.recipients == (request.sender,)
        elif request.scope == AudienceScope.FAMILY:
            allowed = bool(request.recipients) and all(r in self._memberships.get(request.sender, set()) for r in request.recipients)
        elif request.scope == AudienceScope.TRUSTED_CONTACTS:
            allowed = bool(request.recipients) and all(r in self._trusted.get(request.sender, set()) for r in request.recipients)
        elif request.scope in (AudienceScope.GROUP, AudienceScope.SPECIFIC_RECIPIENTS):
            allowed = bool(request.recipients)
        else:
            allowed = not request.requires_consent
        if request.requires_consent:
            allowed = allowed and all((request.sender, r, request.scope) in self._consents for r in request.recipients)
        return AudienceDecision(allowed, "audience scope accepted" if allowed else "audience scope denied", request.scope)
