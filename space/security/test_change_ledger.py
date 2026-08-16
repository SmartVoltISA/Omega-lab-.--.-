from pathlib import Path

from .change_ledger import ChangeLedger


def test_bidirectional_records_are_persistent_and_verifiable(tmp_path: Path):
    ledger = ChangeLedger(tmp_path / "changes.jsonl")

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

    assert ledger.verify()
    assert ledger.path.read_text(encoding="utf-8").count("\n") == 2


def test_tampering_breaks_chain(tmp_path: Path):
    ledger = ChangeLedger(tmp_path / "changes.jsonl")
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

    raw = ledger.path.read_text(encoding="utf-8")
    ledger.path.write_text(raw.replace('"reason": "test"', '"reason": "tampered"'), encoding="utf-8")
    assert not ledger.verify()
