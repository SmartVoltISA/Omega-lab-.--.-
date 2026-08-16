"""Resource allocation boundary between SPACE and its hardware habitat.

CPU/RAM/GPU/VRAM/storage/network/device resources are represented as bounded
resources. Hardware adapters may use this contract without entering the core.
"""
from dataclasses import dataclass
from typing import Any

@dataclass
class Resource:
    resource_id: str
    kind: str
    capacity: float
    available: float
    metadata: dict[str, Any]

    def allocate(self, amount: float) -> bool:
        if amount < 0 or amount > self.available:
            return False
        self.available -= amount
        return True

    def release(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.available = min(self.capacity, self.available + amount)

class ResourceManager:
    def __init__(self) -> None:
        self.resources: dict[str, Resource] = {}

    def register(self, resource_id: str, kind: str, capacity: float, metadata: dict[str, Any] | None = None) -> Resource:
        if resource_id in self.resources:
            raise ValueError("duplicate resource")
        resource = Resource(resource_id, kind, capacity, capacity, metadata or {})
        self.resources[resource_id] = resource
        return resource

    def request(self, resource_id: str, amount: float) -> bool:
        return self.resources[resource_id].allocate(amount)

    def release(self, resource_id: str, amount: float) -> None:
        self.resources[resource_id].release(amount)

    def available(self, resource_id: str) -> float:
        return self.resources[resource_id].available

    def snapshot(self) -> dict[str, dict[str, Any]]:
        return {
            rid: {"kind": r.kind, "capacity": r.capacity, "available": r.available, "metadata": dict(r.metadata)}
            for rid, r in self.resources.items()
        }
