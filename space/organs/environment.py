"""Habitat boundary: describes the host environment without coupling the core to hardware."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Habitat:
    host_id: str
    platform: str
    architecture: str
    interfaces: set[str] = field(default_factory=set)
    resources: dict[str, Any] = field(default_factory=dict)
    devices: dict[str, dict[str, Any]] = field(default_factory=dict)

    def expose_interface(self, name: str) -> None:
        self.interfaces.add(name)

    def register_device(self, device_id: str, kind: str, metadata: dict[str, Any] | None = None) -> None:
        self.devices[device_id] = {"kind": kind, "metadata": metadata or {}}

    def snapshot(self) -> dict[str, Any]:
        return {
            "host_id": self.host_id,
            "platform": self.platform,
            "architecture": self.architecture,
            "interfaces": sorted(self.interfaces),
            "resources": dict(self.resources),
            "devices": dict(self.devices),
        }
