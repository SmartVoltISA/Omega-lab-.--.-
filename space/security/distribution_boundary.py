"""Hard boundary for external/distributed capabilities.

Default policy is deny. This module deliberately contains no networking,
Bluetooth, discovery, replication, or self-deployment implementation.
It only defines the policy boundary those future tools must cross.
"""
from dataclasses import dataclass
from enum import Enum


class Capability(str, Enum):
    NETWORK = "network"
    BLUETOOTH = "bluetooth"
    PEER_DISCOVERY = "peer_discovery"
    MEMORY_SHARING = "memory_sharing"
    CAPABILITY_DELEGATION = "capability_delegation"
    SELF_DEPLOYMENT = "self_deployment"


@dataclass(frozen=True)
class DistributionRequest:
    request_id: str
    capability: Capability
    source: str
    target: str


class DistributionBoundary:
    """Default-deny boundary for distributed/external behavior."""

    def inspect(self, request: DistributionRequest) -> bool:
        # No capability is implicitly granted. A future explicit user-mediated
        # policy can be layered above this boundary without changing the core.
        return False

    def can_delegate(self, *_args, **_kwargs) -> bool:
        return False

    def can_discover_peers(self, *_args, **_kwargs) -> bool:
        return False

    def can_share_memory(self, *_args, **_kwargs) -> bool:
        return False

    def can_self_deploy(self, *_args, **_kwargs) -> bool:
        return False
