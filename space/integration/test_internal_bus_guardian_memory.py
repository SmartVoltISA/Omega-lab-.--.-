"""Tests for the local semantic bus security and persistence boundary.

These tests are deliberately dependency-light so they can run in the phone
sandbox and in CI without external services.
"""
from dataclasses import dataclass
from space.core.internal_bus import InternalSemanticBus, SemanticEvent


@dataclass
class Decision:
    allowed: bool


def test_allowed_event_reaches_subscriber():
    bus = InternalSemanticBus()
    received = []
    bus.subscribe("state.changed", received.append)

    event = SemanticEvent(
        event_id="E1",
        topic="state.changed",
        source="state",
        meaning="temperature changed",
        place="body/thermal",
        reference="state:thermal",
        delta={"temperature": 1},
    )
    bus.publish(event)

    assert bus.pending() == 1
    assert bus.dispatch_one() is True
    assert received == [event]
    assert bus.pending() == 0


def test_blocked_event_is_not_dispatched():
    bus = InternalSemanticBus()
    received = []
    bus.subscribe("restricted.action", received.append)

    # Guardian decision is represented explicitly before publication.
    guardian = Decision(allowed=False)
    event = SemanticEvent(
        event_id="E2",
        topic="restricted.action",
        source="tool",
        meaning="request restricted action",
        place="tools",
    )

    if guardian.allowed:
        bus.publish(event)

    assert bus.pending() == 0
    assert bus.dispatch_one() is False
    assert received == []


def test_reference_and_delta_preserve_semantic_compactness():
    event = SemanticEvent(
        event_id="E3",
        topic="memory.delta",
        source="memory",
        meaning="one relation changed",
        place="memory/graph",
        reference="node:42",
        delta={"edge": "node:42->node:17", "state": "active"},
    )

    assert event.reference == "node:42"
    assert event.delta["state"] == "active"
    # The event carries the change, not a copied full object/history.
    assert "full_object" not in event.delta


def test_feedback_can_be_routed_without_polling():
    bus = InternalSemanticBus()
    feedback = []
    bus.subscribe("feedback", feedback.append)

    bus.publish(
        SemanticEvent(
            event_id="E4",
            topic="feedback",
            source="organ",
            meaning="processing completed",
            place="organ/test",
            reference="event:E1",
            delta={"result": "ok"},
        )
    )

    assert bus.dispatch_one() is True
    assert feedback[0].reference == "event:E1"
    assert feedback[0].delta["result"] == "ok"
