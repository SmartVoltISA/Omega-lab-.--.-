"""Deterministic Ω-Audio Organ v0.1.

No neural model is used. The organ converts sampled mono audio into a small,
inspectable acoustic feature record. It is intentionally a measurement layer;
phoneme/word decisions remain candidates until graph/context validation.
"""
from dataclasses import dataclass
import math
from typing import Sequence


@dataclass(frozen=True)
class AudioFeatures:
    duration_s: float
    rms: float
    peak: float
    zero_crossing_rate: float
    f0_hz: float | None
    voiced: bool


class AudioOrgan:
    def __init__(self, sample_rate: int = 16000) -> None:
        if sample_rate <= 0:
            raise ValueError("sample_rate must be positive")
        self.sample_rate = sample_rate

    def analyze(self, samples: Sequence[float]) -> AudioFeatures:
        n = len(samples)
        if n == 0:
            return AudioFeatures(0.0, 0.0, 0.0, 0.0, None, False)

        peak = max(abs(float(x)) for x in samples)
        rms = math.sqrt(sum(float(x) ** 2 for x in samples) / n)
        crossings = sum(
            1 for a, b in zip(samples, samples[1:])
            if (a < 0 <= b) or (a >= 0 > b)
        )
        zcr = crossings / max(1, n - 1)
        f0 = self._estimate_f0(samples)
        voiced = f0 is not None and rms > 1e-4
        return AudioFeatures(n / self.sample_rate, rms, peak, zcr, f0, voiced)

    def _estimate_f0(self, samples: Sequence[float]) -> float | None:
        # Deterministic autocorrelation search for speech-range periodicity.
        n = len(samples)
        if n < 32:
            return None
        lo = max(1, int(self.sample_rate / 450))
        hi = min(n // 2, int(self.sample_rate / 60))
        if lo >= hi:
            return None
        mean = sum(samples) / n
        x = [float(v) - mean for v in samples]
        energy = sum(v * v for v in x)
        if energy <= 1e-12:
            return None
        best_lag, best_score = None, 0.0
        for lag in range(lo, hi + 1):
            corr = sum(x[i] * x[i - lag] for i in range(lag, n))
            norm = math.sqrt(sum(x[i] * x[i] for i in range(lag, n)) * energy)
            score = corr / norm if norm else 0.0
            if score > best_score:
                best_lag, best_score = lag, score
        if best_lag is None or best_score < 0.55:
            return None
        return self.sample_rate / best_lag
