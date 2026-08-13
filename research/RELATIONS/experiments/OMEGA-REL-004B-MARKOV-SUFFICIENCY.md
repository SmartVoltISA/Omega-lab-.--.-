# Ω-REL-004B — Markov sufficiency of the node-state pair

Date: 2026-08-13
Status: EXECUTED / RESULT

## Question

Can a memoryless relation between A and B retain an additional hidden relational history when the complete current state is only `(A,B)` and the transition rule is fixed?

## Model

Two binary states:

`S(t) = (A(t), B(t))`

with deterministic mutual update:

`S(t+1) = F(S(t))`

No edge state and no history variable are present.

The test used all 144 mutually coupled Boolean rule pairs from Ω-REL-004A.

## Test

For every mutually coupled rule pair:

1. generate histories from all four possible initial states;
2. follow every trajectory for 0–6 steps;
3. group all observations by their current pair `(A,B)`;
4. whenever the same current pair is reached through different histories, compare its next 10 states;
5. test whether two identical current node states can have different futures solely because of different prior histories.

## Result

Across all 144 mutually coupled rules:

- 576 grouped current-state observations were checked;
- every identical current `(A,B)` state produced the same future trajectory under the fixed deterministic rule;
- number of violations: **0**.

Therefore, within this model:

`Future = F(A,B)`

and no additional history variable is observable once the complete current node state is specified.

## Interpretation

This is not a proof about arbitrary Ω models. It is a result about the tested memoryless deterministic class.

The result establishes an important constraint:

> An independent persistent relation-state cannot hide inside a deterministic model whose complete state is only `(A,B)` and whose transition rule is fixed.

Any apparent path dependence must be encoded in one of:

- current A/B state;
- an explicit relation state;
- environment/context;
- stochastic state not represented by `(A,B)`;
- an adaptive transition rule.

Therefore, if a future experiment finds genuine path dependence while A and B are exactly matched and external conditions are matched, an additional state variable is logically required.

## Consequence for Ω-REL research

We now have a clean distinction:

`node-state memory` ≠ `relation-state memory`

If the history is stored in A or B, the relation itself has not yet been shown to possess independent memory.

## Next test

Ω-REL-005 should search for the minimal mechanism that allows a relation to acquire an independent state while remaining distinguishable from memory stored in A/B.

`Execution performed; result recorded.`
