"""Regression tests for Ω-INF-3."""

import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("omega_inf_3", HERE / "Omega-INF-3_local_relations_preserved.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_eulerian_reconstruction_preserves_bigram_multiset():
    reconstructed = MODULE.reconstruct_preserving_bigrams(MODULE.TEXT, MODULE.SEED)
    assert len(reconstructed) == len(MODULE.TEXT)
    assert Counter(reconstructed) == Counter(MODULE.TEXT)
    assert Counter(zip(reconstructed, reconstructed[1:])) == Counter(zip(MODULE.TEXT, MODULE.TEXT[1:]))


def test_local_metrics_are_invariant():
    reconstructed = MODULE.reconstruct_preserving_bigrams(MODULE.TEXT, MODULE.SEED)
    original = MODULE.metrics(MODULE.TEXT)
    result = MODULE.metrics(reconstructed)
    assert result["n_chars"] == original["n_chars"]
    assert result["symbol_entropy_bits"] == original["symbol_entropy_bits"]
    assert result["conditional_entropy_bits"] == original["conditional_entropy_bits"]
    assert result["unique_bigrams"] == original["unique_bigrams"]


def test_longer_range_compression_can_change():
    reconstructed = MODULE.reconstruct_preserving_bigrams(MODULE.TEXT, MODULE.SEED)
    original = MODULE.metrics(MODULE.TEXT)
    result = MODULE.metrics(reconstructed)
    assert result["zlib_bytes"] != original["zlib_bytes"]


def test_run_is_deterministic():
    assert MODULE.run() == MODULE.run()
