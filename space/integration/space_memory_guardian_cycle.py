"""Minimal closed loop: Space action -> Guardian -> Memory/Graph feedback.

This is deliberately an in-memory deterministic prototype. It demonstrates
that an authorized result can become a provenance-bearing memory/graph event
without making the graph inspector responsible for policy or execution.
"""
from dataclasses import dataclass
from typing import Any

from space.integration.space_guardian_bridge import IntegrationResult, SpaceAction, SpaceGuardianBridge
from space.prototype.capability_registry import Capability
from space.security.guardian_core import SecurityEvidence
from tools.graph_memory_inspector.inspector import Finding, inspect_graph


@dataclass(frozen=True)
class MemoryEvent:
    event_id: str
    space_id: str
    action_id: str
    decision: str
    executed: bool
    provenance: str


class SpaceMemoryGuardianCycle:
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

    def graph_snapshot(self) -> dict[str, Any]:
        nodes = [
            {"id": "space:" + event.space_id, "state": "ACTIVE", "provenance": "cycle"}
            for event in self.events
        ]
        nodes += [
            {"id": event.event_id, "state": event.decision, "provenance": event.provenance}
            for event in self.events
        ]
        relations = [
            {
                "id": f"rel-{event.event_id}",
                "source": "space:" + event.space_id,
                "target": event.event_id,
                "type": "PRODUCED_EVENT",
                "provenance": event.provenance,
            }
            for event in self.events
        ]
        return {"nodes": nodes, "relations": relations}

    def inspect_feedback_graph(self) -> list[Finding]:
        return inspect_graph(self.graph_snapshot())
