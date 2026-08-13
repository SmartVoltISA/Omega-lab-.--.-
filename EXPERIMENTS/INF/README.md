# Ω-INF-1 — Character order and structural information

**Date:** 2026-08-13
**Status:** EXPLORATORY / initial controlled result
**Hypothesis:** H-INF-1

## Question

If the exact same elements are retained, does changing only their organization produce measurable structural differences?

## Controlled intervention

One fixed Russian-language Ω text of 855 Unicode characters was used.

The intervention randomly permuted all characters while preserving:

- sequence length;
- every character;
- multiplicity of every character;
- encoding procedure.

Randomization used seed `20260813` and 100 independent permutations.

## Metrics fixed for this run

1. symbol entropy — composition control;
2. first-order conditional entropy — local sequential organization;
3. unique bigrams — local relation diversity;
4. zlib compressed byte length — operational compressibility proxy;
5. simple LZ phrase-dictionary complexity proxy.

## Results

| Metric | Original | 100-shuffle mean | Difference (shuffle − original) |
|---|---:|---:|---:|
| Length | 855 | 855 | 0 |
| Symbol entropy, bits | 4.6327 | 4.6327 | 0 |
| Conditional entropy, bits | 2.9979 | 3.7262 | +0.7283 |
| Unique bigrams | 281 | 436.06 | +155.06 |
| zlib bytes | 654 | 824.24 | +170.24 |
| LZ complexity proxy | 359 | 387.75 | +28.75 |

The composition metric is exactly invariant, as expected. The organization-sensitive metrics changed substantially in this controlled intervention.

## Interpretation

**Observation:** the same multiset of characters produced different measurable sequential/structural properties after permutation.

**Interpretation:** the original text contains non-random organization at the tested character-order level. This organization makes the sequence more locally predictable and more compressible than the shuffled controls.

**Not established:** this experiment does not prove that "information is physically located in relations", nor does it establish a universal definition of information. It demonstrates an operational distinction between composition and organization.

## Status of H-INF-1

**OPEN — supported by this initial controlled run, not confirmed as a general law.**

The main remaining threats are:

- short single-text sample;
- dependence on language and text genre;
- metric dependence;
- possible encoding/compression artifacts;
- character-level representation only.

## Required next controls

### Ω-INF-2 — Corpus replication

Repeat the same intervention across many independent texts and genres.

### Ω-INF-3 — Hierarchical permutation

Compare:

- character shuffle;
- word shuffle;
- sentence shuffle;
- paragraph shuffle.

This separates structural levels instead of collapsing them into one intervention.

### Ω-INF-4 — Local-preservation control

Shuffle while preserving bigram or trigram statistics as far as possible. This tests whether the measured effect requires only local relations or longer-range organization.

### Ω-INF-5 — Recovery

Ask whether the original organization can be recovered from a relational trace without access to the original ordering.

## Reproducibility

Code: `Omega-INF-1_character_order.py`

Tests: `test_Omega-INF-1.py`

Archived numerical output: `RESULTS.json`

All three are part of the experiment record. The experiment must not be silently rewritten if later controls weaken or reject its interpretation.
