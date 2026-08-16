"""Resource allocation boundary between SPACE and its hardware habitat.

CPU/RAM/GPU/VRAM/storage/network/device resources are represented as bounded
resources. Hardware adapters may use this contract without entering the core.
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

    def register(self, resource: Resource) -> None:
        if resource.resource_id in self.resources:
            raise ValueError("duplicate resource")
        self.resources[resource.resource_id] = resource

    def request(self, claim_id: str, owner: str, resource_id: str, amount: float, unit: str | None = None) -> bool:
        if amount < 0:
            return False
        resource = self.resources.get(resource_id)
        if resource is None or not resource.available:
            return False
        used = sum(c.amount for c in self.claims.values() if c.resource_id == resource_id and not c.released)
        if resource.capacity is not None and used + amount > resource.capacity:
            return False
        self.claims[claim_id] = ResourceClaim(claim_id, owner, resource_id, amount, unit)
        return True

    def release(self, claim_id: str) -> bool:
        claim = self.claims.get(claim_id)
        if claim is None or claim.released:
            return False
        claim.released = True
        return True

    def available(self, resource_id: str) -> float | None:
        resource = self.resources[resource_id]
        if resource.capacity is None:
            return None
        used = sum(c.amount for c in self.claims.values() if c.resource_id == resource_id and not c.released)
        return max(0.0, resource.capacity - used)

    def snapshot(self) -> dict[str, Any]:
        return {"resources": {k: vars(v) for k, v in self.resources.items()}, "claims": {k: vars(v) for k, v in self.claims.items()}}
