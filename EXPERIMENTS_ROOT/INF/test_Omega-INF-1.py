"""Regression tests for Ω-INF-1."""

import importlib.util
import random
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("omega_inf_1", HERE / "Omega-INF-1_character_order.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def deterministic_shuffle(seq, seed=314159):
    chars = list(seq)
    random.Random(seed).shuffle(chars)
    return chars


def test_shuffle_preserves_composition():
    chars = list(MODULE.TEXT)
    shuffled = deterministic_shuffle(chars)
    assert Counter(chars) == Counter(shuffled)
    assert len(chars) == len(shuffled)


def test_symbol_entropy_is_invariant_under_permutation():
    original = MODULE.entropy(MODULE.TEXT)
    shuffled = MODULE.entropy(deterministic_shuffle(MODULE.TEXT))
    assert original == shuffled


def test_relational_metrics_can_change_without_composition_change():
    original = MODULE.metrics(MODULE.TEXT)
    shuffled = MODULE.metrics(deterministic_shuffle(MODULE.TEXT))
    assert original["symbol_entropy_bits"] == shuffled["symbol_entropy_bits"]
    assert original["unique_bigrams"] != shuffled["unique_bigrams"]


def test_deterministic_seed_and_count():
    a = MODULE.run()
    b = MODULE.run()
    assert a == b
    assert a["seed"] == 20260813
    assert a["n_shuffles"] == 100
