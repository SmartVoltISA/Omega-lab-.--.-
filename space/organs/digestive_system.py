"""Digestive system: prepares and digests complex information through an LLM boundary.

The core remains provider-agnostic. An LLM is treated as a processing organ,
not as the authority or security boundary.
"""
from dataclasses import dataclass
from typing import Any, Protocol

class LLMBackend(Protocol):
    def generate(self, prompt: str, context: list[dict[str, Any]]) -> Any: ...

@dataclass(frozen=True)
class Digest:
    input_id: str
    interpretation: Any
    backend: str
    accepted: bool

class DigestiveSystem:
    def __init__(self, backend: LLMBackend | None = None, backend_name: str = "none") -> None:
        self.backend = backend
        self.backend_name = backend_name
        self._counter = 0

    def digest(self, input_id: str, prompt: str, context: list[dict[str, Any]]) -> Digest:
        self._counter += 1
        if self.backend is None:
            return Digest(input_id, {"status": "NO_LLM_BACKEND", "prompt": prompt}, self.backend_name, False)
        result = self.backend.generate(prompt, context)
        return Digest(input_id, result, self.backend_name, True)
