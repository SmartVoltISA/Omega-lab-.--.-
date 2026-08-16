import tempfile
import unittest
from pathlib import Path

from change_ledger import ChangeLedger


class ChangeLedgerTests(unittest.TestCase):
    def test_bidirectional_records_are_persistent_and_verifiable(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = ChangeLedger(Path(tmp) / "changes.jsonl")
            ledger.record(
                change_id="c-external-1",
                direction="EXTERNAL_TO_INTERNAL",
                actor="quarantine",
                target="memory",
                action="propose_update",
                before_hash="before",
                after_hash="after",
                guardian_decision="ACCEPT",
                disposition="ACCEPTED",
                reason="validated measurement",
            )
            ledger.record(
                change_id="c-internal-1",
                direction="INTERNAL_TO_EXTERNAL",
                actor="space",
                target="tool",
                action="request_output",
                before_hash="before2",
                after_hash=None,
                guardian_decision="DENY",
                disposition="REJECTED",
                reason="external output not authorized",
            )
            self.assertTrue(ledger.verify())
            self.assertEqual(ledger.path.read_text(encoding="utf-8").count("\n"), 2)

    def test_tampering_breaks_chain(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changes.jsonl"
            ledger = ChangeLedger(path)
            ledger.record(
                change_id="c1",
                direction="EXTERNAL_TO_INTERNAL",
                actor="test",
                target="node",
                action="mutate",
                before_hash=None,
                after_hash="h",
                guardian_decision="DENY",
                disposition="REJECTED",
                reason="test",
            )
            raw = path.read_text(encoding="utf-8")
            path.write_text(raw.replace('"reason": "test"', '"reason": "tampered"'), encoding="utf-8")
            self.assertFalse(ChangeLedger(path).verify())

    def test_two_records_are_linked(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = ChangeLedger(Path(tmp) / "changes.jsonl")
            first = ledger.record(
                change_id="one", direction="EXTERNAL_TO_INTERNAL", actor="t",
                target="node", action="observe", before_hash=None, after_hash="a",
                guardian_decision="RESTRICT", disposition="REJECTED", reason="test",
            )
            second = ledger.record(
                change_id="two", direction="INTERNAL_TO_EXTERNAL", actor="t",
                target="node", action="publish", before_hash="a", after_hash="b",
                guardian_decision="ALLOW", disposition="ACCEPTED", reason="test",
            )
            self.assertEqual(second.previous_record_hash, first.record_hash)
            self.assertTrue(ledger.verify())


if __name__ == "__main__":
    unittest.main()
