"""Resource allocation boundary between SPACE and its hardware habitat.

CPU/RAM/GPU/VRAM/storage/network/device resources are represented as bounded
resources. The manager accepts both the explicit claim API and the compact
legacy form used by the habitat boundary tests.
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
    def __init__(self) -> None:
        self.resources: dict[str, Resource] = {}
        self.claims: dict[str, ResourceClaim] = {}
        self._sequence = 0

    def register(self, resource: Resource | str, kind: str | None = None, capacity: float | None = None, unit: str | None = None) -> None:
        """Register a Resource object or register(id, kind, capacity, unit)."""
        if isinstance(resource, str):
            resource = Resource(resource, kind or "unknown", capacity, unit)
        if resource.resource_id in self.resources:
            raise ValueError("duplicate resource")
        self.resources[resource.resource_id] = resource

    def request(self, claim_id: str, owner: str | float, resource_id: str | None = None, amount: float | None = None, unit: str | None = None) -> bool:
        """Request a resource using explicit or compact (resource_id, amount) form."""
        if resource_id is None and isinstance(owner, (int, float)):
            resource_id, amount = claim_id, float(owner)
            self._sequence += 1
            claim_id, owner = f"claim-{self._sequence}", "space"
        if resource_id is None or amount is None:
            return False
        if amount < 0:
            return False
        resource = self.resources.get(resource_id)
        if resource is None or not resource.available:
            return False
        used = sum(c.amount for c in self.claims.values() if c.resource_id == resource_id and not c.released)
        if resource.capacity is not None and used + amount > resource.capacity:
            return False
        self.claims[claim_id] = ResourceClaim(claim_id, str(owner), resource_id, amount, unit)
        return True

    def release(self, claim_id: str, amount: float | None = None) -> bool:
        """Release a claim, or partially release the oldest active amount for a resource."""
        if amount is None:
            claim = self.claims.get(claim_id)
            if claim is None or claim.released:
                return False
            claim.released = True
            return True
        remaining = amount
        for claim in self.claims.values():
            if claim.resource_id == claim_id and not claim.released and remaining > 0:
                released = min(claim.amount, remaining)
                claim.amount -= released
                remaining -= released
                if claim.amount == 0:
                    claim.released = True
        return remaining == 0

    def available(self, resource_id: str) -> float | None:
        resource = self.resources[resource_id]
        if resource.capacity is None:
            return None
        used = sum(c.amount for c in self.claims.values() if c.resource_id == resource_id and not c.released)
        return max(0.0, resource.capacity - used)

    def snapshot(self) -> dict[str, Any]:
        return {"resources": {k: vars(v) for k, v in self.resources.items()}, "claims": {k: vars(v) for k, v in self.claims.items()}}
