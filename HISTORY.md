# Ω-Lab — Research History

## Purpose

This file is a chronological research log. It records the path, including failed tests, methodological corrections, limits, and changes of interpretation. It is not a polished retrospective. Historical results must not be rewritten to make the path look cleaner.

## Working discipline

1. Record the question before the result whenever possible.
2. Preserve failed tests and methodological errors.
3. Separate observation, interpretation, and hypothesis.
4. Do not upgrade a local result into a universal claim without replication.
5. When a control weakens a claim, record that as a result, not as a setback to hide.
6. New experiments must not rewrite completed experiments.
7. Prefer one controlled change at a time.

## Information line — Ω-INF

### Ω-INF-1 — Character Order
Question: can changing only the order of an unchanged character multiset alter measurable sequential structure?

Intervention: preserve length and exact character multiset; randomly permute characters.

Observation: symbol entropy remained invariant while conditional entropy, bigram counts, compression size, and LZ-like complexity changed.

Status: supported for the tested text, intervention, and metrics.

Limit: this does not establish where information "is" in any metaphysical sense.

### Ω-INF-2 — Hierarchical Permutation
Question: which structural levels are visible to character-sequential metrics?

Interventions: character, word, sentence-within-paragraph, and paragraph permutations.

Observation: character scrambling produced a large local change; word scrambling produced a smaller change; sentence/paragraph scrambling produced very small changes under the current character-level metrics.

Important correction: weak metric response to higher-level scrambling is not evidence that higher-level structure was preserved. It may simply mean the metric does not observe that level.

### Ω-INF-3 — Local Relations Preserved
Question: if all first-order local relations (bigrams) are preserved, is the sequence fully determined for the measured structure?

Intervention: reconstruct sequences preserving the exact multiset of bigrams.

Observation: original and reconstructions shared the measured first-order statistics, yet compression differed.

Status: partially supported for the tested reconstruction family and metrics.

### Ω-INF-4 — Trigram Preservation
Question: if exact trigram statistics are preserved, is the measured structure fully determined?

Intervention: reconstruct sequences preserving the exact trigram multiset.

Observation: for the original Ω text, compression still differed across reconstructions.

Status: local result only.

### Ω-INF-5 — Independent Corpus Replication
Question: does the Ω-INF-4 compression direction generalize across different sequence classes?

Observation: no universal direction was found. Technical and literary samples moved slightly downward, pseudorandom slightly upward, and the structured sample upward more clearly.

Important correction: this falsified the stronger expectation that trigram-preserving reconstruction should consistently increase compression size.

### Ω-INF-6 — Sampling Control
Question: could Ω-INF-5 be an artifact of one particular reconstruction/sampling policy?

Intervention: compare different traversal/sampling policies while preserving the same trigram constraints.

Observation: the sign of the mean compression difference agreed between the compared stochastic policies for the tested corpus.

Limit: this rejects only a narrow implementation-artifact explanation; it does not prove a universal property of all trigram-equivalent sequences.

## Current position

The strongest defensible statement is narrow:

> In tested finite sequences, preserving element composition and local n-gram statistics does not necessarily fix all measured higher-order sequential properties such as compression under the reconstruction procedures tested.

This is a statement about the experiments, not a general theory of information.

## Next planned step

Ω-INF-7 is a robustness/expanded-sampling control. The aim is to increase independent corpora, seeds, and reconstruction samples before increasing n-gram order. The purpose is to determine whether the observed effects survive broader sampling and whether any apparent effect is dominated by reconstruction method.
