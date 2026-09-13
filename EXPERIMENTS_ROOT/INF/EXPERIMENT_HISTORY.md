# Ω-INF — Experimental History

This file is a chronological record of the information/organization experiments. It is intentionally a research log, not a polished success narrative.

## 2026-08-13 — Why the series began

A discussion about whether information can depend on organization rather than only on the inventory of elements led to a controlled question:

> If the same elements are retained while their organization is changed, which measurable properties change?

The series was deliberately framed without assuming a universal definition of information. Compression, entropy and complexity are treated as observables of representations, not as direct semantic measurements.

## Ω-INF-1 — Character order

**Question:** Does changing only character order produce measurable differences?

**Intervention:** 855-character fixed Ω text; 100 exact character permutations; composition preserved.

**Observed:** symbol entropy remained invariant while conditional entropy, unique bigrams, compression and the LZ proxy changed.

**Interpretation at the time:** initial controlled support for distinguishing composition from organization.

**Limit:** one short text; metrics are representation-dependent.

## Ω-INF-2 — Hierarchical scrambling

**Question:** Do the same low-level metrics respond equally to character, word, sentence and paragraph scrambling?

**Observed:** character scrambling strongly changed low-level metrics; word/sentence/paragraph scrambling changed them only slightly in this text.

**Important failure/control:** this showed that a metric that is sensitive to local character order is not automatically a detector of higher-level textual organization.

**Lesson:** do not equate metric change with semantic change.

## Ω-INF-3 — Local relations preserved

**Question:** Can longer-range organization vary while the exact bigram multiset is fixed?

**Intervention:** randomized Eulerian reconstruction preserving every original bigram.

**Observed:** composition, bigram multiset and first-order conditional entropy were fixed; zlib size changed from 654 bytes in the original to a mean of 734.54 bytes across 100 reconstructions.

**Status:** partially supported in the tested representation.

**Limit:** one text and one reconstruction family.

## Ω-INF-4 — Trigram relations preserved

**Question:** Does the observation survive when the exact trigram inventory is also fixed?

**Intervention:** trigram-preserving Eulerian reconstruction.

**Observed:** composition, bigrams, trigrams and first/second-order conditional entropy were fixed; zlib size changed from 654 bytes to a mean of 680.29 bytes across 100 reconstructions.

**Status:** partially supported in the tested representation.

**Limit:** one short text and one reconstruction family.

## Ω-INF-5 — Independent corpus replication

**Question:** Does the Ω-INF-4 compression direction replicate across different sequences?

**Observed:** no universal direction. Technical and literary corpora decreased in mean compressed size; random-like and structured corpora increased.

**Important correction:** the result was not promoted into a universal law. The experiment instead became evidence that the effect depends on the sequence and that preserving trigram inventory does not determine compression direction.

## Ω-INF-6 — Sampling control

**Question:** Could the Ω-INF-5 variation be an artifact of one reconstruction sampling policy?

**Intervention:** compared pre-shuffled adjacency lists with dynamic random edge choice, using the same trigram-preserving constraint, 100 runs per policy and corpus.

**Observed:** for technical, literary and structured corpora, the two stochastic policies produced the same direction of mean compression change. Both generated 100 distinct reconstructions for each of those corpora.

**Important limitation:** this does not establish universality; it only weakens one simple implementation-artifact explanation.

## Ω-INF-7 — Expanded reproducibility / control corpus

**Question:** Does the sampling-control result persist when the corpus and number of reconstructions are expanded, and where does the reconstruction family become degenerate?

**Design:** 8 deliberately different short sequences; 200 reconstructions per stochastic policy; exact trigram preservation checked on every reconstruction.

**New observation:** highly periodic sequences can have only one valid reconstruction under the preserved-trigram constraint. For `ABCD` repetition and `AB` alternation, both stochastic policies produced exactly one distinct sequence and no compression change.

This is an important negative result: **not every trigram-equivalence class contains many alternative organizations.**

For non-degenerate corpora, the two stochastic policies again gave closely matching mean compression directions. The repeated-phrase corpus showed a notably larger increase than the other natural-language controls.

**Status:** descriptive/control; open.

## Current position

The strongest defensible statement is still narrow:

> Preserving element composition and finite-order local n-gram inventories does not, by itself, guarantee preservation of every measured property of a sequence. The effect is representation- and corpus-dependent, and some trigram-equivalence classes are effectively degenerate.

Nothing in this history is evidence that semantic information has been located in relations, nor that a universal hierarchy of information has been demonstrated.

## Method rule

When a result is weaker than expected, it remains in the record. When a control fails or a reconstruction family is degenerate, that is recorded as a result, not removed as an inconvenience.
