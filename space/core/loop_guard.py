from dataclasses import dataclass
import hashlib
import json

@dataclass(frozen=True)
class GuardDecision:
    action: str
    reason: str
    repetitions: int

class LoopGuard:
    def __init__(self, threshold: int = 3) -> None:
        self.threshold = threshold
        self._last = None
        self._repetitions = 0

    @staticmethod
    def fingerprint(state, action, result) -> str:
        raw = json.dumps({"state": state, "action": action, "result": result}, sort_keys=True, default=str)
        return hashlib.sha256(raw.encode()).hexdigest()

    def observe(self, state, action, result, evidence_delta: bool = False, strategy_delta: bool = False) -> GuardDecision:
        fp = self.fingerprint(state, action, result)
        if fp == self._last and not evidence_delta and not strategy_delta:
            self._repetitions += 1
        else:
            self._repetitions = 0
        self._last = fp
        if self._repetitions >= self.threshold:
            return GuardDecision("STOP_REPLAN", "repeated cycle without progress", self._repetitions)
        return GuardDecision("CONTINUE", "productive or initial cycle", self._repetitions)

    def reset(self) -> None:
        self._last = None
        self._repetitions = 0
