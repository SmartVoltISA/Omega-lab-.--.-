# Ω-Lab — EXP-004 Dynamic Boundary Emergence — 2026-10-08

## Status

EXECUTED / TOY RESULT / CANDIDATE POSITIVE

## Question

Can a boundary be recovered from relational dynamics without giving the learner the boundary labels?

## Important limitation

The data generator contains a hidden two-module structure. The learner does NOT receive those labels, but the experiment therefore tests **emergence/recovery of a latent relational boundary**, not creation of a boundary from an ontologically structureless universe.

## Setup

- 12 states
- hidden modules: 6 + 6 (labels withheld from learner)
- 8,000 observed transitions for learning
- 3,000 held-out transitions for evaluation
- 30 independent seeds
- transition probability within hidden module: 80% in the main robustness condition
- transition probability across modules: 20%
- learner sees only transition counts

## Boundary learner

1. Estimate each state's outgoing transition distribution.
2. Compare states by cosine similarity of their transition distributions.
3. Build a similarity matrix.
4. Compute the second eigenvector of the graph Laplacian.
5. Split states by the median of that eigenvector.

No hidden module labels are used during learning.

## Main result

For the main condition (cross-module transition probability = 20%):

- F1 against hidden boundary: **1.000 ± 0.000**
- cut conductance: **0.3608 ± 0.0066**
- held-out within-predicted-group transition rate: **0.7974 ± 0.0089**

## Robustness sweep

Cross-module transition probability:

| Cross-module probability | F1 | Conductance | Held-out within-group rate |
|---:|---:|---:|---:|
| 0.10 | 1.000 ± 0.000 | 0.2082 ± 0.0069 | 0.8993 ± 0.0057 |
| 0.20 | 1.000 ± 0.000 | 0.3608 ± 0.0066 | 0.7974 ± 0.0089 |
| 0.30 | 1.000 ± 0.000 | 0.4657 ± 0.0046 | 0.6986 ± 0.0080 |
| 0.40 | 1.000 ± 0.000 | 0.5262 ± 0.0026 | 0.5986 ± 0.0092 |
| 0.45 | 1.000 ± 0.000 | 0.5410 ± 0.0012 | 0.5503 ± 0.0080 |

## Interpretation

Positive toy result:

A relational boundary can be recovered from transition dynamics alone when the underlying dynamics contain a persistent separation of regimes.

The boundary was not supplied to the learner as labels.

However, this does NOT establish that the boundary is fundamental. The hidden generator already contained two dynamical regimes.

Therefore the correct claim is:

> **Boundary is recoverable as a property of relational dynamics in this toy model.**

Not:

> **Boundary is proven to be fundamental.**

## Stronger next test

Remove the explicit 6+6 modular generator.

Generate a growing relational system with no predefined modules, then ask whether persistent predictive/causal separation appears spontaneously and remains stable under perturbation.

Required controls:
- shuffled transition control;
- Erdős–Rényi/randomized-transition null;
- degree-preserving rewiring;
- capacity-matched clustering;
- held-out perturbation/recovery test.

## Decision

Do not promote BOUNDARY to confirmed foundation.

Promote it from **OPEN** to **SUPPORTED TOY MECHANISM / NEEDS STRONGER NULLS**.

