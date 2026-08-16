"""Non-trusted staging area for measurements and CI/test results.

Staged data remains inspectable without becoming trusted memory. Promotion is
explicit and requires an independent Guardian decision at a later step.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class StagedMeasurement:
    measurement_id: str
    source: str
    payload_hash: str
    status: str = "STAGED"


class MeasurementStaging:
    """Append-only staging store; it never writes to trusted memory."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.index = self.root / "index.jsonl"

    @staticmethod
    def payload_hash(payload: Any) -> str:
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def stage(self, measurement_id: str, source: str, payload: Any) -> StagedMeasurement:
        record = StagedMeasurement(measurement_id, source, self.payload_hash(payload))
        with self.index.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record), ensure_ascii=False, sort_keys=True) + "\n")
        (self.root / f"{measurement_id}.json").write_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2, default=str),
            encoding="utf-8",
        )
        return record

    def list_staged(self) -> list[StagedMeasurement]:
        if not self.index.exists():
            return []
        return [StagedMeasurement(**json.loads(line)) for line in self.index.read_text(encoding="utf-8").splitlines() if line.strip()]
