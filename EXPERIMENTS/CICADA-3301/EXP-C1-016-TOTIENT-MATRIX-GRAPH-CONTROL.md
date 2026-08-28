# EXP-C1-016 — Totient matrix graph control

Date: 2026-08-28
Status: negative / weak signal

## Question
Do the three Liber Primus numerical matrices form an internal totient graph, and is the observed structure stronger than a null model?

## Source
The matrix corpus and prior totient scan are recorded in the Cicada 3301 research repository. The strict criterion used here is: n is an element of a matrix AND phi(n) is also an element of the same matrix. External preimages such as 4115 -> 3288 are excluded because 4115 is not itself a matrix element.

## Result
Under the strict internal-edge criterion, each of the three matrices has one unique phi edge:

- Matrix 1: 131 -> 130
- Matrix 2: 626 -> 312
- Matrix 3: 3299 -> 3298

Repeated occurrences of the same values are not counted as new unique edges.

The earlier broader scan reported additional preimages (for example phi(4115)=3288, phi(4517)=4516, phi(3259)=3258). Those are mathematically valid preimages but are NOT internal graph edges because the source values are absent from the corresponding matrix. They must not be used as evidence for an internal matrix graph.

## Control interpretation
The strict result does not establish that the matrices were constructed as totient graphs. A null/random comparison is required before assigning evidential weight to the three observed edges. The observed signals are currently insufficient to promote the totient hypothesis.

## Related structural observations
- Matrix 1 trace = 1033.
- Matrix 2 trace = 3301.
- Matrix 3 trace = 10673 = 13 * 821.
- In Matrix 3, phi(821)=820 and both 821 and 820 occur in the matrix.
- The archive independently documents that LP1 explicitly emphasizes primes and the totient function.

These are observations, not causal proof.

## Decision
TOTIENT-AS-INTERNAL-MATRIX-GRAPH = UNCONFIRMED.
Do not use the phi edges as a decryption key or endpoint generator.

## Next test
Move from value-only edges to position-aware structural tests. For each matrix, test whether transformations are defined by (value, position), symmetry, row/column relations, Gematria residue, or cross-matrix transitions. Compare each candidate against shuffled/null matrices with identical dimensions and value multisets.

## Research principle
Preserve negative results and methodological corrections. The broader preimage scan remains archived as exploratory material; the strict internal-edge result is the current foundation for further testing.
