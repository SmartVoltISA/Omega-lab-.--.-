# Ω-REL-004A — Causal persistence after interaction

Date: 2026-08-13
Status: EXECUTED / RESULT

## Question

After mutual interaction creates joint dynamics between A and B, does the relation remain as an independently active causal dependency when the interaction rule is removed, without introducing an explicit memory variable?

## Model

Two binary states:

`A, B ∈ {0,1}`

Mutual phase:

`A' = f(A,B)`
`B' = g(A,B)`

All 16 Boolean functions of two binary inputs were available for each component, giving 256 possible mutual rule pairs. A rule was classified as mutually coupled when A's update depends on B and B's update depends on A. There are 144 such rule pairs.

Off phase:

`A' = f_off(A)`
`B' = g_off(B)`

All 16 independent rule pairs were considered as controls.

No memory variable, edge variable, hidden state, or adaptive coupling variable was introduced.

## Test 1 — causal dependence during interaction

For a given state `(A,B)`, A→B causal influence is present when changing A while holding B fixed changes B's next state. B→A is defined analogously.

Across the 144 mutually coupled rule pairs and 4 states each, 576 local state/rule combinations were checked.

256 combinations exhibited simultaneous local influence in both directions.

This confirms that the model can represent genuine mutual causal interaction at the state-update level.

## Test 2 — causal dependence after interaction is removed

After switching to any independent rule pair:

`A' = f_off(A)`
`B' = g_off(B)`

A change in A cannot alter B's next state, and a change in B cannot alter A's next state.

Observed causal cross-influence after switch-off:

`A→B = 0`
`B→A = 0`

for the independent control class.

Therefore the mutual causal relation is not retained merely because the system previously interacted.

## Test 3 — correlation can remain without causal relation

A separate ensemble test started from the four possible states with equal weight. A mutually coupled rule was applied for 3 steps, producing an ensemble with mutual information:

`MI(A;B) = 0.811278 bits`

The independent identity update was then applied for 5 steps. The joint-state distribution and mutual information remained unchanged.

Thus a statistical correlation can persist after causal interaction is removed, while the subsequent update rule contains no cross-dependence.

This is a critical distinction:

`correlation ≠ active relation`

at least under the causal definition used here.

## Result

The experiment does NOT show autonomous persistence of the relation.

It shows:

1. mutual interaction can create joint dynamics;
2. after the interaction rule is removed, cross-causal influence disappears immediately;
3. correlations created by the interaction can remain as a property of the joint state even when causal coupling is zero.

Therefore the current minimal memoryless model supports:

`interaction → joint state / correlation`

but does not support:

`interaction → independently persistent causal relation`

without an additional mechanism.

## Important implication

If Ω is to contain a relation that survives after the direct interaction is removed, the persistence must be encoded somewhere. Candidate locations are not yet determined:

- state of A or B;
- state of the relation itself;
- environment/context;
- topology/structure;
- history-dependent rule.

We must not call this "memory of the relation" until the storage location is identified.

## Next test

Ω-REL-004B should test whether persistent relational behavior can arise when the history is encoded only in the states of A and B, without an explicit edge variable. If it can, determine whether this is genuinely a relation property or merely node-state memory.

`Execution performed; result recorded.`
