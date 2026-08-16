"""Append-only, hash-chained ledger for organism mutations.

The ledger records proposed, accepted, rejected, isolated and failed changes
coming from either outside->inside or inside->outside flows. It is deliberately
independent from trusted state: recording a change never authorizes it.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

Direction = Literal["EXTERNAL_TO_INTERNAL", "INTERNAL_TO_EXTERNAL"]
Disposition = Literal["PROPOSED", "ACCEPTED", "REJECTED", "ISOLATED", "FAILED"]


@dataclass(frozen=True)
class ChangeRecord:
    change_id: str
    timestamp: str
    direction: Direction
    actor: str
    target: str
    action: str
    before_hash: str | None
    after_hash: str | None
    guardian_decision: str
    disposition: Disposition
    reason: str
    previous_record_hash: str
    record_hash: str


class ChangeLedger:
    """Durable JSONL ledger with a SHA-256 hash chain.

    The ledger is intentionally append-only. A new record references the hash
    of the previous record, allowing later integrity verification without
    modifying the organism's trusted state.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _last_hash(self) -> str:
        if not self.path.exists():
            return "GENESIS"
        last = "GENESIS"
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    last = json.loads(line)["record_hash"]
        return last

    @staticmethod
    def _hash_payload(payload: dict[str, Any]) -> str:
        canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def record(
        self,
        *,
        change_id: str,
        direction: Direction,
        actor: str,
        target: str,
        action: str,
        before_hash: str | None,
        after_hash: str | None,
        guardian_decision: str,
        disposition: Disposition,
        reason: str,
    ) -> ChangeRecord:
        timestamp = datetime.now(timezone.utc).isoformat()
        previous = self._last_hash()
        base = {
            "change_id": change_id,
            "timestamp": timestamp,
            "direction": direction,
            "actor": actor,
            "target": target,
            "action": action,
            "before_hash": before_hash,
            "after_hash": after_hash,
            "guardian_decision": guardian_decision,
            "disposition": disposition,
            "reason": reason,
            "previous_record_hash": previous,
        }
        record_hash = self._hash_payload(base)
        record = ChangeRecord(record_hash=record_hash, **base)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(record), ensure_ascii=False, sort_keys=True) + "\n")
        return record

    def verify(self) -> bool:
        previous = "GENESIS"
        if not self.path.exists():
            return True
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                data = json.loads(line)
                if data["previous_record_hash"] != previous:
                    return False
                actual = data.pop("record_hash")
                if self._hash_payload(data) != actual:
                    return False
                previous = actual
        return True
