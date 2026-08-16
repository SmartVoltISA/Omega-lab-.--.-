"""Quarantine boundary for unhealthy autonomous organs.

Quarantine is fail-closed: it prevents dispatch into an isolated organ while
leaving unrelated organs available to the runtime. It performs no network or
self-deployment operations.
"""
from dataclasses import dataclass, field

from space.organs.autonomous_organ import AutonomousOrgan, OrganRuntime


@dataclass
class OrganQuarantine:
    runtime: OrganRuntime
    isolated: set[str] = field(default_factory=set)

    def isolate(self, organ_id: str, reason: str) -> dict[str, str]:
        if organ_id not in self.runtime.organs:
            raise ValueError("organ is not registered")
        self.isolated.add(organ_id)
        self.runtime.organs[organ_id].stop()
        return {"organ": organ_id, "status": "quarantined", "reason": reason}

    def release(self, organ_id: str) -> None:
        if organ_id not in self.isolated:
            raise ValueError("organ is not quarantined")
        self.isolated.remove(organ_id)
        self.runtime.organs[organ_id].start()

    def is_isolated(self, organ_id: str) -> bool:
        return organ_id in self.isolated

    def available_organs(self) -> list[str]:
        return sorted(
            organ_id
            for organ_id, organ in self.runtime.organs.items()
            if organ.running and organ_id not in self.isolated
        )
