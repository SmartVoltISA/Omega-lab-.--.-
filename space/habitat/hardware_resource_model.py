"""Hardware/resource contracts for the SPACE habitat.

This module deliberately models resources, not vendor-specific hardware.
Actual adapters belong at the habitat boundary and must be authorized before
protected I/O is performed.
"""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Resource:
    resource_id: str
    kind: str
    capacity: float | None = None
    unit: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    available: bool = True


@dataclass
class ResourceClaim:
    claim_id: str
    owner: str
    resource_id: str
    amount: float
    unit: str | None = None
    released: bool = False


class ResourceManager:
    """Deterministic accounting layer; no direct hardware access."""

    def __init__(self) -> None:
        self.resources: dict[str, Resource] = {}
        self.claims: dict[str, ResourceClaim] = {}

    def register(self, resource: Resource) -> None:
        self.resources[resource.resource_id] = resource

    def claim(self, claim: ResourceClaim) -> bool:
        resource = self.resources.get(claim.resource_id)
        if resource is None or not resource.available:
            return False
        if resource.capacity is not None:
            used = sum(
                c.amount for c in self.claims.values()
                if c.resource_id == claim.resource_id and not c.released
            )
            if used + claim.amount > resource.capacity:
                return False
        self.claims[claim.claim_id] = claim
        return True

    def release(self, claim_id: str) -> bool:
        claim = self.claims.get(claim_id)
        if claim is None:
            return False
        claim.released = True
        return True

    def snapshot(self) -> dict[str, Any]:
        return {
            "resources": {k: vars(v) for k, v in self.resources.items()},
            "claims": {k: vars(v) for k, v in self.claims.items()},
        }
