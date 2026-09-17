# PHYSICAL CORRESPONDENCE & GOAL-DIRECTED SEARCH v1.0

Ω-Lab may automatically compare discovered structural candidates with known physical patterns using structural fingerprints rather than names.

\[
\text{candidate}\rightarrow\text{fingerprint}\rightarrow\text{known-pattern comparison}
\]

Fingerprint components may include boundary/interface, internal relations, invariants, persistence, transformations, interactions, composability, and response patterns.

Statuses:
- `KNOWN_CORRESPONDENCE`
- `PARTIAL_CORRESPONDENCE`
- `CANDIDATE_CORRESPONDENCE`
- `NO_KNOWN_CORRESPONDENCE`
- `NEW_HYPOTHESIS`

`NO_KNOWN_CORRESPONDENCE` does not mean non-existence. `STRUCTURAL MATCH` does not mean physical identity.

## Goal-directed search

Ω-Lab may also search for structures capable of satisfying a predefined goal:

\[
GOAL\rightarrow REQUIRED\ BEHAVIOR\rightarrow STRUCTURAL\ CONSTRAINTS\rightarrow SEARCH\rightarrow TEST
\]

The goal defines the criterion, not the desired answer. Objective metrics, constraints, baseline/null, admissible transformations, and rejection criteria must be fixed before execution.

Examples include searching for structures that preserve an invariant under perturbation, transport changes across a boundary, maximize propagation/coupling/recovery, or minimize a declared transformation cost.

Two modes are therefore supported:

1. **Discovery:** relations → entities → properties → laws → physical correspondence.
2. **Goal-directed:** goal → required properties → structural search → candidate → test → physical correspondence.

Both modes retain preregistration, controls, provenance, falsification, and epistemic status discipline.
