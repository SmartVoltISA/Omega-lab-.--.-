# EXP-C1-018 — M3: Fibonacci-prime spiral structure

Date: 2026-08-28
Status: strong structural observation / independently arithmetic-verified; mechanism not yet established

## Question
Does the 4×4 numerical grid associated with Liber Primus contain a position-aware structure that is invisible to value-only tests?

## Source
The grid is recorded in the Cicada 3301 research corpus as:

3258 3222 3152 3038
3278 3299 3298 2838
3288 3294 3296 2472
4516 1206 708 1820

A community research source documents the transformation below and the corresponding Fibonacci/spiral interpretation. The arithmetic mapping itself is independently checked here.

## Transformation
For the first twelve cells, subtract the grid value from 3301:

3258 -> 43
3222 -> 79
3152 -> 149
3038 -> 263
3278 -> 23
3299 -> 2
3298 -> 3
2838 -> 463
3288 -> 13
3294 -> 7
3296 -> 5
2472 -> 829

These are primes.

For the bottom row, the community interpretation uses a sign change for the first two cells:

3301 + 4516 = 7817
3301 + 1206 = 4507
3301 - 708  = 2593
3301 - 1820 = 1481

These are also primes.

## Prime ordinal mapping
Using 0-based prime index:

43 -> 13
79 -> 21
149 -> 34
263 -> 55
23 -> 8
2 -> 0
3 -> 1
463 -> 89
13 -> 5
7 -> 3
5 -> 2
829 -> 144
7817 -> 987
4507 -> 610
2593 -> 377
1481 -> 233

The resulting index grid is:

13  21  34  55
 8   0   1  89
 5   3   2 144
987 610 377 233

These are exactly Fibonacci numbers F_7 through F_16 plus the initial 0,1,2,3,5,8 ordering, arranged spatially so that increasing Fibonacci index traces a spiral from the center outward:

0 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21 -> 34 -> 55 -> 89 -> 144 -> 233 -> 377 -> 610 -> 987.

Coordinate sequence (row,column, 0-based):

0:(1,1)
1:(1,2)
2:(2,2)
3:(2,1)
5:(2,0)
8:(1,0)
13:(0,0)
21:(0,1)
34:(0,2)
55:(0,3)
89:(1,3)
144:(2,3)
233:(3,3)
377:(3,2)
610:(3,1)
987:(3,0)

This is a continuous square spiral from the center to the outer boundary.

## Interpretation
This is substantially stronger than the earlier totient-only hypothesis because the relation uses BOTH value and position:

value -> prime -> prime ordinal -> Fibonacci index -> spatial path

The result therefore supports the current direction of testing position-aware operators and graph structure.

It does NOT yet prove that this is the intended decoding algorithm. In particular:

1. The sign change in the bottom-left two cells must be independently established from the original artifact, not inferred only from a community reconstruction.
2. We must test whether the same construction occurs elsewhere in Cicada material.
3. We must compare against null grids preserving the same dimensions and value multiset.
4. We must determine whether the spiral is a routing instruction, a key, an ordering function, or merely an embedded mathematical signature.

## Current status
FIBONACCI-SPIRAL-IN-M3 = STRONG STRUCTURAL OBSERVATION.

POSITION-AWARE GRAPH HYPOTHESIS = SUPPORTED FOR THIS OBJECT, NOT GENERALIZED.

DECRYPTION ALGORITHM = NOT ESTABLISHED.

## Next tests
- Reconstruct the exact original M3 sign convention from primary page imagery.
- Test null permutations of the same 16 values: preserve values, shuffle positions, measure probability of obtaining the exact Fibonacci-index set and a single continuous spiral.
- Test whether 3301 is the unique offset producing all-prime transformed values under the required sign convention.
- Search for the same prime-ordinal/Fibonacci construction in M1, M2, M7 and other Cicada numerical objects.
- Treat the resulting spiral as a candidate graph/routing layer and test whether its endpoint or traversal selects a known page, address, key, or cipher operator.

## Research principle
This result upgrades the hypothesis only because the mapping is reproducible and position-aware. Do not promote it to a key until null controls and cross-object replication are passed.
