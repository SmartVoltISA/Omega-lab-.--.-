"""Integrated Ω-Space organism runtime.

The runtime closes the operational ring: state -> memory/context -> graph ->
action -> Guardian -> execution -> feedback -> memory/state/graph.
"""
from dataclasses import dataclass
from typing import Any, Callable

from space.core.graph import GraphCore
from space.core.loop_guard import LoopGuard
from space.core.memory import DistributedMemory
from space.core.state import SpaceState
from space.core.tool_registry import ToolRegistry, Tool
from space.integration.space_guardian_bridge import SpaceAction, SpaceGuardianBridge
from space.prototype.capability_registry import Capability, CapabilityRegistry
from space.security.guardian_core import SecurityEvidence

@dataclass(frozen=True)
class OrganismResult:
    decision: str
    executed: bool
    output: Any
    feedback: dict[str, Any]
    guard_action: str

class SpaceOrganism:
    def __init__(self, space_id: str = "space-1") -> None:
        self.state = SpaceState(space_id)
        self.memory = DistributedMemory()
        self.graph = GraphCore()
        self.capabilities = CapabilityRegistry()
        self.tools = ToolRegistry()
        self.guardian = SpaceGuardianBridge()
        self.loop_guard = LoopGuard()
        self.graph.upsert_node(f"space:{space_id}", {"mode": "ACTIVE"})

    def register_capability(self, capability: Capability) -> None:
        self.capabilities.register(capability)

    def register_tool(self, tool_id: str, description: str, capability_id: str, handler: Callable[..., Any]) -> None:
        self.tools.register(Tool(tool_id, description, capability_id, handler))

    def _activate_context(self, owner: str) -> list[dict[str, Any]]:
        return [m.__dict__ for m in self.memory.related(owner=owner, limit=8)]

    def step(self, tool_id: str, evidence: SecurityEvidence, **inputs: Any) -> OrganismResult:
        tool = self.tools.get(tool_id)
        action = SpaceAction(f"{tool_id}-cycle-{self.state.cycle + 1}", (tool.capability_id,))
        decision = self.guardian.authorize(action, self.capabilities.all(), evidence)
        context = self._activate_context(self.state.space_id)
        output = None
        if decision.executed:
            output = self.tools.call(tool_id, context=context, state=self.state.snapshot(), **inputs)
        feedback = {
            "tool": tool_id,
            "decision": decision.decision.value,
            "executed": decision.executed,
            "output": output,
            "cycle": self.state.cycle,
        }
        self.state.last_result = output
        self.state.last_feedback = feedback
        self.state.cycle += 1
        self.state.update(last_tool=tool_id, last_decision=decision.decision.value)
        trace = self.memory.remember(self.state.space_id, "feedback", feedback, f"tool:{tool_id}", self.state.cycle)
        event_id = f"event:{self.state.cycle}"
        self.graph.upsert_node(event_id, feedback, trace.trace_id)
        self.graph.connect(f"space:{self.state.space_id}", event_id, "PRODUCED_FEEDBACK", trace.trace_id)
        guard = self.loop_guard.observe(self.state.snapshot(), tool_id, output)
        if guard.action == "STOP_REPLAN":
            self.state.mode = "REPLAN"
        return OrganismResult(decision.decision.value, decision.executed, output, feedback, guard.action)

    def snapshot(self) -> dict[str, Any]:
        return {
            "state": self.state.snapshot(),
            "memory": self.memory.snapshot(),
            "graph": self.graph.snapshot(),
            "capabilities": [c.__dict__ for c in self.capabilities.all()],
            "tools": [t.tool_id for t in self.tools.list()],
        }
