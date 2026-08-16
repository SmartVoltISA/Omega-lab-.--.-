"""Isolated cycle domain: SPACE action -> Guardian -> cycle memory.

The cycle may retain relations between its own states and events, but it is
not allowed to materialize those relations as the operational GraphCore.
Graph construction is a separate domain with its own boundary.
"""
from dataclasses import dataclass

from space.integration.space_guardian_bridge import IntegrationResult, SpaceAction, SpaceGuardianBridge
from space.prototype.capability_registry import Capability
from space.security.guardian_core import SecurityEvidence


@dataclass(frozen=True)
class MemoryEvent:
    event_id: str
    space_id: str
    action_id: str
    decision: str
    executed: bool
    provenance: str


class SpaceMemoryGuardianCycle:
    """Closed cycle domain with no graph-construction capability."""

    def __init__(self, bridge: SpaceGuardianBridge | None = None) -> None:
        self.bridge = bridge or SpaceGuardianBridge()
        self.events: list[MemoryEvent] = []

    def step(
        self,
        action: SpaceAction,
        capabilities: list[Capability],
        evidence: SecurityEvidence,
        result_provenance: str,
    ) -> IntegrationResult:
        result = self.bridge.authorize(action, capabilities, evidence)
        self.events.append(
            MemoryEvent(
                event_id=f"event-{len(self.events) + 1}",
                space_id=evidence.space_id,
                action_id=action.action_id,
                decision=result.decision.value,
                executed=result.executed,
                provenance=result_provenance,
            )
        )
        return result

    def cycle_snapshot(self) -> dict[str, list[dict[str, str]]]:
        """Return cycle-local state only; never a GraphCore representation."""
        states = [
            {"id": event.event_id, "state": event.decision, "provenance": event.provenance}
            for event in self.events
        ]
        relations = [
            {
                "id": f"cycle-rel-{event.event_id}",
                "source": "cycle:" + event.space_id,
                "target": event.event_id,
                "type": "CYCLE_PRODUCED_EVENT",
                "provenance": event.provenance,
            }
            for event in self.events
        ]
        return {"states": states, "relations": relations}

    def graph_snapshot(self):
        raise PermissionError("cycle domain cannot be materialized as operational graph")

    def inspect_feedback_graph(self):
        raise PermissionError("cycle domain cannot enter graph inspection domain")
