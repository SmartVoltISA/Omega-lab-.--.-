"""Deterministic spectrum/formant candidate layer for Ω-Audio Organ v0.1."""
from dataclasses import dataclass
import math
from typing import Sequence


@dataclass(frozen=True)
class SpectralFeatures:
    dominant_hz: float | None
    spectral_centroid_hz: float | None
    f1_hz: float | None
    f2_hz: float | None
    f3_hz: float | None


def spectrum_features(samples: Sequence[float], sample_rate: int = 16000) -> SpectralFeatures:
    """Return deterministic spectral peaks using a direct DFT.

    This is intentionally small and inspectable; it is not a production ASR
    formant tracker. Peaks are candidates and must not be treated as phonemes.
    """
    n = len(samples)
    if n < 8 or sample_rate <= 0:
        return SpectralFeatures(None, None, None, None, None)
    x = [float(v) for v in samples]
    half = n // 2
    mags: list[tuple[float, float]] = []
    total_power = 0.0
    weighted = 0.0
    for k in range(1, half):
        re = 0.0
        im = 0.0
        for i, value in enumerate(x):
            angle = 2.0 * math.pi * k * i / n
            re += value * math.cos(angle)
            im -= value * math.sin(angle)
        power = re * re + im * im
        hz = k * sample_rate / n
        mags.append((hz, power))
        total_power += power
        weighted += hz * power
    if not mags or total_power <= 1e-12:
        return SpectralFeatures(None, None, None, None, None)
    centroid = weighted / total_power
    ranked = sorted(mags, key=lambda p: p[1], reverse=True)
    peaks: list[float] = []
    for hz, power in ranked:
        if power <= 0:
            continue
        if all(abs(hz - old) >= sample_rate / n * 2 for old in peaks):
            peaks.append(hz)
        if len(peaks) == 3:
            break
    peaks.sort()
    padded = peaks + [None] * (3 - len(peaks))
    return SpectralFeatures(ranked[0][0], centroid, padded[0], padded[1], padded[2])
