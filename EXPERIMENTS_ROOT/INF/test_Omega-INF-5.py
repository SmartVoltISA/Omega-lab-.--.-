"""Regression tests for Ω-INF-5 independent corpus replication."""
import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("omega_inf_5", HERE / "Omega-INF-5_independent_corpus_replication.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_corpus_is_independent_of_fixed_omega_text():
    assert len(M.CORPUS) == 4
    assert all(len(v) >= 200 for v in M.CORPUS.values())


def test_trigram_inventory_is_preserved_for_every_corpus_and_seed():
    for text in M.CORPUS.values():
        original = Counter(zip(text, text[1:], text[2:]))
        for i in range(10):
            transformed = M.reconstruct(text, M.SEED_START + i)
            assert len(transformed) == len(text)
            assert Counter(transformed) == Counter(text)
            assert Counter(zip(transformed, transformed[1:], transformed[2:])) == original


def test_reconstruction_is_not_forced_to_have_one_compression_direction():
    results = M.run()["results"]
    deltas = []
    for r in results.values():
        deltas.append(r["mean_zlib"] - r["original"]["zlib"])
    assert any(x < 0 for x in deltas)
    assert any(x > 0 for x in deltas)


def test_run_is_deterministic():
    assert M.run() == M.run()
