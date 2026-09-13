# Ω-INF-6 — Test Report

**Date:** 2026-08-13
**Runs:** 100 per policy and corpus

## Controls

- exact character multiset preserved;
- exact trigram multiset preserved;
- randomized pre-shuffled adjacency policy;
- independently randomized dynamic-choice policy;
- deterministic reverse and sorted traversals retained as controls.

## Results

The two randomized policies generated 100 distinct reconstructions per corpus and produced very similar compression distributions.

Mean zlib deltas:

| Corpus | Pre-shuffled | Dynamic-choice |
|---|---:|---:|
| technical | -3.20 | -3.46 |
| literary | -1.96 | -2.03 |
| structured | +8.24 | +8.00 |

The direction agrees between the two randomized policies for all three corpora.

## Interpretation

This is evidence against a simple implementation-specific explanation: the Ω-INF-5 pattern is not reproduced only by one exact randomization implementation. It remains dependent on corpus structure, however, and the experiment does not sample the full set of all trigram-equivalent sequences.

The deterministic reverse/sorted traversals are explicitly treated as controls rather than random samples.

**Status: DESCRIPTIVE / CONTROL — OPEN.**

Next step should improve corpus size and sampling coverage before increasing n-gram order.
