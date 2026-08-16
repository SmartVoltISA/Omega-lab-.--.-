from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Plan:
    tool_id: str
    inputs: dict[str, Any]
    reason: str

class Planner:
    """Deterministic planner boundary; model-based planning can plug in later."""
    def choose(self, tool_id: str, inputs: dict[str, Any], reason: str = "explicit request") -> Plan:
        return Plan(tool_id, dict(inputs), reason)
