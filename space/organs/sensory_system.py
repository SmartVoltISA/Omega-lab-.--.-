"""Sensory system: normalized boundary for external observations."""
from dataclasses import dataclass
from time import time
from typing import Any, Callable

@dataclass(frozen=True)
class Observation:
    observation_id: str
    modality: str
    source: str
    payload: Any
    timestamp: float
    reliability: float

class SensorySystem:
    def __init__(self) -> None:
        self._counter = 0
        self._adapters: dict[str, Callable[[], Any]] = {}

    def register(self, modality: str, reader: Callable[[], Any]) -> None:
        if modality in self._adapters:
            raise ValueError("duplicate sensory modality")
        self._adapters[modality] = reader

    def read(self, modality: str, source: str | None = None, reliability: float = 1.0) -> Observation:
        self._counter += 1
        value = self._adapters[modality]()
        return Observation(f"obs-{self._counter}", modality, source or modality, value, time(), max(0.0, min(1.0, reliability)))

    def modalities(self) -> list[str]:
        return list(self._adapters)
