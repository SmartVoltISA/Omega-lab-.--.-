"""Deterministic phonetic candidate layer for Ω-Audio Organ v0.2.

This layer never asserts a phoneme as fact. It converts measured acoustic
features into ranked candidates using explicit ranges and keeps ambiguity
visible for later graph/context validation.
"""
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class PhonemeCandidate:
    symbol: str
    score: float
    reason: str


# Deliberately small seed inventory: vowels only. Values are broad and are
# candidates, not speaker-independent truth.
_VOWELS = {
    "a": (700.0, 1100.0),
    "i": (220.0, 2800.0),
    "u": (300.0, 850.0),
    "o": (570.0, 850.0),
    "e": (530.0, 1850.0),
}


def vowel_candidates(f1: float, f2: float) -> Sequence[PhonemeCandidate]:
    """Return ranked vowel hypotheses from F1/F2 proximity.

    The score is intentionally simple and deterministic. Missing calibration,
    speaker normalization and temporal context are left for later layers.
    """
    if f1 <= 0 or f2 <= 0:
        return ()
    ranked = []
    for symbol, (target_f1, target_f2) in _VOWELS.items():
        # Broad target bands are used as anchors; uncertainty remains explicit.
        d1 = abs(f1 - target_f1) / max(target_f1, 1.0)
        d2 = abs(f2 - target_f2) / max(target_f2, 1.0)
        score = 1.0 / (1.0 + d1 + d2)
        ranked.append(PhonemeCandidate(symbol, score, "F1/F2 proximity"))
    return tuple(sorted(ranked, key=lambda c: c.score, reverse=True))
