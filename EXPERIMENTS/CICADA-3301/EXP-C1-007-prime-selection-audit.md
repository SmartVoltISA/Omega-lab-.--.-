# EXP-C1-007 — Prime-selection audit of LP2 P20

**Date:** 2026-08-28
**Status:** ACTIVE / correction of prior hypothesis

## Finding

The community master tracker calls the P20 split a "prime-position stream" / "non-prime stream" and elsewhere describes it as value-based. This terminology is internally inconsistent with Gematria Primus: the 29 Gematria values are themselves the first 29 primes.

Therefore the statement "prime-valued vs non-prime-valued rune" cannot literally mean testing the Gematria value for primality. Every rune would pass.

Reference Gematria table: 29 symbols, indices 0–28, values 2–109, all prime.

## Consequence

Our previous claim that the 166-rune stream was established by "prime indices" is NOT yet independently proved. The number 166 must be regenerated directly from the original P20 transcription by an explicitly stated selection rule.

Candidate selection rules to distinguish:

1. prime positions in the full rune stream;
2. prime positions after punctuation removal;
3. prime-valued rune classes (expected to select all rune classes, therefore a negative control);
4. prime indices of the Gematria alphabet;
5. another prime-derived mask used by the original solver.

## Hard arithmetic controls

- P20 is reported as 166 selected + 646 non-selected = 812 rune tokens.
- The count of ordinary prime positions among 1..812 is 141, not 166.
- Therefore "166 = prime positions" cannot be accepted without an additional indexing convention.
- All 29 Gematria values are prime, so "prime values" cannot by itself produce a 166/646 partition.

## Experimental requirement

Reconstruct the 812-token P20 stream from the primary transcription and generate every candidate mask above. For each mask:

A. report selected count;
B. report exact selected positions;
C. apply the claimed Beaufort + Deor operation;
D. test the claimed 2×83 rearrangement;
E. compare against shuffled-position controls;
F. only then classify the mechanism.

## Status

- Gematria values are all prime: PROVED.
- P20 total/166+646 split: reported by community tracker, but selection mechanism: UNKNOWN.
- "prime-position" as ordinary 1-based prime positions: REJECTED by count mismatch (141 != 166).
- "prime-valued rune" as Gematria-value primality: REJECTED as non-discriminating.
- 2×83 transpose: PLAUSIBLE/REPORTED, pending reconstruction from the primary stream.

## Why this matters

This is a deliberate foundation correction. We do not build further hypotheses on an undefined selector. The next experiment must recover the selector itself from the raw P20 data.
