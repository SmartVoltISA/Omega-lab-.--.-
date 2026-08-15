"""Ω-Space capability registry — minimal read-only MVP.

This prototype records what the environment claims to have and separates
claims from verification. It does not execute arbitrary capabilities.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Capability:
    capability_id: str
    description: str
    organs: tuple[str, ...] = ()
    permissions: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()
    verification_state: str = "UNVERIFIED"
    provenance: Optional[str] = None


class CapabilityRegistry:
    """Minimal registry for explicit capability discovery."""

    VALID_STATES = {"UNVERIFIED", "VERIFIED", "BLOCKED", "DEGRADED"}

    def __init__(self) -> None:
        self._items: Dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        if capability.verification_state not in self.VALID_STATES:
            raise ValueError("invalid verification state")
        if capability.capability_id in self._items:
            raise ValueError("duplicate capability id")
        self._items[capability.capability_id] = capability

    def get(self, capability_id: str) -> Capability:
        return self._items[capability_id]

    def all(self) -> List[Capability]:
        return list(self._items.values())

    def available(self) -> List[Capability]:
        return [x for x in self._items.values() if x.verification_state == "VERIFIED"]

    def missing_or_unverified(self, required_ids: List[str]) -> List[str]:
        return [
            cid for cid in required_ids
            if cid not in self._items or self._items[cid].verification_state != "VERIFIED"
        ]

    def snapshot(self) -> tuple[Capability, ...]:
        return tuple(self._items.values())
