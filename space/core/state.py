from dataclasses import dataclass, field
from typing import Any

@dataclass
class SpaceState:
    space_id: str
    cycle: int = 0
    mode: str = "ACTIVE"
    values: dict[str, Any] = field(default_factory=dict)
    last_result: Any = None
    last_feedback: Any = None
    revision: int = 0

    def update(self, **changes: Any) -> None:
        self.values.update(changes)
        self.revision += 1

    def snapshot(self) -> dict[str, Any]:
        return {
            "space_id": self.space_id,
            "cycle": self.cycle,
            "mode": self.mode,
            "values": dict(self.values),
            "last_result": self.last_result,
            "last_feedback": self.last_feedback,
            "revision": self.revision,
        }
