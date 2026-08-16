"""Immune boundary: detects abnormal conditions and can quarantine a component."""
from dataclasses import dataclass
from time import time
from typing import Any, Callable

@dataclass(frozen=True)
class Anomaly:
    anomaly_id: str
    source: str
    severity: str
    reason: str
    timestamp: float
    evidence: Any

class ImmuneSystem:
    def __init__(self) -> None:
        self._counter = 0
        self._quarantined: set[str] = set()
        self._rules: list[Callable[[str, Any], str | None]] = []
        self._history: list[Anomaly] = []

    def add_rule(self, rule: Callable[[str, Any], str | None]) -> None:
        self._rules.append(rule)

    def inspect(self, source: str, evidence: Any) -> list[Anomaly]:
        findings = []
        for rule in self._rules:
            severity = rule(source, evidence)
            if severity:
                self._counter += 1
                anomaly = Anomaly(f"anom-{self._counter}", source, severity, "rule_match", time(), evidence)
                self._history.append(anomaly)
                findings.append(anomaly)
        return findings

    def quarantine(self, source: str) -> None:
        self._quarantined.add(source)

    def is_quarantined(self, source: str) -> bool:
        return source in self._quarantined

    def history(self) -> list[Anomaly]:
        return list(self._history)
