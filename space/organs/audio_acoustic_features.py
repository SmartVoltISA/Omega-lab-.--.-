"""Deterministic acoustic feature layer for Ω-Audio Organ v0.1.

No neural model is used here. The layer exposes auditable measurements that
can later become nodes/relations in the Ω representation.
"""
from dataclasses import dataclass
import math
from typing import Sequence


@dataclass(frozen=True)
class AcousticFeatures:
    sample_rate_hz: float
    duration_s: float
    rms: float
    peak: float
    zero_crossing_rate: float
    f0_hz: float | None
    voiced: bool


def _rms(samples: Sequence[float]) -> float:
    if not samples:
        return 0.0
    return math.sqrt(sum(x * x for x in samples) / len(samples))


def _zero_crossing_rate(samples: Sequence[float]) -> float:
    if len(samples) < 2:
        return 0.0
    crossings = sum(
        1 for a, b in zip(samples, samples[1:]) if (a < 0 <= b) or (a >= 0 > b)
    )
    return crossings / (len(samples) - 1)


def estimate_f0(samples: Sequence[float], sample_rate_hz: float, min_hz: float = 60.0,
                max_hz: float = 500.0) -> float | None:
    """Estimate F0 from the strongest normalized autocorrelation peak."""
    if not samples or sample_rate_hz <= 0:
        return None
    energy = sum(x * x for x in samples)
    if energy <= 1e-12:
        return None
    lo = max(1, int(sample_rate_hz / max_hz))
    hi = min(len(samples) - 1, int(sample_rate_hz / min_hz))
    if lo > hi:
        return None
    best_lag = None
    best_score = 0.0
    for lag in range(lo, hi + 1):
        numerator = sum(samples[i] * samples[i + lag] for i in range(len(samples) - lag))
        denom_a = sum(x * x for x in samples[:-lag])
        denom_b = sum(x * x for x in samples[lag:])
        if denom_a <= 1e-12 or denom_b <= 1e-12:
            continue
        score = numerator / math.sqrt(denom_a * denom_b)
        if score > best_score:
            best_score = score
            best_lag = lag
    if best_lag is None or best_score < 0.30:
        return None
    return sample_rate_hz / best_lag


def analyze(samples: Sequence[float], sample_rate_hz: float) -> AcousticFeatures:
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive")
    if not samples:
        return AcousticFeatures(sample_rate_hz, 0.0, 0.0, 0.0, 0.0, None, False)
    peak = max(abs(x) for x in samples)
    f0 = estimate_f0(samples, sample_rate_hz)
    return AcousticFeatures(
        sample_rate_hz=sample_rate_hz,
        duration_s=len(samples) / sample_rate_hz,
        rms=_rms(samples),
        peak=peak,
        zero_crossing_rate=_zero_crossing_rate(samples),
        f0_hz=f0,
        voiced=f0 is not None,
    )
