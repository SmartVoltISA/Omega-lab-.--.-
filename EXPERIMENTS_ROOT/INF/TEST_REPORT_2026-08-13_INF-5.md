# Ω-INF-5 — Test Report

**Date:** 2026-08-13  
**Runs:** 100 per corpus × 4 corpora  
**Corpora:** technical, literary, random-like, structured

## Checks

1. Every reconstruction preserved sequence length.
2. Every reconstruction preserved the exact character multiset.
3. Every reconstruction preserved the exact trigram multiset.
4. The reconstruction produced multiple distinct sequences for each corpus.
5. Results were deterministic for the fixed seed range.
6. The observed compression changes were not forced to have one direction.

**Result: 6/6 checks passed in the local execution.**

## Result

Technical: zlib 355 → 352.05 mean (Δ −2.95).  
Literary: 286 → 284.09 mean (Δ −1.91).  
Random-like: 195 → 196.46 mean (Δ +1.46).  
Structured: 239 → 247.23 mean (Δ +8.23).

## Important observation

Ω-INF-4's intervention replicates as a valid trigram-preserving reconstruction across all four corpora. However, the compression effect is corpus-dependent: two corpora move slightly downward and two upward.

Therefore Ω-INF-5 does **not** support a universal claim that trigram-preserving reconstruction must increase or decrease compressibility.

## Interpretation limit

This is a replication/control result. Compression remains an operational proxy for sequence structure, not a direct measurement of semantic information. No universal hierarchy is inferred.

## Status

**DESCRIPTIVE / CONTROL — OPEN.**

The next step should improve corpus size and sampling controls rather than immediately increase n-gram order.
