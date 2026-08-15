# Ω-PHYS-ELECTRON-004 — Corrected relation-only clustering and null control

Date: 2026-08-16
Status: COMPLETED PILOT / NEGATIVE FOR NOVEL PREDICTIVE EVIDENCE / NUMBERS VERIFIED

## Purpose

Test whether the relation-first representation used in the Ω-Lab electron/particle pilot recovers known particle-family structure and whether the reported result survives an independent rerun.

## Important correction

A full independent rerun of the exact Python protocol stored with this experiment was performed. The original prose record contained incorrect reported values for k=2..6 and for the leave-one-out kNN test. The corrected values below replace those claims. The k=7 ARI and permutation-null values were reproduced exactly.

This correction is preserved rather than hidden because reproducibility is itself a laboratory result.

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

Nine binary structural fields:

1. electromagnetic interaction;
2. weak interaction;
3. strong interaction;
4. Higgs/Yukawa mass-generation relation;
5. gravitational/energy-momentum relation;
6. electric charge relation;
7. fermionic statistics;
8. spin-1 bosonic structure;
9. colour relation.

These fields are already informed by established Standard Model knowledge. Therefore this experiment cannot establish that Ω discovered the categories.

## Exact independent rerun

The exact X matrix and labels in the companion Python file were rerun with scikit-learn using:

- AgglomerativeClustering(metric='hamming', linkage='average');
- adjusted Rand index;
- silhouette score using Hamming distance;
- NumPy RNG seed 42 for the 5,000 permutation null;
- leave-one-out KNN with Hamming distance.

### Correct clustering results

| k | ARI | silhouette |
|---|---:|---:|
| 2 | 0.327141 | 0.526866 |
| 3 | 0.275689 | 0.457619 |
| 4 | 0.692029 | 0.633987 |
| 5 | 0.675985 | 0.611765 |
| 6 | 0.649823 | 0.611765 |
| 7 | 0.826150 | 0.823529 |

The k=7 ARI exactly matches the previous stored value. The other values did not; the earlier prose values were therefore incorrect and are retired.

### Null permutation

For k=7:

- observed ARI = 0.8261504748;
- null mean = 0.0009811541;
- null standard deviation = 0.0864012293;
- empirical p = 0.0001999600 using 5,000 permutations plus-one correction.

These values reproduce the stored result.

### Leave-one-out KNN

Correct exact rerun:

- k=1: 14/17 = 82.35%;
- k=2: 14/17 = 82.35%;
- k=3: 14/17 = 82.35%.

The previously stored 15/17 and 16/17 claims were incorrect and are retired.

## What this actually establishes

1. The exact encoded relation vectors contain non-random structure correlated with the supplied broad-family labels.
2. The k=7 clustering alignment is reproducible.
3. The permutation null gives p≈0.00020 for that descriptive alignment.
4. The relation representation can classify the supplied labels above chance in this tiny dataset.
5. None of this demonstrates predictive new physics, because the relation features themselves were defined from Standard Model concepts.

## What it does NOT establish

It does NOT constitute a true held-out prediction experiment.

No independent experimental observable was hidden and predicted. The labels were withheld from fitting, but the feature definitions already encode known theory categories. Therefore the title 'held-out relation test' is historical shorthand only; the substantive experiment is a corrected relation-only clustering/null-control pilot.

It does NOT establish:

- a new physical law;
- a new particle ontology;
- that particles are literally graph structures;
- that Ω is more fundamental than quantum field theory.

## Falsification status

The stronger Ω claim remains unsupported. The present result is useful only as evidence that a relation-rich representation can encode known physical organization.

The next valid experiment must use measured process data, not predefined interaction labels, and must predict genuinely held-out observables before their values are revealed.

## Verdict

**Exact numerical rerun: VERIFIED.**

**Previous incorrect k=2..6 and KNN values: RETIRED.**

**Relation/family association: REPRODUCIBLE IN THIS SMALL PILOT.**

**Novel predictive evidence: NOT DEMONSTRATED.**

**New physical law: NOT FOUND.**

**Next experiment: genuine held-out process prediction.**

## External reference

PDG 2026 particle properties:
https://pdg.lbl.gov/2026/listings/particle_properties.html
