"""Scoped boundary for external/distributed capabilities.

The system may model or execute ordinary domain operations inside an
explicitly isolated laboratory/sandbox. That is different from autonomous
external propagation. External peer discovery, memory sharing, capability
delegation and self-deployment remain explicit boundary events.
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
    LAB_REPRODUCTION = "lab_reproduction"


@dataclass(frozen=True)
class DistributionRequest:
    request_id: str
    capability: Capability
    source: str
    target: str
    scope: str = "external"


class DistributionBoundary:
    """Separate ordinary laboratory capability from external propagation."""

    SANDBOX_SCOPE = "sandbox"

    def inspect(self, request: DistributionRequest) -> bool:
        # Ordinary domain/reproduction experiments are allowed only inside an
        # explicit sandbox. External/distributed capabilities remain denied.
        if request.capability == Capability.LAB_REPRODUCTION:
            return request.scope == self.SANDBOX_SCOPE
        return False

    def can_lab_reproduce(self, scope: str = SANDBOX_SCOPE) -> bool:
        return scope == self.SANDBOX_SCOPE

    def can_delegate(self, *_args, **_kwargs) -> bool:
        return False

    def can_discover_peers(self, *_args, **_kwargs) -> bool:
        return False

    def can_share_memory(self, *_args, **_kwargs) -> bool:
        return False

    def can_self_deploy(self, *_args, **_kwargs) -> bool:
        return False
