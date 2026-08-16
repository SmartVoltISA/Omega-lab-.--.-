"""Explicit family policy layer for multi-SPACE environments.

This layer expresses authorization policy; Guardian remains the final decision
maker. Wellbeing reporting is limited to observable signals and confidence,
not unsupported claims about a person's inner mental state.
"""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class FamilyMember:
    space_id: str
    role: str
    age_band: str
    verified_relation: bool = False

@dataclass(frozen=True)
class AccessRule:
    role: str
    age_band: str
    allowed_topics: tuple[str, ...]
    monitoring_level: str

class FamilyPolicy:
    def __init__(self) -> None:
        self.members: dict[str, FamilyMember] = {}
        self.rules: list[AccessRule] = []

    def add_member(self, member: FamilyMember) -> None:
        self.members[member.space_id] = member

    def add_rule(self, rule: AccessRule) -> None:
        self.rules.append(rule)

    def allowed_topics(self, space_id: str) -> tuple[str, ...]:
        member = self.members[space_id]
        topics: set[str] = set()
        for rule in self.rules:
            if rule.role == member.role and rule.age_band == member.age_band:
                topics.update(rule.allowed_topics)
        return tuple(sorted(topics))

    def monitoring_level(self, space_id: str) -> str:
        member = self.members[space_id]
        levels = [r.monitoring_level for r in self.rules if r.role == member.role and r.age_band == member.age_band]
        return levels[-1] if levels else "MINIMAL"

    def can_access(self, requester: str, subject: str, topic: str) -> bool:
        if requester not in self.members or subject not in self.members:
            return False
        return topic in self.allowed_topics(requester)

    def relationship_report(self) -> list[dict[str, Any]]:
        return [
            {"space_id": m.space_id, "role": m.role, "age_band": m.age_band,
             "verified_relation": m.verified_relation,
             "allowed_topics": self.allowed_topics(m.space_id),
             "monitoring_level": self.monitoring_level(m.space_id)}
            for m in self.members.values()
        ]
