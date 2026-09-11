# Ω-Test-4 — Interaction-sensitive invariant

**Experiment ID:** Ω-TEST-4-OPPOSING-INTERACTION-2026-09-12  
**Date:** 2026-09-12  
**Time:** 02:51 (UTC+05:00, run timestamp)  
**Status:** COMPLETED / EXPLORATORY NUMERICAL TEST  

## Question

Can a statistic distinguish a response associated with two opposing components from a phase-scrambled null while preserving marginal spectral structure?

## Model

```text
dx/dt = I - E - γx - cxy
dy/dt = E - I - γy - cxy
```

with `γ=0.8`, `c=0.6`.

Candidate statistic:

```text
J = <(I-E) xdot> / (σ(I-E) σ(xdot))
```

## Null

200 phase-randomized surrogates of `E` were generated. This preserves the Fourier amplitude spectrum while disrupting phase relation with `I`.

Observed:

```text
J = 0.657818
surrogate mean = 0.645334
surrogate SD = 0.036990
z = 0.337504
empirical two-sided p = 0.731343
```

Uncoupled model with the same drives:

```text
J_uncoupled = 0.682158
```

## Interpretation

The proposed statistic **did not significantly distinguish the full model from the phase-scrambled null** (`p≈0.73`). It therefore fails this version of the interaction-detection test.

The fact that the uncoupled model produces a similar or larger value is another warning: the statistic is not specific enough to identify opposing interaction.

## Classification

**REJECTED as a validated interaction invariant.**

Retained as a failed experiment because the failure is scientifically informative.

## What was learned

1. A statistic can correlate with boundary motion without measuring opposition.
2. Matching marginal spectral structure is not sufficient if the statistic is insensitive to the causal/interaction structure.
3. The `+1/-1` opposition must be detected through a property that disappears or changes predictably under a properly matched interaction null.
4. The candidate `J` must not be promoted to a foundational Ω invariant.

## Next test

Build a deliberately known interaction model and a matched null where the interaction term is removed while all external drive statistics are held fixed. Search for an observable based on **conditional dependence / response asymmetry**, not simple correlation with boundary velocity.

## Provenance

Local numerical outputs retained separately:
- `omega_test4_interaction_report.md`
- `omega_test4_interaction_results.csv`
- `omega_test4_surrogate_scores.csv`

**Canonical rule:** failed and rejected experiments remain part of the research history.
