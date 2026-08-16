"""Integrated Ω-Space organism runtime."""
from dataclasses import dataclass
from typing import Any, Callable

from space.core.audit import AuditLog
from space.core.event_bus import EventBus
from space.core.graph import GraphCore
from space.core.loop_guard import LoopGuard
from space.core.memory import DistributedMemory
from space.core.planner import Planner
from space.core.recovery import RecoveryManager
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
        self.planner = Planner()
        self.events = EventBus()
        self.audit = AuditLog()
        self.recovery = RecoveryManager()
        self.guardian = SpaceGuardianBridge()
        self.loop_guard = LoopGuard()
        self.graph.upsert_node(f"space:{space_id}", {"mode": "ACTIVE"})

    def observe(self, observation: Any, source: str = "input") -> None:
        self.state.update(observation=observation, observation_source=source)
        self.memory.remember(self.state.space_id, "observation", observation, source, self.state.cycle)
        self.events.publish("OBSERVATION", observation, self.state.cycle)

    def register_capability(self, capability: Capability) -> None:
        self.capabilities.register(capability)

    def register_tool(self, tool_id: str, description: str, capability_id: str, handler: Callable[..., Any]) -> None:
        self.tools.register(Tool(tool_id, description, capability_id, handler))

    def _activate_context(self, owner: str) -> list[dict[str, Any]]:
        return [m.__dict__ for m in self.memory.related(owner=owner, limit=8)]

    def step(self, tool_id: str, evidence: SecurityEvidence, **inputs: Any) -> OrganismResult:
        plan = self.planner.choose(tool_id, inputs)
        tool = self.tools.get(plan.tool_id)
        action = SpaceAction(f"{tool.tool_id}-cycle-{self.state.cycle + 1}", (tool.capability_id,))
        decision = self.guardian.authorize(action, self.capabilities.all(), evidence)
        context = self._activate_context(self.state.space_id)
        output = None
        if decision.executed:
            output = self.tools.call(tool.tool_id, context=context, state=self.state.snapshot(), **plan.inputs)
        feedback = {
            "tool": tool.tool_id,
            "decision": decision.decision.value,
            "executed": decision.executed,
            "output": output,
            "cycle": self.state.cycle,
            "plan_reason": plan.reason,
        }
        self.state.last_result = output
        self.state.last_feedback = feedback
        self.state.cycle += 1
        self.state.update(last_tool=tool.tool_id, last_decision=decision.decision.value)
        trace = self.memory.remember(self.state.space_id, "feedback", feedback, f"tool:{tool.tool_id}", self.state.cycle)
        event_id = f"event:{self.state.cycle}"
        self.graph.upsert_node(event_id, feedback, trace.trace_id)
        self.graph.connect(f"space:{self.state.space_id}", event_id, "PRODUCED_FEEDBACK", trace.trace_id)
        self.events.publish("RESULT", feedback, self.state.cycle)
        self.audit.record(self.state.cycle, tool.tool_id, decision.decision.value, plan.reason, feedback)
        semantic_state = {"mode": self.state.mode, "values": dict(self.state.values)}
        guard = self.loop_guard.observe(semantic_state, tool.tool_id, output)
        if guard.action == "STOP_REPLAN":
            self.state.mode = "REPLAN"
            self.events.publish("LOOP_GUARD", guard.reason, self.state.cycle)
            self.audit.record(self.state.cycle, "loop_guard", "STOP_REPLAN", "guard", guard.reason)
        return OrganismResult(decision.decision.value, decision.executed, output, feedback, guard.action)

    def recover(self, reason: str) -> None:
        decision = self.recovery.recover(reason, self.state.snapshot())
        self.state.mode = decision.mode
        self.memory.remember(self.state.space_id, "recovery", decision.reason, "recovery", self.state.cycle)
        self.events.publish("RECOVERY", decision.reason, self.state.cycle)
        self.audit.record(self.state.cycle, "recovery", decision.mode, "recovery", decision.reason)

    def snapshot(self) -> dict[str, Any]:
        return {
            "state": self.state.snapshot(),
            "memory": self.memory.snapshot(),
            "graph": self.graph.snapshot(),
            "events": self.events.recent(),
            "audit": self.audit.snapshot(),
            "capabilities": [c.__dict__ for c in self.capabilities.all()],
            "tools": [t.tool_id for t in self.tools.list()],
        }
