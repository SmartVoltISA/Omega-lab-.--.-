# EXP-C1-002 — 4×4 prime/Fibonacci grid

**Status:** PROVED as a structural transformation; interpretive meaning remains UNKNOWN.
**Date:** 2026-08-28

## Input

The published 4×4 grid is:

```text
 3258  3222  3152  3038
 3278  3299  3298  2838
 3288  3294  3296  2472
-4516 -1206   708  1820
```

## Operation

For every cell calculate `|3301 - x|`.

Result:

```text
43    79   149   263
23     2     3   463
13     7     5   829
7817 4507  2593  1481
```

All 16 results are prime.

Then replace each prime with its zero-based ordinal index in the ordered list of primes.

Result:

```text
13   21   34   55
 8    0    1   89
 5    3    2  144
987  610  377  233
```

These are exactly the first 16 Fibonacci numbers beginning with 0,1,2,3,5,8,... placed in the grid.

Sorting cells by Fibonacci index gives coordinates:

```text
0   -> (2,2)
1   -> (2,3)
2   -> (3,3)
3   -> (3,2)
5   -> (3,1)
8   -> (2,1)
13  -> (1,1)
21  -> (1,2)
34  -> (1,3)
55  -> (1,4)
89  -> (2,4)
144 -> (3,4)
233 -> (4,4)
377 -> (4,3)
610 -> (4,2)
987 -> (4,1)
```

This traces a continuous inward-to-outward spiral from the central 2/3 pair through the 4×4 perimeter.

## Result

**PROVED:** the published grid encodes a Fibonacci ordering through prime ordinals after transformation relative to 3301.

**NOT PROVED:** that this spiral is the actual traversal rule for Liber Primus ciphertext.

**NOT PROVED:** that the grid itself supplies the LP2 keystream.

## Consequence for Ω-CICADA

The grid is now a valid structural support, not merely a visual/numerological observation. The next experiment must test whether this ordering reproduces any independently known ordering/key material elsewhere in Cicada. If it fails on known controls, it must not be used to force an LP2 solution.

## Negative-control requirement

Repeat the same transformation with:

1. random 4×4 permutations of the 16 primes;
2. nearby constants instead of 3301;
3. random prime sets of the same size.

Measure whether an equally clean Fibonacci/spiral encoding occurs by chance. The observed construction is strong evidence of intentional structure, but this control determines how diagnostic it is for later decryption.
