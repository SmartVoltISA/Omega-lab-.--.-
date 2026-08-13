"""Regression and invariance tests for Ω-INF-2."""

import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("omega_inf_2", HERE / "Omega-INF-2_hierarchical_scrambling.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_all_conditions_preserve_character_multiset_and_length():
    base = Counter(MODULE.TEXT)
    rng = __import__("random").Random(MODULE.SEED)
    transforms = [
        MODULE.condition_t1(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32))),
        MODULE.condition_t2(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32))),
        MODULE.condition_t3(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32))),
        MODULE.condition_t4(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32))),
    ]
    for transformed in transforms:
        assert len(transformed) == len(MODULE.TEXT)
        assert Counter(transformed) == base


def test_symbol_entropy_is_invariant():
    base = MODULE.entropy(MODULE.TEXT)
    rng = __import__("random").Random(MODULE.SEED)
    for transform in (
        MODULE.condition_t1,
        MODULE.condition_t2,
        MODULE.condition_t3,
        MODULE.condition_t4,
    ):
        transformed = transform(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32)))
        assert base == MODULE.entropy(transformed)


def test_t1_changes_low_level_relational_metrics():
    rng = __import__("random").Random(MODULE.SEED)
    transformed = MODULE.condition_t1(MODULE.TEXT, __import__("random").Random(rng.randrange(2**32)))
    original = MODULE.metrics(MODULE.TEXT)
    shuffled = MODULE.metrics(transformed)
    assert shuffled["conditional_entropy_bits"] > original["conditional_entropy_bits"]
    assert shuffled["unique_bigrams"] > original["unique_bigrams"]
    assert shuffled["zlib_bytes"] > original["zlib_bytes"]


def test_run_is_deterministic():
    a = MODULE.run()
    b = MODULE.run()
    assert a == b
    assert a["seed"] == 20260813
    assert a["text_length_chars"] == 855
