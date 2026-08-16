"""Minimal autonomous-organ contract for Ω-Space.

An organ owns its local state and memory reference. Cross-organ cooperation
uses explicit envelopes and must be authorized by the caller's boundary
layer. This module does not grant network, graph, memory-sharing, or execution
capabilities by itself.
"""
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class OrganMessage:
    message_id: str
    source: str
    target: str
    operation: str
    payload: Any = None
    capability: str | None = None


@dataclass
class AutonomousOrgan:
    organ_id: str
    state: dict[str, Any] = field(default_factory=dict)
    memory: list[dict[str, Any]] = field(default_factory=list)
    handlers: dict[str, Callable[[Any], Any]] = field(default_factory=dict)
    running: bool = True

    def register_operation(self, operation: str, handler: Callable[[Any], Any]) -> None:
        if not operation or operation.startswith("_"):
            raise ValueError("operation must be an explicit public contract")
        self.handlers[operation] = handler

    def handle_local(self, operation: str, payload: Any = None) -> Any:
        if not self.running:
            raise RuntimeError("organ is stopped")
        try:
            handler = self.handlers[operation]
        except KeyError as exc:
            raise PermissionError("operation is not part of this organ contract") from exc
        result = handler(payload)
        self.memory.append({"operation": operation, "result": result})
        return result

    def make_message(
        self, target: str, operation: str, payload: Any = None, capability: str | None = None
    ) -> OrganMessage:
        if not target or target == self.organ_id:
            raise ValueError("target must be another organ")
        return OrganMessage(
            message_id=f"{self.organ_id}:{len(self.memory) + 1}",
            source=self.organ_id,
            target=target,
            operation=operation,
            payload=payload,
            capability=capability,
        )

    def stop(self) -> None:
        self.running = False

    def start(self) -> None:
        self.running = True

    def snapshot(self) -> dict[str, Any]:
        return {
            "organ_id": self.organ_id,
            "state": dict(self.state),
            "memory": list(self.memory),
            "operations": sorted(self.handlers),
            "running": self.running,
        }
