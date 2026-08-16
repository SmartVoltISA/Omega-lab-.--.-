"""Dynamic trust ledger.

Provenance and trust are deliberately independent. Lineage explains where a
SPACE came from; evidence determines how much trust it currently receives.
Trust changes are append-only events and can be reviewed by Guardian.
"""
from dataclasses import dataclass, asdict
from time import time
from typing import Any

@dataclass(frozen=True)
class TrustEvent:
    event_id: str
    subject: str
    previous: float
    current: float
    reason: str
    evidence: Any
    created_at: float

class TrustLedger:
    def __init__(self, default: float = 0.0) -> None:
        if not 0.0 <= default <= 1.0:
            raise ValueError("trust must be in [0, 1]")
        self.default = default
        self._scores: dict[str, float] = {}
        self._history: list[TrustEvent] = []

    def score(self, subject: str) -> float:
        return self._scores.get(subject, self.default)

    def set_initial(self, subject: str, score: float, reason: str, evidence: Any = None) -> TrustEvent:
        """Set a first explicit trust value without bypassing the audit trail."""
        if subject in self._scores:
            raise ValueError("initial trust already set")
        return self.update(subject, score, reason, evidence)

    def update(self, subject: str, score: float, reason: str, evidence: Any = None) -> TrustEvent:
        if not 0.0 <= score <= 1.0:
            raise ValueError("trust must be in [0, 1]")
        previous = self.score(subject)
        event = TrustEvent(f"trust-{len(self._history) + 1}", subject, previous, score, reason, evidence, time())
        self._history.append(event)
        self._scores[subject] = score
        return event

    def adjust(self, subject: str, delta: float, reason: str, evidence: Any = None) -> TrustEvent:
        return self.update(subject, max(0.0, min(1.0, self.score(subject) + delta)), reason, evidence)

    def history(self, subject: str | None = None) -> list[dict[str, Any]]:
        events = [e for e in self._history if subject is None or e.subject == subject]
        return [asdict(e) for e in events]

    def snapshot(self) -> dict[str, float]:
        return dict(self._scores)
