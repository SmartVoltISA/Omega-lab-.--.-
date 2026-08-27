# EXP-C1-006 — Prime-index correction in P20

**Date:** 2026-08-28
**Status:** CONFIRMED STRUCTURAL CORRECTION

## Finding

The current community MASTER_TRACKER describes P20 as using a "prime-position" / "prime-valued" stream and lists the extracted rune letters:

`TH, O, C, W, J, P, B, M, D`

This wording is misleading. In Gematria Primus these are NOT a special subset of prime-valued rune values: every one of the 29 Gematria values is itself prime.

The listed nine runes correspond exactly to the **prime indices** of the 29-character Gematria alphabet:

index 2  = TH
index 3  = O
index 5  = C/K
index 7  = W
index 11 = J/IO
index 13 = P
index 17 = B
index 19 = M
index 23 = D

Thus the operative P20 partition is best described as:

**rune Gematria index is prime** vs **rune Gematria index is non-prime**.

This explains why the tracker can have a 166-rune selected stream and a 646-rune complementary stream without requiring "prime values" (which would select all runes).

## Consequence

The P20 clue chain is now structurally cleaner:

P19: `REARRANGING THE PRIMES...`
→ Gematria index of each rune
→ retain positions whose **alphabet index is prime**
→ 166-rune stream
→ 2×83 rearrangement
→ Beaufort with Deor
→ observed Old English fragments.

The complementary 646-rune stream is the non-prime-index class.

## Status

- "All Gematria values are prime": PROVED from the 29-entry alphabet.
- Listed P20 prime subset = prime alphabet indices: PROVED by direct index inspection.
- 166/646 partition: PROVED as the current repository's reported P20 counts; independent recount still desirable.
- `2×83` is a permutation/transposition of the selected 166 stream: REPORTED / REPRODUCIBLE CLAIM; exact orientation should be independently reconstructed from raw P20.
- Deor/Beaufort on the transformed stream: REPORTED working partial result.
- Why this exact prime-index rule is intended by Cicada: STRONGLY PLAUSIBLE from P19 + Gematria structure, but authorial intent is UNKNOWN.

## Critical distinction

Do NOT use the phrase "prime-valued rune" for this experiment. It is mathematically ambiguous/misleading because every Gematria rune has a prime value.

Use:

`prime Gematria index` = {2,3,5,7,11,13,17,19,23}

and

`non-prime Gematria index` = remaining indices {0,1,4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28}.

## Next experiment

Reconstruct the exact 166-rune prime-index stream from the raw P20 transcription, reproduce the 2×83 transformation in both orientations, and verify the Deor/Beaufort output against the reported Old English fragments. Then apply the same prime-index partition to P21–P54 as a structural test, without assuming the same cipher layer.
