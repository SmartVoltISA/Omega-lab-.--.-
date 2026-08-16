"""Trust-aware relationship layer for SPACE-to-SPACE interaction.

Lineage explains relationship; Trust Ledger supplies current trust evidence;
Guardian remains the final authorization boundary.
"""
from dataclasses import dataclass, asdict
from typing import Any

from space.core.space_hierarchy import SpaceHierarchy
from space.core.trust import TrustLedger

@dataclass(frozen=True)
class RelationshipContext:
    sender: str
    receiver: str
    relation: str
    trust_score: float
    capability: str
    purpose: str
    evidence: tuple[str, ...] = ()

class SpaceRelationship:
    def __init__(self, hierarchy: SpaceHierarchy, trust: TrustLedger) -> None:
        self.hierarchy = hierarchy
        self.trust = trust

    def context(self, sender: str, receiver: str, capability: str, purpose: str, evidence: tuple[str, ...] = ()) -> RelationshipContext:
        relation = self.hierarchy.relationship(sender, receiver)["relation"]
        trust_score = self.trust.score(receiver)
        return RelationshipContext(sender, receiver, relation, trust_score, capability, purpose, evidence)

    def can_request(self, ctx: RelationshipContext, minimum_trust: float = 0.5) -> bool:
        return ctx.trust_score >= minimum_trust

    def explain(self, ctx: RelationshipContext) -> dict[str, Any]:
        return asdict(ctx) | {"trust_sufficient": self.can_request(ctx)}
