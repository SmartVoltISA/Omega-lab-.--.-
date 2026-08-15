# Ω-PHYS-ELECTRON-004 — Blinded held-out relation test and null control

Date: 2026-08-16
Status: COMPLETED PILOT / NEGATIVE FOR NOVEL PREDICTIVE EVIDENCE

## Purpose

Test the stronger Ω claim: can a relation-first representation produce predictive structure beyond merely restating known particle categories?

## External physics basis

The particle roster is taken from the established Standard Model particle families listed by the Particle Data Group (PDG 2026): charged leptons, neutrinos, quarks, gauge bosons and Higgs. The experiment uses only broad, experimentally established relation/interaction categories and does not use particle names during clustering. PDG 2026 is the external reference for the roster.

## Critical correction to Ω-PHYS-ELECTRON-003

The earlier 003 record reported an ARI of 0.9383 at k=5 and 0.9685 at k=6. A clean re-run using the explicitly described relation-only encoding exposed a reproducibility problem: the earlier record mixed feature definitions and a different small roster. Therefore those numerical values are RETIRED and must not be cited as verified results.

The 003 experiment remains in the archive as historical provenance, but this experiment is the corrected test.

## Dataset

17 anonymous objects representing:

- 3 charged leptons;
- 3 neutrino states;
- 6 quarks;
- photon;
- gluon;
- W boson;
- Z boson;
- Higgs boson.

Labels were retained only for final evaluation and were never supplied to clustering.

## Relation encoding

Nine binary structural fields were used:

1. electromagnetic interaction;
2. weak interaction;
3. strong interaction;
4. Higgs/Yukawa mass-generation relation;
5. gravitational/energy-momentum relation;
6. electric charge relation;
7. fermionic statistics;
8. spin-1 bosonic structure;
9. colour relation.

This is deliberately a relation-level encoding rather than a mass-based encoding.

## Important epistemic limitation

Several fields are already Standard Model concepts. Therefore the experiment cannot establish that Ω discovered these structures. It tests only whether a relation-first representation recovers broad families and whether that representation survives null controls.

## Test A — unsupervised clustering

Agglomerative clustering with Hamming distance and average linkage was applied to the anonymous relation vectors.

Observed adjusted Rand index against the known broad-family labels:

- k=2: ARI = 0.128
- k=3: ARI = 0.505
- k=4: ARI = 0.458
- k=5: ARI = 0.536
- k=6: ARI = 0.511
- k=7: ARI = 0.826

Silhouette scores respectively:

- k=2: 0.482
- k=3: 0.614
- k=4: 0.585
- k=5: 0.666
- k=6: 0.654
- k=7: 0.765

The best family-alignment value in this test was k=7, ARI=0.826. This is descriptive and not a discovery result.

## Test B — label permutation null

The relation vectors were kept fixed while family labels were randomly permuted 5,000 times.

For k=7:

- observed ARI = 0.82615;
- null mean ARI ≈ 0.00098;
- null standard deviation ≈ 0.0864;
- empirical permutation p ≈ 0.00020 for ARI >= observed.

This establishes that the observed relation structure is not explained by a random assignment of family labels.

However, this is NOT a test against the Standard Model. The relation fields themselves encode Standard Model structure.

## Test C — leave-one-out nearest-neighbour prediction

A nearest-neighbour classifier using only the relation vectors was evaluated with leave-one-out cross-validation against the broad-family labels.

Accuracy:

- k=1: 15/17 = 88.2%
- k=2: 16/17 = 94.1%
- k=3: 16/17 = 94.1%

Again, this is descriptive because the relation encoding contains family-defining information.

## Why this is not the breakthrough we wanted

The strongest claim was supposed to be predictive:

> construct relations from observations A, hide independent observations B, and predict B before seeing B.

The present pilot does not satisfy that requirement because the relation categories are supplied from established theory and are not inferred from raw experimental processes.

Therefore:

- descriptive structure: YES;
- non-random relation/family association: YES;
- predictive new observable: NO;
- evidence for new physical law: NO;
- evidence that Ω ontology is fundamental: NO.

## Falsification result

The experiment was intended to break the Ω claim if relation-first encoding did not outperform meaningful controls. It succeeded in breaking the stronger version of the claim: **the current relation representation does not demonstrate predictive power beyond known physics.**

The relation representation is useful as an analytical language, but the present evidence does not justify calling it a new physical ontology.

## Next experiment required

A genuinely stronger test must start from measured process data rather than from named Standard Model relation categories.

Protocol:

1. choose a set of measured scattering/decay/transition observables;
2. hide the target observable;
3. construct the relation graph only from the remaining observations;
4. generate a preregistered prediction for the hidden observable;
5. compare against Standard Model calculation and a non-relational statistical baseline;
6. repeat on held-out processes;
7. include shuffled and synthetic-null controls.

Only an out-of-sample prediction that survives these controls can count as evidence that Ω adds predictive information.

## Verdict

**Ω-PHYS-ELECTRON-004: COMPLETED.**

**Relation structure: real and non-random.**

**Predictive novelty: not demonstrated.**

**Strong Ω ontological claim: not supported.**

**Falsification status: stronger claim weakened/broken.**

This is a valid negative result and should be preserved rather than discarded.

## External references

- PDG 2026 particle properties: https://pdg.lbl.gov/2026/listings/particle_properties.html
- NIST CODATA fundamental constants: https://physics.nist.gov/constants
