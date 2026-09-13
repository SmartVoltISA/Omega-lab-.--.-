# Ω-MEM-7 — Preliminary Audit

## What was checked

- Memory capacity is fixed at 8 for every B.
- Controlled branching values are exactly 1, 2, 4, 8.
- Current observable state is constant and therefore unchanged by intervention.
- Relevant memory is the latent state that causally selects the next transition.
- Irrelevant memory is independently randomized at the same nominal capacity.
- Reset memory is sampled independently from the B available transition classes.
- Empirical distinct next transitions equal the requested B in every condition.
- 30 seeds and 80,000 transitions per seed were used.

## Interpretation boundary

The result is a controlled computational demonstration, not evidence that all physical systems implement memory in this form. The relevant-memory construction contains direct information about the next transition by design.

## Required next audit

1. Independent reimplementation from the frozen protocol.
2. Verify raw per-seed outputs and no hidden dependence on B beyond the intended generator.
3. Add a non-trivial dynamical generator where memory is not a direct copy of the next symbol.
4. Verify intervention causality under matched current-state distributions.
5. Only then consider promotion from PRELIMINARY to FINAL.
