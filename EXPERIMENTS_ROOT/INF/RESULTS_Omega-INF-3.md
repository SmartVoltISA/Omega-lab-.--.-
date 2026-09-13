# Ω-INF-3 — Results

**Date:** 2026-08-13
**Status:** COMPLETED / CONTROL
**Seed range:** 20260813–20260912
**Runs:** 100

## Question

Can we change longer-range organization while preserving the exact local relation inventory represented by character bigrams?

## Intervention

The original text is treated as a directed multigraph:

- vertices = characters;
- each adjacent character pair = one directed edge.

A randomized Eulerian traversal uses every original edge exactly once and reconstructs a new character sequence.

Therefore the following are held constant:

- character count;
- character multiset;
- exact bigram multiset;
- unique-bigram count;
- first-order conditional entropy.

## Results

| Metric | Original | 100 reconstructed mean | Range / status |
|---|---:|---:|---|
| Length | 855 | 855 | exact invariant |
| Symbol entropy | 4.632675 | 4.632675 | exact invariant |
| Conditional entropy | 2.997873 | 2.997873 | exact invariant |
| Unique bigrams | 281 | 281 | exact invariant |
| zlib compressed bytes | 654 | 734.54 | 718–747 |

The standard deviation of reconstructed zlib size was **5.50 bytes**.

## Observation

The experiment successfully changed the sequence while preserving the complete first-order adjacency inventory.

At the same time, compressed size changed substantially: from **654 bytes** for the original to a mean of **734.54 bytes** for the reconstructed sequences.

## Interpretation

This is evidence that, for this text and these operational metrics, **first-order local relations do not fully determine the longer-range organization captured by compressibility**.

In other words:

> preserving every character and every adjacent character-pair count is not sufficient to preserve all measured sequence structure.

This is a considerably stronger control than Ω-INF-1 because the intervention no longer destroys the local bigram statistics that Ω-INF-1 used to detect organization.

## Important limitation

Compression is still only an operational proxy. The experiment does not establish semantic information or prove that longer-range relations are the location of meaning.

The randomized Eulerian construction also samples only the space of sequences compatible with the observed bigram multigraph; it does not sample all sequences with the same local statistics uniformly.

## Status

**H-INF-3: PARTIALLY SUPPORTED in the tested representation.**

The result motivates a next control: preserve increasingly long n-gram statistics (bigrams, then trigrams) and determine how much additional structure remains measurable beyond each order.
