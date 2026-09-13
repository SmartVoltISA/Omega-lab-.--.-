"""Regression tests for Ω-INF-7.

These tests check invariants and protocol integrity, not whether the
hypothesis is true.
"""
import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("omega_inf_7", HERE / "Omega-INF-7_robust_sampling.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_exact_sample_count():
    assert M.N_PER_CORPUS == 250
    assert len(M.SEEDS) == 4


def test_reconstruction_preserves_characters_and_trigrams():
    for text in M.CORPUS.values():
        out = M.reconstruct(text, M.SEEDS[0] * 100000)
        assert len(out) == len(text)
        assert Counter(out) == Counter(text)
        assert Counter(zip(out, out[1:], out[2:])) == Counter(zip(text, text[1:], text[2:]))


def test_all_corpora_are_nontrivial():
    for text in M.CORPUS.values():
        assert len(text) > 200
        assert len(set(text)) > 10


def test_seed_rotation_is_deterministic():
    for text in M.CORPUS.values():
        a = M.reconstruct(text, M.SEEDS[1] * 100000 + 17)
        b = M.reconstruct(text, M.SEEDS[1] * 100000 + 17)
        assert a == b
