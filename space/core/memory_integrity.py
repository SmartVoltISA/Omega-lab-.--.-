"""Tamper-evident integrity layer for structural memory.

This layer does not encrypt memory and is not a substitute for secure storage.
It preserves a deterministic hash chain so accidental or unauthorized mutation
can be detected and historical continuity can be checked after migration or
recovery.
"""
from dataclasses import dataclass
import hashlib
import json
from typing import Any

@dataclass(frozen=True)
class IntegrityRecord:
    sequence: int
    trace_id: str
    digest: str
    previous_digest: str

class MemoryIntegrity:
    def __init__(self) -> None:
        self._records: list[IntegrityRecord] = []

    @staticmethod
    def _digest(payload: dict[str, Any], previous_digest: str) -> str:
        raw = json.dumps({"payload": payload, "previous": previous_digest}, sort_keys=True, default=str, separators=(",", ":"))
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def append(self, trace_id: str, payload: dict[str, Any]) -> IntegrityRecord:
        previous = self._records[-1].digest if self._records else "GENESIS"
        digest = self._digest(payload, previous)
        record = IntegrityRecord(len(self._records) + 1, trace_id, digest, previous)
        self._records.append(record)
        return record

    def verify(self, payloads: list[dict[str, Any]]) -> bool:
        if len(payloads) != len(self._records):
            return False
        previous = "GENESIS"
        for record, payload in zip(self._records, payloads):
            if record.previous_digest != previous:
                return False
            if self._digest(payload, previous) != record.digest:
                return False
            previous = record.digest
        return True

    def snapshot(self) -> list[dict[str, Any]]:
        return [r.__dict__ for r in self._records]

    def latest_digest(self) -> str:
        return self._records[-1].digest if self._records else "GENESIS"
