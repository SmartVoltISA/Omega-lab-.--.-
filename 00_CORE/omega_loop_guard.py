"""Ω-LOOP-GUARD v1.0

Small dependency-free guard for detecting unproductive semantic repetition.
It intentionally separates wording changes from real progress: a cycle only
counts as productive when evidence or strategy changes, or the state changes
materially.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Optional


def _fingerprint(value: str) -> str:
    return sha256(value.strip().lower().encode("utf-8")).hexdigest()


def _similarity(a: str, b: str) -> float:
    """Token Jaccard similarity; deliberately simple and deterministic."""
    aa = set(a.lower().split())
    bb = set(b.lower().split())
    if not aa and not bb:
        return 1.0
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


@dataclass(frozen=True)
class LoopDecision:
    action: str
    level: int
    repeated_cycles: int
    reason: str


class OmegaLoopGuard:
    """Detect repeated work without evidence/strategy progress."""

    def __init__(
        self,
        max_repetitions: int = 3,
        state_threshold: float = 0.90,
        action_threshold: float = 0.90,
        output_threshold: float = 0.90,
    ) -> None:
        if max_repetitions < 1:
            raise ValueError("max_repetitions must be >= 1")
        self.max_repetitions = max_repetitions
        self.state_threshold = state_threshold
        self.action_threshold = action_threshold
        self.output_threshold = output_threshold
        self._last: Optional[dict] = None
        self._repetitions = 0

    @property
    def repetitions(self) -> int:
        return self._repetitions

    def observe(
        self,
        *,
        state: str,
        action: str,
        output: str,
        evidence_delta: bool = False,
        strategy_delta: bool = False,
    ) -> LoopDecision:
        current = {
            "state": state,
            "action": action,
            "output": output,
            "state_fp": _fingerprint(state),
            "action_fp": _fingerprint(action),
        }

        if self._last is None:
            self._last = current
            self._repetitions = 0
            return LoopDecision("CONTINUE", 0, 0, "first observation")

        state_sim = _similarity(self._last["state"], state)
        action_sim = _similarity(self._last["action"], action)
        output_sim = _similarity(self._last["output"], output)
        repeated = (
            state_sim >= self.state_threshold
            and action_sim >= self.action_threshold
            and output_sim >= self.output_threshold
        )

        if evidence_delta or strategy_delta or not repeated:
            self._repetitions = 0
            self._last = current
            return LoopDecision(
                "CONTINUE", 0, 0,
                "productive change detected (state/evidence/strategy/output)"
            )

        self._repetitions += 1
        if self._repetitions >= self.max_repetitions:
            # Hard stop: do not silently continue the same action.
            self._repetitions = 0
            self._last = None
            return LoopDecision(
                "STOP_REPLAN", 2, self.max_repetitions,
                "repeated state/action/output with zero evidence and strategy delta"
            )

        self._last = current
        return LoopDecision(
            "WARN", 1, self._repetitions,
            "repetition detected without measurable progress"
        )

    def reset(self) -> None:
        self._last = None
        self._repetitions = 0
