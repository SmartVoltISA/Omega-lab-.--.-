# EXP-C1-019 — 3301/1033 as an operational bridge

**Status:** STRONG STRUCTURAL EVIDENCE; not a final LP key
**Date:** 2026-08-28

## Verified chain

2014 archive material documents the `Interconnectedness` MP3 and extraction of `magicsquares.txt` with OpenPuff 4.0.0. The archived extraction notes give the password as `33011033` and produce three magic squares. Independent archive copies preserve the same payload.

The three squares have magic constants:

- 5x5: 3301
- 7x7: 1033
- 5x5: 1033

The third 5x5 square is exactly the matrix later reproduced in Liber Primus Page 63.

Therefore `3301` and `1033` are not merely co-occurring numbers in the same puzzle. Their concatenation `33011033` was operationally used as a steganographic extraction password for the artifact containing the three squares.

## Important distinction

This does **not** prove that `33011033` is a universal Cicada key, nor that 3301 -> 1033 is a mathematical transformation. The password may have been a puzzle-specific bridge supplied by the earlier hidden data.

One secondary source contains `33011103`; the primary/archival extraction record used here gives `33011033`. Treat `33011033` as the currently supported value and keep the discrepancy recorded rather than silently normalizing it.

## Graph interpretation

The evidence now supports a concrete multi-node path:

portrait/hidden numbers -> 1033 + 3301 -> `33011033` -> OpenPuff -> `magicsquares.txt` -> three magic squares -> LP matrix recurrence

This is stronger than the previous `3301 -> 1033` digit-reversal hypothesis because the relation is operational: the combined values are actually used to unlock the next artifact.

## Falsification / next tests

1. Reconstruct the portrait extraction that yields the two sums independently.
2. Verify the OpenPuff password and payload checksum from an archived carrier.
3. Determine whether `33011033` or its components appear as an input/identifier later in the 2014 chain.
4. Test whether the three squares encode a deterministic endpoint, key, or ordering rule; do not assume they do.
5. Compare the LP 1033 square against the two hidden squares for a shared generator or conserved invariant.

## Current conclusion

`3301 + 1033 -> 33011033 -> hidden magic-square artifact` is an operationally demonstrated bridge in the 2014 puzzle chain. This is currently the strongest concrete evidence for the hypothesis that numerical invariants can function as graph edges/keys between representation layers.