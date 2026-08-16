"""Minimal autonomous-organ contract for Ω-Space.

Each organ owns local state and memory. Inter-organ cooperation is represented
by explicit message envelopes and a small runtime registry; the envelope never
executes by itself. This module grants no network, graph, shared-memory, or
capability-escalation authority.
"""
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class OrganMessage:
    source: str
    target: str
    operation: str
    payload: Any = None
    capability: str | None = None
    message_id: str | None = None


@dataclass
class AutonomousOrgan:
    organ_id: str
    state: dict[str, Any] = field(default_factory=dict)
    memory: list[dict[str, Any]] = field(default_factory=list)
    handlers: dict[str, Callable[[Any], Any]] = field(default_factory=dict)
    running: bool = True
    allowed_operations: set[str] | None = None

    def __post_init__(self) -> None:
        if self.allowed_operations is None:
            self.allowed_operations = set(self.handlers)
        else:
            self.allowed_operations = set(self.allowed_operations)

    @property
    def local_memory(self) -> list[dict[str, Any]]:
        return self.memory

    def remember(self, value: Any) -> None:
        self.memory.append({"value": value})

    def register_operation(self, operation: str, handler: Callable[[Any], Any]) -> None:
        if not operation or operation.startswith("_"):
            raise ValueError("operation must be an explicit public contract")
        self.handlers[operation] = handler
        self.allowed_operations.add(operation)

    def handle_local(self, operation: str, payload: Any = None) -> Any:
        if not self.running:
            raise RuntimeError("organ is stopped")
        if operation not in self.allowed_operations:
            raise PermissionError("operation is not part of this organ contract")
        try:
            handler = self.handlers[operation]
        except KeyError as exc:
            raise PermissionError("operation has no local implementation") from exc
        result = handler(payload)
        self.memory.append({"operation": operation, "result": result})
        return result

    def accept_message(self, message: OrganMessage) -> dict[str, Any]:
        if message.target != self.organ_id:
            raise ValueError("message target does not match organ")
        if message.operation not in self.allowed_operations:
            raise PermissionError("operation is not part of this organ contract")
        if not self.running:
            raise RuntimeError("organ is stopped")
        # Receiving a message is not permission to execute it. Without a
        # registered handler, the organ only acknowledges the contract.
        return {"organ": self.organ_id, "accepted": True, "operation": message.operation}

    def make_message(
        self, target: str, operation: str, payload: Any = None, capability: str | None = None
    ) -> OrganMessage:
        if not target or target == self.organ_id:
            raise ValueError("target must be another organ")
        return OrganMessage(
            source=self.organ_id,
            target=target,
            operation=operation,
            payload=payload,
            capability=capability,
            message_id=f"{self.organ_id}:{len(self.memory) + 1}",
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
            "operations": sorted(self.allowed_operations),
            "running": self.running,
        }


class OrganRuntime:
    """Minimal registry for routing envelopes; it is not an execution authority."""

    def __init__(self) -> None:
        self.organs: dict[str, AutonomousOrgan] = {}

    def register(self, organ: AutonomousOrgan) -> None:
        if organ.organ_id in self.organs:
            raise ValueError("organ id already registered")
        self.organs[organ.organ_id] = organ

    def send(self, message: OrganMessage) -> dict[str, Any]:
        try:
            target = self.organs[message.target]
        except KeyError as exc:
            raise ValueError("target organ is not registered") from exc
        return target.accept_message(message)
