import tempfile
import unittest
from pathlib import Path

from change_ledger import ChangeLedger
from guarded_change_gateway import GuardedChangeGateway
from guardian_core import Decision, GuardianCore, SecurityEvidence


class GuardedChangeGatewayTests(unittest.TestCase):
    def evidence(self, **overrides):
        data = dict(
            space_id="space-test",
            device_key_id="device-test",
            key_attested=True,
            integrity_ok=True,
            request_fresh=True,
        )
        data.update(overrides)
        return SecurityEvidence(**data)

    def test_allowed_change_is_applied_and_recorded(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = ChangeLedger(Path(tmp) / "changes.jsonl")
            gateway = GuardedChangeGateway(GuardianCore(), ledger)
            applied = []
            outcome = gateway.execute(
                change_id="c-allow",
                evidence=self.evidence(),
                direction="INTERNAL_TO_EXTERNAL",
                actor="test",
                target="organism.output",
                action="publish",
                before_hash="before",
                after_hash="after",
                reason="valid test change",
                apply=lambda: applied.append(True),
            )
            self.assertEqual(outcome.decision, Decision.ALLOW)
            self.assertTrue(outcome.applied)
            self.assertEqual(applied, [True])
            self.assertTrue(ledger.verify())

    def test_blocked_change_never_reaches_apply(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = ChangeLedger(Path(tmp) / "changes.jsonl")
            gateway = GuardedChangeGateway(GuardianCore(), ledger)
            applied = []
            outcome = gateway.execute(
                change_id="c-block",
                evidence=self.evidence(revoked=True),
                direction="EXTERNAL_TO_INTERNAL",
                actor="test",
                target="organism.state",
                action="mutate",
                before_hash="before",
                after_hash="after",
                reason="revoked source",
                apply=lambda: applied.append(True),
            )
            self.assertEqual(outcome.decision, Decision.BLOCK)
            self.assertFalse(outcome.applied)
            self.assertEqual(applied, [])
            self.assertTrue(ledger.verify())

    def test_ledger_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changes.jsonl"
            ledger = ChangeLedger(path)
            ledger.record(
                change_id="c-1",
                direction="EXTERNAL_TO_INTERNAL",
                actor="test",
                target="organism.state",
                action="observe",
                before_hash=None,
                after_hash="h1",
                guardian_decision="RESTRICT",
                disposition="REJECTED",
                reason="test",
            )
            self.assertTrue(ledger.verify())
            text = path.read_text(encoding="utf-8").replace('"reason": "test"', '"reason": "tampered"')
            path.write_text(text, encoding="utf-8")
            self.assertFalse(ChangeLedger(path).verify())


if __name__ == "__main__":
    unittest.main()
