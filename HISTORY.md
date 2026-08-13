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

### Ω-INF-7 — Expanded Robustness / Sampling
Question: do the trigram-preserving reconstruction effects remain stable across more texts and seeds?

Protocol: four corpora, four deterministic seed families, 250 reconstructions per corpus; exact trigram multiset and character multiset preserved; compression measured with zlib.

Audit event: the first local run accidentally produced 248 samples per corpus because of integer division. That run was rejected and not archived as final data. The GitHub protocol was corrected to exactly 250 samples. A syntax error introduced during that correction was also detected by audit and fixed before the final figures were recorded.

Final observation: technical and literary corpora had predominantly negative mean compression deltas; the structured corpus had positive delta in all 250 reconstructions; the randomish corpus was centered essentially at zero. All four corpora produced 250 distinct reconstructions.

Status: robustness of the tested sampling procedure is strengthened, but there is still no universal direction. The effect remains corpus-dependent.

### Ω-INF-8 — Deliberate Falsification / Break Test
Question: can the Ω-INF-7 observation be weakened by changing reconstruction policy and observable while preserving exact trigram counts?

Protocol: four corpora; 80 reconstructions per corpus for each of four policies (two stochastic, two deterministic adversarial controls). Observables: zlib size, character entropy, bigram entropy, unique-bigram count. Exact trigram preservation was asserted for every reconstruction.

Audit result: the two stochastic policies reproduced the same qualitative sign for technical (negative), literary (negative), and structured (positive) corpora. The randomish corpus remained near zero and changed sign between stochastic policies. Character entropy, bigram entropy, and unique-bigram count did not change under trigram-preserving reconstruction; only zlib varied among the tested observables.

Important correction: Ω-INF-8 does NOT support a broad claim that "higher-order structure" is visible across arbitrary metrics. The effect observed here is specifically a compression effect under the tested reconstruction family, and its direction is corpus-dependent.

Status: the narrow implementation-artifact explanation is weakened, but the stronger interpretation remains unproven. Deterministic reverse/sorted controls are not treated as stochastic evidence.

## Current position

The strongest defensible statement is narrow:

> In tested finite sequences, preserving element composition and local n-gram statistics does not necessarily fix all measured higher-order sequential properties such as compression under the reconstruction procedures tested.

This is a statement about the experiments, not a general theory of information.

## Current rule

Before increasing n-gram order, strengthen controls where a methodological artifact is still plausible. Every failed or corrected run is part of the history.
