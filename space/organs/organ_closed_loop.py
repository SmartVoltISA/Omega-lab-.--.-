"""Minimal closed behavioral loop for one autonomous organ.

The loop is intentionally local: event -> state -> action -> result ->
evaluation -> causal memory -> next state. It does not construct or mutate
the operational graph and it does not grant capabilities.
"""
from dataclasses import dataclass
from typing import Any, Callable

from space.organs.autonomous_organ import AutonomousOrgan
from space.organs.causal_memory import CausalMemory, CausalRecord


@dataclass(frozen=True)
class LoopResult:
    event: str
    action: str
    result: Any
    evaluation: str
    record_id: str


class OrganClosedLoop:
    def __init__(self, organ: AutonomousOrgan, memory: CausalMemory | None = None) -> None:
        self.organ = organ
        self.memory = memory or CausalMemory()
        self.state_history: list[dict[str, Any]] = []

    def run_once(
        self,
        event: str,
        action: str,
        payload: Any = None,
        evaluate: Callable[[Any], str] | None = None,
    ) -> LoopResult:
        if not event:
            raise ValueError("event is required")
        result = self.organ.handle_local(action, payload)
        evaluation = evaluate(result) if evaluate else "accepted"
        record = self.memory.record(event, action, result, evaluation)
        self.organ.state["last_event"] = event
        self.organ.state["last_action"] = action
        self.organ.state["last_evaluation"] = evaluation
        self.state_history.append(dict(self.organ.state))
        return LoopResult(event, action, result, evaluation, record.record_id)

    def snapshot(self) -> dict[str, Any]:
        return {
            "organ": self.organ.snapshot(),
            "causal_memory": self.memory.snapshot(),
            "state_history": list(self.state_history),
        }
