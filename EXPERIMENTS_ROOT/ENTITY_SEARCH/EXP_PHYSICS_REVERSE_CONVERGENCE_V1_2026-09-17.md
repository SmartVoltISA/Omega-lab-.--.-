# EXP_PHYSICS_REVERSE_CONVERGENCE_V1 — 2026-09-17

Status: EXECUTED / PARTIAL SUPPORT / OPEN

## Objective
Test whether the abstract structural search and physical observations converge on the same pattern without using the physical name during structural extraction.

## Abstract side
A 5-node connected-graph Boolean threshold model was used as a minimal dynamical control. For every connected labeled graph (728 total), synchronous threshold dynamics were constructed using node-local majority-like thresholds. Attractors were enumerated over all 32 states.

Result:
- 728/728 graphs had at least two fixed-point attractors under this particular threshold convention.
- 548/728 had exactly two fixed-point attractors.

This establishes that bistability-like behavior is easy to generate in this toy model, but it also exposes a confound: the chosen threshold rule makes all-zero/all-one fixed states common. Therefore this is NOT evidence for a fundamental entity.

## Reverse physical abstraction
Independent physical literature was used only after defining the abstract signature:

`two distinguishable stable states + externally controlled switching + hysteresis/threshold behavior`

Examples found include:
- elasto-magnetic bistable dynamics with mechanical memory (Nature Communications, 2026);
- bistable superlattice switching with non-volatile memory in monolayer TaIrTe4 (Nature, 2026);
- bistable mechanical/architected lattice structures with reversible state changes and healing (NPG Asia Materials, 2020);
- bistable ferroic/nuclear-polarization and Josephson-junction systems.

These sources independently exhibit the same broad abstract signature, but they are physically different systems. Therefore the signature is a cross-domain pattern, not an identification of one physical entity.

## Convergence result
`Ω → {stable states, switching, persistence}`

and

`Physics → observations → {stable states, switching, persistence}`

converge at the level of a coarse structural/functional signature.

## Important negative result
The current convergence is too coarse to claim ontology. Many unrelated physical systems share bistability. A stronger correspondence must compare richer invariants:

- number and topology of stable states;
- basin structure;
- transition graph;
- threshold/hysteresis geometry;
- perturbation response;
- recovery law;
- composability;
- scaling relations.

## Decision
SUPPORTED as a proof-of-method / pattern-convergence observation.
NOT_PROVEN as a physical entity derivation.

## Next experiment
Construct a richer anonymous physical signature from published data for 3–5 systems, then ask the Ω search to reconstruct candidate structures without names. Compare transition graphs and invariants against the physical signatures using blinded matching and null permutations.

## Sources
- Nature Communications (2026), elasto-magnetic instabilities and mechanical memory.
- Nature (2026), bistable superlattice switching in TaIrTe4.
- NPG Asia Materials (2020), healable, memorizable and transformable lattice structures.
- Physical Review B, bistable Josephson-junction array resonator.
