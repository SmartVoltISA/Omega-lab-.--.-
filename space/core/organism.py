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
from space.organs import (NervousSystem, CirculatorySystem, SensorySystem, MotorSystem, DigestiveSystem, Habitat, ImmuneSystem)
from space.habitat.resource_manager import ResourceManager, Resource
from space.habitat.guardian_io import GuardianIO, IORequest
from space.habitat.space_transport import SpaceTransport, SpaceMessage

@dataclass(frozen=True)
class OrganismResult:
    decision: str
    executed: bool
    output: Any
    feedback: dict[str, Any]
    guard_action: str

class SpaceOrganism:
    def __init__(self, space_id: str = "space-1", habitat: Habitat | None = None, llm_backend: Any = None) -> None:
        self.state = SpaceState(space_id)
        self.memory = DistributedMemory(); self.graph = GraphCore(); self.capabilities = CapabilityRegistry(); self.tools = ToolRegistry()
        self.planner = Planner(); self.events = EventBus(); self.audit = AuditLog(); self.recovery = RecoveryManager()
        self.guardian = SpaceGuardianBridge(); self.loop_guard = LoopGuard()
        self.nervous = NervousSystem(); self.circulatory = CirculatorySystem(); self.sensory = SensorySystem(); self.motor = MotorSystem()
        self.digestive = DigestiveSystem(llm_backend, "configured" if llm_backend else "none"); self.immune = ImmuneSystem(); self.habitat = habitat
        self.resources = ResourceManager(); self.io = GuardianIO(); self.space_transport = SpaceTransport()
        self.graph.upsert_node(f"space:{space_id}", {"mode": "ACTIVE"}); self.circulatory.register("cycle_budget", 1.0); self.circulatory.health = "HEALTHY"

    def observe(self, observation: Any, source: str = "input") -> None:
        self.state.update(observation=observation, observation_source=source); self.memory.remember(self.state.space_id, "observation", observation, source, self.state.cycle)
        self.events.publish("OBSERVATION", observation, self.state.cycle); self.nervous.emit("OBSERVATION", source, observation, priority=20)

    def sense(self, modality: str, source: str | None = None, reliability: float = 1.0) -> Any:
        observation = self.sensory.read(modality, source, reliability); self.observe(observation.payload, observation.source); return observation

    def register_capability(self, capability: Capability) -> None: self.capabilities.register(capability)
    def register_tool(self, tool_id: str, description: str, capability_id: str, handler: Callable[..., Any]) -> None: self.tools.register(Tool(tool_id, description, capability_id, handler))
    def register_sense(self, modality: str, reader: Callable[[], Any]) -> None: self.sensory.register(modality, reader)
    def register_actuator(self, actuator: str, handler: Callable[[Any], Any]) -> None: self.motor.register(actuator, handler)
    def register_resource(self, resource_id: str, kind: str, capacity: float | None = None, unit: str | None = None, metadata: dict[str, Any] | None = None) -> None: self.resources.register(Resource(resource_id, kind, capacity, unit, metadata or {}))
    def claim_resource(self, claim_id: str, resource_id: str, amount: float, unit: str | None = None) -> bool: return self.resources.request(claim_id, self.state.space_id, resource_id, amount, unit)
    def release_resource(self, claim_id: str) -> bool: return self.resources.release(claim_id)
    def register_io_adapter(self, interface: str, handler: Callable[[str, Any], Any]) -> None: self.io.register_adapter(interface, handler)
    def connect_space_peer(self, space_id: str, handler: Callable[[SpaceMessage], Any]) -> None: self.space_transport.register_peer(space_id, handler)

    def _authorize_capability(self, action_id: str, capability_id: str, evidence: SecurityEvidence):
        return self.guardian.authorize(SpaceAction(action_id, (capability_id,)), self.capabilities.all(), evidence)

    def external_io(self, request_id: str, interface: str, operation: str, capability_id: str, payload: Any, evidence: SecurityEvidence, direction: str = "out") -> Any:
        request = IORequest(request_id, interface, operation, capability_id, payload, direction)
        guardian_decision = self._authorize_capability(request_id, capability_id, evidence)
        self.io.authorizer = lambda _: guardian_decision.executed
        decision = self.io.execute(request)
        self.audit.record(self.state.cycle, f"io:{interface}:{operation}", guardian_decision.decision.value if not guardian_decision.executed else ("ALLOW" if decision.allowed else "BLOCK"), "guardian", {"request": request.__dict__, "reason": decision.reason})
        if decision.allowed:
            self.memory.remember(self.state.space_id, "external_io", {"request": request.__dict__, "result": decision.result}, f"interface:{interface}", self.state.cycle)
            self.events.publish("EXTERNAL_IO", {"interface": interface, "operation": operation, "result": decision.result}, self.state.cycle)
        return decision

    def send_space_message(self, message: SpaceMessage, evidence: SecurityEvidence) -> Any:
        guardian_decision = self._authorize_capability(message.message_id, message.capability_id, evidence)
        if not guardian_decision.executed:
            self.audit.record(self.state.cycle, "space_transport", guardian_decision.decision.value, "guardian", message.__dict__)
            raise PermissionError(f"Guardian denied SPACE message: {guardian_decision.decision.value}")
        self.space_transport.authorize = lambda _: True
        result = self.space_transport.send(message)
        self.memory.remember(self.state.space_id, "space_message", {"message": message.__dict__, "result": result}, "space_transport", self.state.cycle)
        self.nervous.emit("SPACE_MESSAGE", message.receiver, {"message": message.__dict__, "result": result}, priority=25)
        return result

    def _activate_context(self, owner: str) -> list[dict[str, Any]]: return [m.__dict__ for m in self.memory.related(owner=owner, limit=8)]
    def digest(self, input_id: str, prompt: str) -> Any: return self.digestive.digest(input_id, prompt, self._activate_context(self.state.space_id))

    def step(self, tool_id: str, evidence: SecurityEvidence, **inputs: Any) -> OrganismResult:
        plan = self.planner.choose(tool_id, inputs); tool = self.tools.get(plan.tool_id)
        decision = self._authorize_capability(f"{tool.tool_id}-cycle-{self.state.cycle + 1}", tool.capability_id, evidence)
        context = self._activate_context(self.state.space_id); output = None
        if decision.executed: output = self.tools.call(tool.tool_id, context=context, state=self.state.snapshot(), **plan.inputs)
        feedback = {"tool": tool.tool_id, "decision": decision.decision.value, "executed": decision.executed, "output": output, "cycle": self.state.cycle, "plan_reason": plan.reason}
        self.state.last_result = output; self.state.last_feedback = feedback; self.state.cycle += 1; self.state.update(last_tool=tool.tool_id, last_decision=decision.decision.value)
        trace = self.memory.remember(self.state.space_id, "feedback", feedback, f"tool:{tool.tool_id}", self.state.cycle); event_id = f"event:{self.state.cycle}"
        self.graph.upsert_node(event_id, feedback, trace.trace_id); self.graph.connect(f"space:{self.state.space_id}", event_id, "PRODUCED_FEEDBACK", trace.trace_id)
        self.events.publish("RESULT", feedback, self.state.cycle); self.nervous.emit("RESULT", tool.tool_id, feedback, priority=30); self.audit.record(self.state.cycle, tool.tool_id, decision.decision.value, plan.reason, feedback)
        anomalies = self.immune.inspect(tool.tool_id, feedback)
        if anomalies: self.events.publish("ANOMALY", [a.__dict__ for a in anomalies], self.state.cycle)
        self.circulatory.pulse(self.state.cycle, self.nervous.pending(), "HEALTHY" if decision.executed else "DEGRADED")
        guard = self.loop_guard.observe({"mode": self.state.mode, "values": dict(self.state.values)}, tool.tool_id, output)
        if guard.action == "STOP_REPLAN": self.state.mode = "REPLAN"; self.events.publish("LOOP_GUARD", guard.reason, self.state.cycle); self.audit.record(self.state.cycle, "loop_guard", "STOP_REPLAN", "guard", guard.reason)
        return OrganismResult(decision.decision.value, decision.executed, output, feedback, guard.action)

    def actuate(self, actuator: str, payload: Any, authorized: bool = False) -> Any:
        result = self.motor.execute(actuator, payload, authorized); self.events.publish("ACTUATION", result.__dict__, self.state.cycle); return result
    def recover(self, reason: str) -> None:
        decision = self.recovery.recover(reason, self.state.snapshot()); self.state.mode = decision.mode; self.memory.remember(self.state.space_id, "recovery", decision.reason, "recovery", self.state.cycle); self.events.publish("RECOVERY", decision.reason, self.state.cycle); self.audit.record(self.state.cycle, "recovery", decision.mode, "recovery", decision.reason)
    def snapshot(self) -> dict[str, Any]:
        return {"state": self.state.snapshot(), "memory": self.memory.snapshot(), "graph": self.graph.snapshot(), "events": self.events.recent(), "audit": self.audit.snapshot(), "capabilities": [c.__dict__ for c in self.capabilities.all()], "tools": [t.tool_id for t in self.tools.list()], "resources": self.resources.snapshot(), "organs": {"nervous_pending": self.nervous.pending(), "sensory_modalities": self.sensory.modalities(), "actuators": self.motor.actuators(), "llm_backend": self.digestive.backend_name, "immune_quarantined": sorted(self.immune._quarantined), "habitat": self.habitat.snapshot() if self.habitat else None}}
