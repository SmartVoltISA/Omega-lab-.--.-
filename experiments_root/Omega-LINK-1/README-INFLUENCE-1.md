# Ω-LINK-1 — Influence-1

**Status:** FROZEN / protocol

## Question
Can the structural influence of a single edge be quantified by the change in reachable-state space caused by removing that edge?

## Definition
For an edge `e`, compare the baseline reachable-state set with the reachable-state set after removing only `e`.

Primary influence score:

`Influence(e) = |R_base| - |R_without_e|`

where `R` is the union of reachable nodes from the matched starting-state set.

Secondary measures:

- number of source nodes whose reachable set changes;
- total lost source→target reachability pairs;
- change in immediate next-choice count;
- change in shortest-path distances where a target remains reachable.

## Controls

- Node set fixed.
- Node attributes fixed.
- Transition rule fixed.
- Only one edge removed per intervention.
- No memory and no stochastic choice in the primary test.

## Interpretation boundary

The score measures structural influence under this specific graph and transition definition. It is not assumed to be a universal measure of causal importance.

## Falsification

If edge removal systematically produces no measurable change in the defined reachability measures, the proposed influence measure does not distinguish the tested edge roles.
