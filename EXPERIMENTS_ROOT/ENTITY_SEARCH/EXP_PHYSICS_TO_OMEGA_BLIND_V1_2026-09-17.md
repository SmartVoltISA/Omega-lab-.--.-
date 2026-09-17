# EXP_PHYSICS_TO_OMEGA_BLIND_V1 — 2026-09-17

Status: PILOT / EXECUTED / OPEN

## Objective
Test the reverse direction:

physical observations → anonymized transition structure → Ω structural fingerprint → candidate class.

The physical labels are not used as input to the structural matching stage.

## Blind abstraction layer
Three anonymized behavioral classes were represented only by transition-level observations:

A: two persistent states with reversible transitions and distinct switching thresholds.
B: two persistent states with reversible transitions but no hysteretic memory requirement.
C: three states with neighboring transitions and asymmetric metastable behavior.

The labels were intentionally removed before structural matching.

## Structural reconstruction
A small directed transition-graph library was generated for 2–4 states. 2,305 connected candidate transition graphs were enumerated under the pilot constraints.

Exact transition-count matching identified:
- A: a unique 2-state mutual-transition topology.
- B: the same coarse topology as A, demonstrating that topology alone cannot recover hysteresis or threshold behavior.
- C: 15 coarse topological matches, requiring higher-order behavioral descriptors to discriminate.

## Critical result
The reverse map is feasible at the coarse structural level, but topology alone is insufficient.

Therefore the fingerprint must include behavior beyond graph connectivity:

state graph + switching thresholds + hysteresis + basin structure + perturbation response + recovery + symmetry/scaling where measurable.

This is a positive methodological result because the blind test exposes exactly what information is lost by over-aggressive abstraction.

## Physical correspondence layer
The anonymized class A/B pattern is consistent with documented physical bistable/hysteretic systems. Examples include reprogrammable bistable mechanical metamaterials and elasto-magnetic mechanical memory. The physical examples are used only after abstraction as correspondence checks, not as labels during reconstruction.

## Falsification / controls
A valid future test must include:
1. physical datasets with labels withheld;
2. preregistered feature extraction;
3. multiple competing abstract representations;
4. matched random/null transition systems;
5. held-out physical systems;
6. scoring defined before label reveal;
7. no post-hoc feature selection after correspondence is observed.

## Decision
SUPPORT the reverse-search mechanism as a computational method at pilot level.
DO NOT promote to physical ontology evidence.

Next: use richer physical trajectories and require bidirectional convergence:

Physics → Ω fingerprint ← Ω discovery

with the physical label revealed only after both sides produce their fingerprints.
