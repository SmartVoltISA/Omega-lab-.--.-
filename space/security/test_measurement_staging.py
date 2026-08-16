from pathlib import Path

from .measurement_staging import MeasurementStaging


def test_staging_is_readable_without_trusted_memory(tmp_path: Path):
    staging = MeasurementStaging(tmp_path / "quarantine")
    record = staging.stage("m1", "test", {"value": 42})

    assert record.status == "STAGED"
    assert staging.list_staged()[0] == record
    assert (tmp_path / "quarantine" / "m1.json").exists()


def test_staging_hash_is_deterministic(tmp_path: Path):
    staging = MeasurementStaging(tmp_path / "quarantine")
    assert staging.payload_hash({"b": 2, "a": 1}) == staging.payload_hash({"a": 1, "b": 2})
