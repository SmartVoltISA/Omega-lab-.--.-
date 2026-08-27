# Ω-CICADA-3301 — Research Branch

**Status:** exploratory research
**Branch:** `research/cicada-3301`
**Goal:** independently investigate the unresolved Cicada 3301 / Liber Primus structure using reproducible experiments.

## Research rule

No candidate plaintext, key, sequence, or mechanism is accepted as a solution merely because it produces plausible English.

Every result is classified as:

- **PROVED** — reproduced from primary material and independently verified;
- **PLAUSIBLE** — supported by evidence but not uniquely established;
- **UNKNOWN** — not established;
- **REJECTED** — tested and contradicted by a defined criterion.

## Working cycle

`find → verify → experiment → verify result → record → next support`

A failed experiment is a result and must remain recorded.

## Initial known supports

1. Gematria Primus: 29-rune alphabet.
2. Solved Liber Primus pages provide verified examples of Caesar/Atbash/Vigenère-style transformations and a prime/totient stream.
3. Page 56 gives a confirmed prime/totient mechanism in the conservative community reconstruction.
4. Unsolved LP2 pages preserve word boundaries/punctuation in the available transcription.
5. The unsolved corpus has statistical properties inconsistent with simple substitution alone.
6. Prime-number, Fibonacci, and ordering mechanisms are recurring hypotheses, but their causal role in LP2 remains unproven.
7. OutGuess payloads exist in several LP2 images; some extracted material is currently unusable/garbled.

## First experimental branches

### C1 — Stream-key hypothesis
Test whether a deterministic keystream derived from primes/totients can reproduce known solved pages and then generalize to unsolved pages.

### C2 — Fibonacci / Lucas ordering
Test Fibonacci, Lucas, and combined index-selection rules against known solved pages before applying them to unknown pages.

### C3 — Single-rune constraints
Use one-rune English words as hard constraints (`A`/`I`) and infer candidate keystream values without assuming a global cipher.

### C4 — OutGuess payloads
Extract and classify payloads page-by-page. Do not treat garbage output as evidence of a key until independently validated.

### C5 — Negative controls
Apply each candidate mechanism to shuffled/randomized controls. A mechanism that produces equally good English-like output on controls is rejected as non-diagnostic.

## First target

LP2 unsolved corpus, beginning with one page at a time. The first objective is **not** to solve the book; it is to find one new, reproducible structural support that survives controls.

## Current external state

As of August 2026, community repositories still describe the majority of LP2 as unresolved, although several repositories publish claims of high-percentage or near-complete solutions. These claims are treated as hypotheses until independently reproduced.
