# Ω-INF — Information and organization

This series operationally investigates the distinction between element composition and relational organization.

It does **not** assume a universal definition of information and does not treat compression, entropy or complexity as direct semantic measures.

## Experiments

### Ω-INF-1 — Character order

**Question:** If the exact same elements are retained, does changing only their order produce measurable structural differences?

- 855-character fixed Ω text;
- 100 character permutations;
- seed 20260813;
- composition preserved exactly.

Result: symbol entropy remained invariant, while conditional entropy, unique bigrams, compression and the LZ proxy changed substantially.

Status: **OPEN — initial controlled support for the operational distinction between composition and organization.**

### Ω-INF-2 — Hierarchical scrambling

**Question:** Do low-level metrics respond differently when organization is destroyed at character, word, sentence or paragraph level?

Conditions:

- T0 original;
- T1 character shuffle;
- T2 word shuffle within paragraph;
- T3 sentence shuffle within paragraph;
- T4 paragraph shuffle.

Result: T1 strongly changed low-level relational metrics; T2–T4 changed them only slightly for this short text.

This is a useful negative/control result: destroying a higher-level textual organization does not necessarily produce a large change in low-level metrics.

Status: **DESCRIPTIVE / OPEN.**

### Ω-INF-3 — Local relations preserved

**Question:** Can longer-range organization change while the exact local bigram inventory remains fixed?

A randomized Eulerian reconstruction preserves every original character bigram exactly once while changing the resulting sequence.

Across 100 runs:

- character composition: invariant;
- bigram multiset: invariant;
- conditional entropy: invariant;
- unique bigrams: invariant;
- zlib compressed size: original 654 bytes; reconstructed mean 734.54 bytes (range 718–747).

Status: **PARTIALLY SUPPORTED in the tested representation.**

This is the key control after Ω-INF-1: preserving first-order local relations is not sufficient to preserve all measured sequence structure.

### Ω-INF-4 — Trigram relations preserved

**Question:** Does the Ω-INF-3 effect survive when the exact trigram inventory is also fixed?

A randomized Eulerian traversal over overlapping character bigrams preserves every original trigram exactly once.

Across 100 runs on the fixed Ω text:

- character composition: invariant;
- bigram multiset: invariant;
- trigram multiset: invariant;
- first- and second-order conditional entropy: invariant;
- zlib compressed size: original 654 bytes; reconstructed mean 680.29 bytes (range 665–692).

Status: **PARTIALLY SUPPORTED in the tested representation.**

Important limitation: this remains one short text and one reconstruction family. No semantic or universal conclusion follows.

### Ω-INF-5 — Independent corpus replication

**Question:** Does the Ω-INF-4 observation replicate on other sequences without increasing the n-gram order?

Four independent short corpora were tested: technical, literary, random-like, and deliberately structured. Each received 100 trigram-preserving Eulerian reconstructions.

The exact trigram inventory was preserved in all runs. However, the compression effect was **not universal in direction**:

| Corpus | Original zlib | Reconstruction mean | Mean difference |
|---|---:|---:|---:|
| technical | 355 | 352.05 | -2.95 |
| literary | 286 | 284.09 | -1.91 |
| random-like | 195 | 196.46 | +1.46 |
| structured | 239 | 247.23 | +8.23 |

This is an important control result. The experiment does **not** support a universal rule that preserving trigram statistics causes compression to increase or decrease. It does support that the intervention can change higher-order sequence organization while the exact trigram inventory remains fixed.

Status: **DESCRIPTIVE / CONTROL — OPEN.**

## Current research path

```text
Ω-INF-1
  ↓
same elements, changed order
  ↓
Ω-INF-2
  ↓
organizational levels
  ↓
Ω-INF-3
  ↓
same elements + same bigram relations, changed longer-range organization
  ↓
Ω-INF-4
  ↓
same elements + same trigram relations, changed longer-range organization
  ↓
Ω-INF-5
  ↓
independent corpus replication
  ↓
NEXT: larger corpus + stronger sampling controls
```

## Core rule

A metric change is an observation about the metric. It is not automatically a measurement of semantic information.

Every experiment must preserve controls, archive code and tests, and retain negative results and methodological failures.
