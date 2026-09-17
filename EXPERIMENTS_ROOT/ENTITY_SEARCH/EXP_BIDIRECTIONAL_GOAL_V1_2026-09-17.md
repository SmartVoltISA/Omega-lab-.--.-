# EXP_BIDIRECTIONAL_GOAL_V1 — 2026-09-17

Status: EXECUTED / PARTIAL SUPPORT / OPEN

## Question
Can the same structural search framework operate in three directions?

1. Discovery: structure → candidate entity → invariants.
2. Reverse abstraction: physical observations → properties/relations → abstract structure.
3. Goal-directed search: goal constraints → candidate structure.

## Method
Small connected undirected graphs with 5 nodes were enumerated. Connected substructures of size 2–4 with a non-empty external boundary were treated as structural candidates.

For each candidate we computed:
- internal edge count;
- internal degree multiset as a simple invariant;
- boundary size;
- density;
- switchability under internal edge-state changes;
- persistence under randomized perturbations involving the candidate/interface.

The search generated 728 connected host graphs and 11,470 candidate substructures.

## Goal tests
Three toy objective functions were evaluated:

### A. State retention / memory-like goal
High persistence + two distinguishable internal states + sufficient internal organization.

Top candidates tended toward compact, densely connected substructures with an external interface and switchable internal configurations.

### B. Transmission/interface goal
Higher interface + lower internal closure + controlled persistence.

Top candidates tended toward smaller structures with more external boundary relative to internal density.

### C. Recovery/self-restoration-like goal
Persistence + interface + state-switch capability.

Top candidates were structurally different from the pure memory and transmission selections.

## Result
The goal functions changed the selected structural classes. Therefore the goal-directed search is not equivalent to simply returning the globally most persistent patterns.

This is a methodological result, not a physical discovery.

## Controls / limitations
The perturbation model is still synthetic. In particular, persistence can be inflated if the perturbation operator protects internal edges by construction. Therefore persistence ≠ physical entity evidence.

The next required control is a preregistered perturbation family in which internal, interface, and external changes are independently randomized, with matched-complexity null candidates and destructive controls.

## Physical correspondence check
The abstract pattern "stable state + reversible switching + recovery" has known physical analogues. Published examples include bistable mechanical structures and reprogrammable mechanical metamaterials with reversible binary states, as well as self-healing/self-restoring materials using reversible or movable crosslinks. These are correspondences of functional/structural patterns, not evidence that the abstract graph candidate is any particular physical object.

## Bidirectional criterion
A stronger future test is convergence:

Ω → abstract pattern ← Physics

If an abstract pattern is independently derived from relational search and independently reconstructed from physical observations, agreement of invariants and transformation behavior is stronger evidence than one-way pattern matching.

## Goal-directed criterion
A goal must specify observable structural constraints before candidate selection. The candidate must not redefine the goal or its promotion criteria.

## Status vocabulary
DEFINITION | MODEL | DERIVATION | EXECUTED | OBSERVED | SUPPORTED | HYPOTHESIS | THEOREM | COUNTEREXAMPLE | REJECTED | OPEN

## Current decision
PROMOTE as a methodology experiment: the architecture supports three distinct search modes, but physical entity claims remain OPEN until stronger controls and physical-data reverse mapping are executed.
