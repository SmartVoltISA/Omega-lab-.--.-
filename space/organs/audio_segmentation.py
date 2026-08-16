"""Deterministic temporal segmentation for Ω-Audio Organ.

This is a candidate boundary detector, not a phoneme recognizer. It uses
frame energy and voicing transitions to expose likely speech segments while
preserving uncertainty for later graph/context validation.
"""
from dataclasses import dataclass
from typing import Sequence
import math


@dataclass(frozen=True)
class AudioSegment:
    start_s: float
    end_s: float
    voiced: bool
    mean_energy: float


class AudioSegmenter:
    def __init__(self, sample_rate: int = 16000, frame_ms: float = 20.0, hop_ms: float = 10.0, threshold: float = 1e-4) -> None:
        if sample_rate <= 0 or frame_ms <= 0 or hop_ms <= 0:
            raise ValueError("invalid audio segmentation parameters")
        self.sample_rate = sample_rate
        self.frame = max(1, int(sample_rate * frame_ms / 1000.0))
        self.hop = max(1, int(sample_rate * hop_ms / 1000.0))
        self.threshold = threshold

    def segment(self, samples: Sequence[float]) -> list[AudioSegment]:
        if not samples:
            return []
        frames: list[tuple[float, float, bool]] = []
        for start in range(0, max(1, len(samples) - self.frame + 1), self.hop):
            block = [float(x) for x in samples[start:start + self.frame]]
            if not block:
                continue
            energy = sum(x * x for x in block) / len(block)
            rms = math.sqrt(energy)
            crossings = sum(1 for a, b in zip(block, block[1:]) if (a < 0 <= b) or (a >= 0 > b))
            zcr = crossings / max(1, len(block) - 1)
            voiced = rms >= self.threshold and zcr < 0.35
            frames.append((start / self.sample_rate, min(len(samples), start + len(block)) / self.sample_rate, voiced))
        if not frames:
            return []
        segments: list[AudioSegment] = []
        cur_start, cur_end, cur_voiced = frames[0]
        energies: list[float] = []
        for start, end, voiced in frames:
            block = samples[int(start * self.sample_rate):int(end * self.sample_rate)]
            energy = sum(float(x) ** 2 for x in block) / max(1, len(block))
            if voiced != cur_voiced and start > cur_start:
                segments.append(AudioSegment(cur_start, cur_end, cur_voiced, sum(energies) / max(1, len(energies))))
                cur_start = start
                energies = []
                cur_voiced = voiced
            cur_end = end
            energies.append(energy)
        segments.append(AudioSegment(cur_start, cur_end, cur_voiced, sum(energies) / max(1, len(energies))))
        return segments
