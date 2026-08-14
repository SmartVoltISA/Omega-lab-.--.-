# Ω-LINK-1 — Matrix / Reachability

**Status:** FROZEN / protocol only
**Date:** 2026-08-14

## Question

Does changing only the connectivity matrix change the space of reachable future states when the set of observable nodes remains fixed?

## Variables

- Node/state set: fixed across all conditions.
- Connectivity matrix: manipulated variable.
- Transition rule: fixed and local.
- Initial node: matched across conditions.

## Conditions

Construct matched directed graphs with the same nodes and equal edge count, but different edge placement/topology. Include a baseline graph and interventions in which exactly one edge is removed.

## Measurements

For every starting node:

1. number of reachable nodes;
2. set of reachable nodes within 1, 2, 3, ... steps;
3. shortest-path distance to each reachable node;
4. number of available next transitions;
5. whether an edge is structurally critical (its removal reduces reachability);
6. change in the transition-space after single-edge removal.

## Primary comparison

Hold the node/state matrix constant. Change only the connectivity matrix. Test whether reachability and immediate future-choice space change accordingly.

## Controls

- Same node labels and state definitions.
- Same edge count between matched graph conditions.
- Same starting-state distribution.
- No memory variable.
- No stochastic choice required for the primary graph-theoretic test.
- Verify that edge removal changes no node attributes.

## Falsification

The claim is weakened if matched graphs with different connectivity produce identical reachable-state sets and identical next-transition spaces under the fixed transition rule, or if apparent differences arise from unintended node/state changes.

## Non-claims

This experiment does not establish that connectivity is the only determinant of behavior. It tests only whether connectivity itself changes the mathematically available transition space under fixed node definitions and transition rules.

## Freeze rule

This protocol is frozen before implementation. Any change must be recorded as an amendment and must not silently alter the primary test.
