# Ω-INF-4 — Results

**Date:** 2026-08-13
**Status:** COMPLETED / CONTROL
**Seed range:** 20260815–20260914
**Runs:** 100

## Question

After preserving the exact trigram inventory, does any measurable sequence structure remain free to change?

## Intervention

The original text is represented as a directed multigraph:

- vertices = character bigrams;
- each character trigram = one directed edge between overlapping bigrams.

A randomized Eulerian traversal uses every original trigram exactly once and reconstructs a new sequence.

## Preserved exactly

- length: 855 characters;
- character multiset;
- exact bigram multiset;
- exact trigram multiset;
- unique bigram count: 281;
- unique trigram count: 549;
- first-order conditional entropy: 2.997873 bits;
- second-order conditional entropy: 1.243827 bits.

## Results

| Metric | Original | 100 reconstructed mean | Range / status |
|---|---:|---:|---|
| Length | 855 | 855 | exact invariant |
| Symbol entropy | 4.632675 | 4.632675 | exact invariant |
| Conditional entropy, order 1 | 2.997873 | 2.997873 | exact invariant |
| Conditional entropy, order 2 | 1.243827 | 1.243827 | exact invariant |
| Unique bigrams | 281 | 281 | exact invariant |
| Unique trigrams | 549 | 549 | exact invariant |
| zlib compressed bytes | 654 | 680.29 | 665–692 |

The standard deviation of reconstructed zlib size was **5.41 bytes**.

## Observation

The intervention successfully changed the sequence while preserving the complete first- and second-order n-gram inventories.

The compressed representation nevertheless changed: from **654 bytes** for the original to a mean of **680.29 bytes** for the reconstructed sequences.

## Interpretation

For this text, this reconstruction method, and this operational metric, preserving exact trigram statistics was **not sufficient to preserve the observed compressibility**.

This extends Ω-INF-3 by one controlled order: the effect seen in Ω-INF-3 does not disappear when all trigram counts are also held fixed.

## Important limitation

This is still a single short text and one reconstruction family. Compression remains only an operational proxy for sequence structure, not a direct measurement of semantic information. The result does not identify what the remaining structure is, nor prove that it is semantic.

No conclusion about a universal hierarchy of information is justified from this experiment alone.

## Status

**H-INF-4: PARTIALLY SUPPORTED in the tested representation.**

The next step should not be a deeper theoretical claim. The immediate control is replication on independent texts/corpora before increasing the order further.
