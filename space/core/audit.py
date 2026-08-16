from dataclasses import dataclass, asdict
from time import time
from typing import Any

@dataclass(frozen=True)
class AuditRecord:
    record_id: str
    cycle: int
    operation: str
    decision: str
    source: str
    payload: Any
    created_at: float

class AuditLog:
    def __init__(self) -> None:
        self._records: list[AuditRecord] = []

    def record(self, cycle: int, operation: str, decision: str, source: str, payload: Any) -> AuditRecord:
        record = AuditRecord(f"audit-{len(self._records) + 1}", cycle, operation, decision, source, payload, time())
        self._records.append(record)
        return record

    def snapshot(self) -> list[dict[str, Any]]:
        return [asdict(r) for r in self._records]
