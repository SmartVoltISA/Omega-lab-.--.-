# Ω REL-003 — Weighted Relations Without Explicit Decay

Date: 2026-08-13
Status: EXECUTED — exploratory model, NOT historical edge-only reproduction

## Purpose

Test whether the concentration of relation weights observed in REL-002 survives when the explicit decay term is removed.

## Controlled change

REL-002 used an explicit decay factor `DECAY = 0.985`.
REL-003 sets `DECAY = 1` (removes explicit decay).

Other exploratory parameters were retained:

- seed = 42
- N = 12
- directed relations = 132
- steps = 250
- coupling = 0.08
- noise = 0.015

## Execution result

Execution completed.

Initial mean weight: 0.582708
Final mean weight: 0.613639

Initial top-10% concentration: 0.154767
Final top-10% concentration: 0.110016

Initial total weight: 76.917470
Final total weight: 81.000337

Final spread (standard deviation): 0.041863

## Interpretation

The concentration effect seen in REL-002 did NOT persist after explicit decay was removed. Instead, the top 10% share decreased from 0.154767 to 0.110016 while the mean weight remained around 0.6.

Therefore the earlier observation that relation weight became relatively concentrated cannot be attributed to the redistribution rule alone in these exploratory models. The explicit decay term contributed materially to that behavior.

This is a result of this model only. It is not evidence about the historical Ω edge-only experiment.

## Important conclusion

Do not call this attractor or collapse.

The current model has not yet implemented the historical Ω classification rules for cycle, attractor, or collapse. It only tests relation-weight redistribution.

## Honesty status

`Execution verified for this script.`
`Historical Ω experiment reproduction: NOT PERFORMED.`
