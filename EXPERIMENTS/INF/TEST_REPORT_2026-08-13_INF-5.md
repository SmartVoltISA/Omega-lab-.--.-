# Ω-INF-5 — Test Report

**Date:** 2026-08-13
**Runs:** 100 per corpus
**Corpora:** technical, literary, random-like, structured

## Checks

1. Every reconstruction preserved sequence length.
2. Every reconstruction preserved the exact character multiset.
3. Every reconstruction preserved the exact trigram multiset.
4. The reconstruction produced multiple distinct sequences for each corpus.
5. Results were deterministic for the fixed seed range.

**Result: 5/5 checks passed in the local execution.**

## Important observation

Ω-INF-4's compression effect replicated only in the weak sense that trigram-preserving reconstructions remained measurably different sequences and could alter higher-order metrics. The direction of zlib change was not universal: technical and literary means were slightly below the originals, random-like was slightly above, and structured was clearly above.

Therefore Ω-INF-5 does **not** support a universal claim that trigram-preserving reconstruction must increase or decrease compressibility.

## Status

**DESCRIPTIVE / CONTROL — OPEN.**

This result is deliberately retained as a constraint on interpretation. The next step should improve corpus size and sampling controls rather than immediately increase n-gram order.
