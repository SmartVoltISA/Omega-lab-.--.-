# EXP-C1-019 — M3 Fibonacci/spiral control

Date: 2026-08-28
Status: strong structural observation; endpoint interpretation unresolved

## Object
LP2 internal page 15 / archive page 32 4x4 grid:

3258 3222 3152 3038
3278 3299 3298 2838
3288 3294 3296 2472
4516 1206 708 1820

The primary archive confirms this exact grid. The community analysis documents the standard transformation: 3301-X for the first 14 cells and 3301+X for the final two bottom-left cells, yielding primes whose 0-based ordinal indices are Fibonacci numbers. The two bottom-left cells are the documented sign anomaly.

## Reproduction
Using the documented sign convention:

43, 79, 149, 263
23, 2, 3, 463
13, 7, 5, 829
7817, 4507, 2593, 1481

Prime indices (0-based):

13, 21, 34, 55
8, 0, 1, 89
5, 3, 2, 144
987, 610, 377, 233

These are exactly the first 16 Fibonacci numbers in a positional arrangement. Reading cells by increasing Fibonacci index produces a continuous spiral path through all 16 cells.

## Control logic
A permutation control is conceptually decisive here: once the 16 transformed prime indices are fixed, a uniformly random permutation of the 16 values has probability 1/16! of placing the exact Fibonacci-index labels in the exact observed positions. This is approximately 4.78e-14. Monte Carlo is therefore unnecessary for the exact-pattern null; it is useful only for weaker similarity metrics.

Important caveat: the sign convention itself is not derived by this test. Fourteen cells use 3301-X and the two bottom-left cells use 3301+X. The sign anomaly is part of the observed construction and must be explained separately; treating it as freely chosen would introduce selection bias.

## Structural interpretation
The strongest defensible result is NOT '3301 is the key' and NOT 'this is a complete decryption algorithm'. It is:

1. A fixed 16-value grid is transformed into primes using a nearly uniform arithmetic rule with a localized two-cell exception.
2. The resulting primes map to exact 0-based prime ordinals.
3. Those ordinals are exactly the first 16 Fibonacci numbers.
4. Their spatial placement encodes a continuous spiral traversal.

This is a strong positional/graph-like structure.

## Endpoint test
The terminal Fibonacci label is 987, located at the bottom-left cell. The spiral therefore terminates at the bottom-left cell under the ascending-index traversal. This does NOT by itself identify a next page, URL, key, or plaintext endpoint. No endpoint claim is promoted.

## Status
M3-FIBONACCI-INDEX-SPIRAL = STRONG / REPRODUCED.
M3-ENDPOINT = UNKNOWN.
SIGN-ANOMALY = UNEXPLAINED.
3301-AS-UNIVERSAL-KEY = UNCONFIRMED.

## Next test
Treat the 16 cells as a graph with directed edges induced by consecutive Fibonacci labels. Compare the resulting edge geometry against: knight moves, king/rook/bishop adjacency, spiral coordinates, page/rune positions, and known LP transition structures. Separately test whether the two sign-flipped cells represent a deliberate direction reversal/Mobius-like fold or a transcription/encoding convention.

## Research principle
Do not infer a next address from the terminal cell without an independently reproducible mapping. Preserve the exact sign anomaly as data, not as a convenient correction.
