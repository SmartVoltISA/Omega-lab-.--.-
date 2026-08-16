from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class RecoveryDecision:
    mode: str
    reason: str
    preserved_state: bool

class RecoveryManager:
    def recover(self, reason: str, state: dict[str, Any]) -> RecoveryDecision:
        preserved = bool(state)
        return RecoveryDecision("RECOVERY", reason, preserved)
