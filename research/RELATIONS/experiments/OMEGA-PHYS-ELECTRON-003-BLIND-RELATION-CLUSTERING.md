# Ω-PHYS-ELECTRON-003 — Blind relation-first particle clustering pilot

Date: 2026-08-16
Status: PILOT COMPLETED / SUPPORTIVE BUT NOT CONFIRMATORY

## Question

Can a relation-first encoding of experimentally established particle properties recover broad physical families without supplying particle labels to the clustering algorithm?

## Important limitation

This is a pilot, not a discovery experiment. The relation features include known Standard Model interaction categories (electromagnetic, weak, strong, colour) and therefore encode real physical structure already known to physics. Recovering particle families from these features cannot by itself establish Ω as a new physical theory.

The meaningful test is whether a relation-first representation adds predictive/compressive value beyond conventional feature representations.

## Dataset

A small reference set of 15 established Standard Model particles was encoded anonymously as A–O before clustering:

- charged leptons: e, μ, τ
- one representative neutrino state
- six quarks: u, d, s, c, b, t
- gluon
- photon
- W boson
- Z boson
- Higgs boson

The labels were retained separately for evaluation only and were not supplied to the unsupervised clustering algorithm.

Input relation/observable fields:

- mass scale;
- electric charge;
- spin;
- colour relation;
- electromagnetic coupling relation;
- weak coupling relation;
- strong coupling relation.

Mass was transformed to log10(mass + 10^-6) to avoid numerical domination by the top-quark scale.

## Blind procedure

1. Remove particle names from the input table.
2. Encode each particle only by observable/property relations.
3. Standardize features.
4. Run unsupervised K-means clustering.
5. Compare resulting anonymous clusters with the known families only AFTER clustering.
6. Repeat over 50 random initializations.
7. Repeat under small perturbations of continuous mass/charge inputs to test cluster stability.
8. Compare against weaker baselines using mass alone and mass+charge+spin.

No particle-family labels were used during fitting.

## Results

### Relation representation

For k = 5 clusters:

- adjusted Rand index (ARI) against known broad families: 0.9383;
- ARI standard deviation across 50 K-means initializations: 0;
- mean silhouette score: 0.4427.

For k = 6:

- ARI: 0.9685;
- silhouette: 0.4189.

For k = 7:

- ARI: 1.0000.

The k = 7 result must NOT be treated as confirmation because increasing k can overfit a small dataset.

### Baselines

Mass alone:

- ARI ≈ 0.0072.

Mass + charge + spin:

- ARI ≈ 0.3602.

Thus the interaction/colour relation fields carry substantially more information about broad Standard Model families than mass alone or the simple mass+charge+spin baseline in this deliberately small pilot.

### Stability

With 2% log-scale perturbations of mass and small perturbations of charge, the k = 6 clustering was stable across 200 perturbation runs in the implemented test; pairwise ARI among the resulting clusterings was 1.0.

## What the clustering recovered

The anonymous encoding grouped:

- the three charged leptons together;
- the six quarks together;
- the gluon separately from the quark cluster;
- the photon separately;
- W and Z together;
- the neutral weak-only neutrino/Higgs pair together in the k = 5 solution, with the Higgs separated when k was increased.

This is physically sensible because the encoding explicitly contains the relevant interaction relations.

## Interpretation

Positive result:

A relation-rich representation can recover meaningful broad particle families without providing particle names to the clustering algorithm.

But this is NOT yet evidence for a new Ω law.

Why not:

1. The relation fields were derived from established Standard Model knowledge.
2. The dataset is tiny (15 objects).
3. The number of clusters is selected externally.
4. The clustering task is unsupervised but the feature construction is not theory-free.
5. The result is descriptive rather than predictive.
6. No held-out experimental observable was predicted.

Therefore the correct status is SUPPORTIVE FOR REPRESENTATION, NOT CONFIRMATORY FOR ONTOLOGY.

## Stronger control required

The next experiment must prevent the relation representation from simply restating known particle categories.

Required design:

- use independently measured observables/processes not used to construct the relation graph;
- construct relations from one subset of observations;
- test predictions on held-out observations;
- compare Ω relation representation with standard numerical and graph baselines;
- preregister target metrics;
- include shuffled/null relation controls;
- evaluate on additional particles and interaction processes;
- keep labels hidden until final evaluation.

A successful result would require Ω to predict held-out structure better than appropriate baselines, not merely cluster known particles correctly.

## Verdict

**Blind clustering pilot: SUCCESSFUL.**

**Relation representation: shows strong descriptive structure.**

**Baseline comparison: relation fields outperform mass-only and mass+charge+spin in this pilot.**

**Ω as new physical ontology: NOT CONFIRMED.**

**Next target: blind held-out prediction.**

## External reference

Particle Data Group 2026 lists the relevant Standard Model particle families, including charged leptons, neutrinos, quarks, gauge bosons and the Higgs boson:

https://pdg.lbl.gov/2026/listings/particle_properties.html

NIST CODATA 2022 provides the electron reference constants used elsewhere in this series:

https://physics.nist.gov/constants
