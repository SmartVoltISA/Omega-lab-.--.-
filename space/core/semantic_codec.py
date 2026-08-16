"""Minimal semantic codec for SPACE Language v1.1.

The codec deliberately preserves relations, provenance, uncertainty and
quantity/cardinality. It is a semantic envelope, not an execution engine.
"""
from dataclasses import dataclass, field
from typing import Any


ALLOWED_KINDS = {
    "fact",
    "measurement",
    "inference",
    "hypothesis",
    "request",
    "recommendation",
    "decision",
    "execution_result",
}


@dataclass(frozen=True)
class Relation:
    source: str
    relation_type: str
    target: str
    direction: str = "forward"
    strength: float | None = None
    scope: str | None = None
    place: str | None = None


@dataclass(frozen=True)
class Quantity:
    value: float | int | None = None
    unit: str | None = None
    count: int | None = None
    minimum: float | int | None = None
    maximum: float | int | None = None
    precision: float | None = None
    rate: float | None = None
    duration: float | None = None
    frequency: float | None = None


@dataclass(frozen=True)
class SemanticMessage:
    message_id: str
    kind: str
    meaning: str
    relations: tuple[Relation, ...] = ()
    quantities: tuple[Quantity, ...] = ()
    source: str | None = None
    provenance: tuple[str, ...] = ()
    confidence: float | None = None
    uncertainty: float | None = None
    freshness: float | None = None
    importance: float | None = None
    place: str | None = None
    context: str | None = None
    reference: str | None = None
    delta: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if self.kind not in ALLOWED_KINDS:
            raise ValueError(f"unknown semantic kind: {self.kind}")
        if not self.message_id or not self.meaning:
            raise ValueError("message_id and meaning are required")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        if self.uncertainty is not None and not 0 <= self.uncertainty <= 1:
            raise ValueError("uncertainty must be between 0 and 1")
        for quantity in self.quantities:
            if quantity.count is not None and quantity.count < 0:
                raise ValueError("count cannot be negative")


def encode(message: SemanticMessage) -> dict[str, Any]:
    """Return a compact, loss-aware semantic representation."""
    message.validate()
    return {
        "id": message.message_id,
        "kind": message.kind,
        "meaning": message.meaning,
        "relations": [r.__dict__ for r in message.relations],
        "quantities": [q.__dict__ for q in message.quantities],
        "source": message.source,
        "provenance": list(message.provenance),
        "confidence": message.confidence,
        "uncertainty": message.uncertainty,
        "freshness": message.freshness,
        "importance": message.importance,
        "place": message.place,
        "context": message.context,
        "reference": message.reference,
        "delta": message.delta,
    }


def decode(payload: dict[str, Any]) -> SemanticMessage:
    """Reconstruct a semantic message without granting execution authority."""
    relations = tuple(Relation(**item) for item in payload.get("relations", []))
    quantities = tuple(
        Quantity(
            value=item.get("value"),
            unit=item.get("unit"),
            count=item.get("count"),
            minimum=item.get("minimum"),
            maximum=item.get("maximum"),
            precision=item.get("precision"),
            rate=item.get("rate"),
            duration=item.get("duration"),
            frequency=item.get("frequency"),
        )
        for item in payload.get("quantities", [])
    )
    message = SemanticMessage(
        message_id=payload["id"],
        kind=payload["kind"],
        meaning=payload["meaning"],
        relations=relations,
        quantities=quantities,
        source=payload.get("source"),
        provenance=tuple(payload.get("provenance", [])),
        confidence=payload.get("confidence"),
        uncertainty=payload.get("uncertainty"),
        freshness=payload.get("freshness"),
        importance=payload.get("importance"),
        place=payload.get("place"),
        context=payload.get("context"),
        reference=payload.get("reference"),
        delta=payload.get("delta", {}),
    )
    message.validate()
    return message
