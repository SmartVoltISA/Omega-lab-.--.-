"""Causal local memory for an autonomous Ω-Space organ.

The record is deliberately local to the organ. It captures event -> action ->
result -> evaluation so later behavior can be informed by consequences without
creating a global graph or shared memory implicitly.
"""
from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class CausalRecord:
    record_id: str
    event: str
    action: str
    result: Any
    evaluation: str


class CausalMemory:
    def __init__(self) -> None:
        self._records: list[CausalRecord] = []

    def record(self, event: str, action: str, result: Any, evaluation: str) -> CausalRecord:
        if not event or not action or not evaluation:
            raise ValueError("event, action and evaluation are required")
        item = CausalRecord(
            record_id=f"cause-{len(self._records) + 1}",
            event=event,
            action=action,
            result=result,
            evaluation=evaluation,
        )
        self._records.append(item)
        return item

    @property
    def records(self) -> tuple[CausalRecord, ...]:
        return tuple(self._records)

    def snapshot(self) -> list[dict[str, Any]]:
        return [asdict(record) for record in self._records]

    def last(self) -> CausalRecord | None:
        return self._records[-1] if self._records else None
