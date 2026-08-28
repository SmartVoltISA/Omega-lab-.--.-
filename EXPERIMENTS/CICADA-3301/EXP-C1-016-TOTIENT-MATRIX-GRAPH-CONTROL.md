# EXP-C1-016 — Totient matrix graph control

Date: 2026-08-28
Status: negative / weak signal

## Question
Do the three Liber Primus numerical matrices form an internal totient graph, and is the observed structure stronger than a null model?

## Source correction
The primary transcription/search result gives Matrix 3's last row as `4516  1206  708  1820`. An earlier exploratory matrix file contained `820` in that position and consequently reported an incorrect trace of 10673. The source-consistent Matrix 3 uses **1820**, giving trace **11673**. The 1820 value is independently present in the page transcription. This correction supersedes the earlier 820/10673 observation.

## Strict criterion
An internal phi edge requires both n and phi(n) to be actual elements of the same matrix. External preimages such as 4115 -> 3288 are excluded because the source values are absent from the matrix.

## Result
Under the strict internal-edge criterion, each matrix has one unique phi edge:

- Matrix 1: 131 -> 130
- Matrix 2: 626 -> 312
- Matrix 3: 3299 -> 3298

Repeated occurrences of the same values are not counted as new unique edges.

## Matrix structure control
Matrix 1 is a genuine 5x5 magic square: every row and column sums to 1033, and it has 180-degree rotational symmetry.

Matrix 2 is also a genuine 5x5 magic square: every row and column sums to 3301, and it has 180-degree rotational symmetry.

Matrix 3, using the source-consistent 1820, is a 4x4 numeric grid but is **not** a conventional magic square: row sums are 12670, 12713, 12350, 8250; column sums are 14340, 11021, 10454, 10168. It also lacks the 180-degree symmetry of Matrices 1 and 2.

This distinction is important: do not treat all three grids as one homogeneous magic-square family without further evidence.

## Control interpretation
The strict result does not establish that the matrices were constructed as totient graphs. The one unique phi edge per matrix is a weak structural signal, not a demonstrated decoding mechanism. The earlier broader preimage scan contained mathematically valid phi preimages but overcounted evidence by allowing source values absent from the matrix.

## Related observations
- Matrix 1 trace/magic constant = 1033.
- Matrix 2 trace/magic constant = 3301.
- Matrix 3 trace = 11673 with the source-consistent 1820.
- Matrix 3 contains 3299 and 3298, giving the exact internal relation phi(3299)=3298.
- LP1 explicitly couples its content to primes and the totient function, but thematic proximity is not causal proof.

## Decision
TOTIENT-AS-INTERNAL-MATRIX-GRAPH = UNCONFIRMED.
Do not use the phi edges as a decryption key or endpoint generator.

## Next test
Move from value-only edges to position-aware structure. Compare row/column permutations, 180-degree symmetry, center/trace relations, Gematria residues, and cross-matrix transitions. Use shuffled/null controls preserving dimensions and the exact multiset of values.

## Research principle
Preserve negative results and corrections. The earlier 820/10673 observation is explicitly superseded rather than deleted from the research history.