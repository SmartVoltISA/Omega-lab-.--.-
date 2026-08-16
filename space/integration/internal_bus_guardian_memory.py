"""Integration boundary for SPACE's local semantic nervous system.

Flow:
semantic event -> Guardian -> organ handler -> Memory/Graph -> feedback.
The bus remains local and event-driven; full state is not copied into events.
"""
from dataclasses import dataclass
from typing import Any, Callable

from space.core.internal_bus import InternalSemanticBus, SemanticEvent

@dataclass(frozen=True)
class GuardedEventResult:
    event_id: str
    allowed: bool
    reason: str
    memory_ref: str | None = None
    graph_ref: str | None = None

class GuardedInternalBus:
    def __init__(
        self,
        bus: InternalSemanticBus,
        guardian: Callable[[SemanticEvent], tuple[bool, str]],
        memory_record: Callable[[SemanticEvent], str | None] | None = None,
        graph_record: Callable[[SemanticEvent], str | None] | None = None,
        feedback: Callable[[GuardedEventResult], None] | None = None,
    ) -> None:
        self.bus = bus
        self.guardian = guardian
        self.memory_record = memory_record
        self.graph_record = graph_record
        self.feedback = feedback

    def publish(self, event: SemanticEvent) -> GuardedEventResult:
        allowed, reason = self.guardian(event)
        if not allowed:
            result = GuardedEventResult(event.event_id, False, reason)
            if self.feedback:
                self.feedback(result)
            return result

        self.bus.publish(event)
        memory_ref = self.memory_record(event) if self.memory_record else None
        graph_ref = self.graph_record(event) if self.graph_record else None
        result = GuardedEventResult(event.event_id, True, reason, memory_ref, graph_ref)
        if self.feedback:
            self.feedback(result)
        return result

    def dispatch_one(self) -> bool:
        return self.bus.dispatch_one()
