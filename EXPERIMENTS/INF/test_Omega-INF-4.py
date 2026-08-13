"""Regression tests for Ω-INF-4."""

import importlib.util
from collections import Counter
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "omega_inf_4", HERE / "Omega-INF-4_local_relations_trigrams_preserved.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_length_and_character_multiset_are_preserved():
    for seed in range(MODULE.SEED, MODULE.SEED + 5):
        transformed = MODULE.reconstruct_preserving_trigrams(MODULE.TEXT, seed)
        assert len(transformed) == len(MODULE.TEXT)
        assert Counter(transformed) == Counter(MODULE.TEXT)


def test_bigram_and_trigram_multisets_are_preserved():
    original_bigrams = Counter(zip(MODULE.TEXT, MODULE.TEXT[1:]))
    original_trigrams = Counter(zip(MODULE.TEXT, MODULE.TEXT[1:], MODULE.TEXT[2:]))
    for seed in range(MODULE.SEED, MODULE.SEED + 5):
        transformed = MODULE.reconstruct_preserving_trigrams(MODULE.TEXT, seed)
        assert Counter(zip(transformed, transformed[1:])) == original_bigrams
        assert Counter(zip(transformed, transformed[1:], transformed[2:])) == original_trigrams


def test_first_and_second_order_entropy_are_invariant():
    original = MODULE.metrics(MODULE.TEXT)
    for seed in range(MODULE.SEED, MODULE.SEED + 5):
        transformed = MODULE.reconstruct_preserving_trigrams(MODULE.TEXT, seed)
        result = MODULE.metrics(transformed)
        assert result["conditional_entropy_order1_bits"] == original["conditional_entropy_order1_bits"]
        assert result["conditional_entropy_order2_bits"] == original["conditional_entropy_order2_bits"]


def test_compression_changes_for_fixed_protocol_sample():
    original = MODULE.metrics(MODULE.TEXT)["zlib_bytes"]
    values = [
        MODULE.metrics(MODULE.reconstruct_preserving_trigrams(MODULE.TEXT, MODULE.SEED + i))["zlib_bytes"]
        for i in range(10)
    ]
    assert any(value != original for value in values)


def test_run_is_deterministic():
    assert MODULE.run() == MODULE.run()
