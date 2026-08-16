"""Closed local organ loop: event -> action -> result -> evaluation -> memory."""
from typing import Any, Callable

from space.organs.autonomous_organ import AutonomousOrgan
from space.organs.causal_memory import CausalMemory, CausalRecord


class OrganClosedLoop:
    """Runs a causal loop entirely inside one organ boundary."""

    def __init__(self, organ: AutonomousOrgan, memory: CausalMemory | None = None) -> None:
        self.organ = organ
        self.memory = memory or CausalMemory()

    def step(
        self,
        event: str,
        operation: str,
        payload: Any = None,
        evaluate: Callable[[Any], str] | None = None,
    ) -> CausalRecord:
        result = self.organ.handle_local(operation, payload)
        evaluation = evaluate(result) if evaluate else "accepted"
        record = self.memory.record(event, operation, result, evaluation)
        self.organ.state["last_evaluation"] = evaluation
        self.organ.state["last_event"] = event
        return record

    def snapshot(self) -> dict[str, Any]:
        return {
            "organ_id": self.organ.organ_id,
            "state": dict(self.organ.state),
            "causal_memory": self.memory.snapshot(),
        }
