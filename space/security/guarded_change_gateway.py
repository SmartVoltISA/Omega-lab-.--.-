"""Single gateway for state-changing operations crossing the organism boundary.

The gateway makes the audit path explicit:
proposal -> Guardian decision -> ledger -> apply (only when allowed).
Recording never grants permission, and rejected changes never reach the
supplied apply callback.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Any

from change_ledger import ChangeLedger, Direction, Disposition
from guardian_core import Decision, GuardianCore, SecurityEvidence


@dataclass(frozen=True)
class ChangeOutcome:
    change_id: str
    decision: Decision
    disposition: Disposition
    applied: bool
    record_hash: str


class GuardedChangeGateway:
    def __init__(self, guardian: GuardianCore, ledger: ChangeLedger):
        self.guardian = guardian
        self.ledger = ledger

    def execute(
        self,
        *,
        change_id: str,
        evidence: SecurityEvidence,
        direction: Direction,
        actor: str,
        target: str,
        action: str,
        before_hash: str | None,
        after_hash: str | None,
        reason: str,
        apply: Callable[[], Any],
    ) -> ChangeOutcome:
        decision = self.guardian.decide(evidence)
        disposition: Disposition = (
            "ACCEPTED" if decision is Decision.ALLOW else "REJECTED"
        )

        if decision is Decision.ALLOW:
            try:
                apply()
            except Exception:
                disposition = "FAILED"
                record = self.ledger.record(
                    change_id=change_id,
                    direction=direction,
                    actor=actor,
                    target=target,
                    action=action,
                    before_hash=before_hash,
                    after_hash=after_hash,
                    guardian_decision=decision.value,
                    disposition=disposition,
                    reason=reason,
                )
                raise RuntimeError(
                    f"change {change_id} failed after Guardian ALLOW; ledger={record.record_hash}"
                )
        record = self.ledger.record(
            change_id=change_id,
            direction=direction,
            actor=actor,
            target=target,
            action=action,
            before_hash=before_hash,
            after_hash=after_hash,
            guardian_decision=decision.value,
            disposition=disposition,
            reason=reason,
        )
        return ChangeOutcome(
            change_id=change_id,
            decision=decision,
            disposition=disposition,
            applied=decision is Decision.ALLOW,
            record_hash=record.record_hash,
        )
