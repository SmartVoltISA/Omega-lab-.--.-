"""Wellbeing signals, not mind-reading.

SPACE may aggregate observable/self-reported signals and report trends with
provenance and confidence. It must not present inferred mental states as facts.
"""
from dataclasses import dataclass, asdict
from time import time
from typing import Any

@dataclass(frozen=True)
class WellbeingSignal:
    subject: str
    signal: str
    value: Any
    source: str
    confidence: float
    observed_at: float
    consent_scope: str

class WellbeingMonitor:
    def __init__(self) -> None:
        self.signals: list[WellbeingSignal] = []

    def record(self, subject: str, signal: str, value: Any, source: str,
               confidence: float, consent_scope: str) -> WellbeingSignal:
        if not 0 <= confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        item = WellbeingSignal(subject, signal, value, source, confidence, time(), consent_scope)
        self.signals.append(item)
        return item

    def report(self, subject: str) -> list[dict[str, Any]]:
        return [asdict(s) for s in self.signals if s.subject == subject]
