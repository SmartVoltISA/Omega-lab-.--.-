# Ω-REL-005 / Ω-REL-006 — Interaction of Relations

Date: 2026-08-13
Status: EXPLORATORY RESULT / NOT HISTORICAL EDGE-ONLY REPRODUCTION

## Question

Can interaction between relations itself redistribute relation weight and produce a non-uniform relational structure without an explicit decay term?

## REL-005 model

- 12 elements used as indices for relation endpoints.
- 132 directed relations.
- Initial relation weights random in [0.2, 1.0].
- Outgoing weight from each source normalized to 1.
- At each step, two-step relational support was calculated as `W @ W`.
- A relation was strengthened when its two-step support exceeded the local mean for that source.
- Total outgoing weight was renormalized to 1.
- No explicit decay term.
- Seed 42.
- 300 steps.

### REL-005 result

Execution completed.

Final values:
- mean entropy per source: 0.658951
- strongest relation: 0.896465
- reciprocity: 0.015327

The final matrix was strongly non-uniform. Several relation channels became much stronger than others. The result therefore demonstrates that this particular local two-step interaction rule can redistribute initially distributed relation weight into a structured/non-uniform relation pattern without explicit decay.

This is NOT evidence that the same mechanism is fundamental to Ω or nature. The rule itself contains a positive-feedback assumption and therefore must be treated as a candidate mechanism, not a discovery.

## REL-006 robustness sweep

20 independent seeds for each coupling value; 300 steps each.

| coupling | mean entropy ± SD | max relation ± SD | strong relations (>=0.10) ± SD |
|---:|---:|---:|---:|
| 0.05 | 2.2989 ± 0.0447 | 0.2057 ± 0.0445 | 49.10 ± 5.29 |
| 0.10 | 1.8142 ± 0.2541 | 0.4817 ± 0.1268 | 31.15 ± 8.30 |
| 0.20 | 0.7518 ± 0.0881 | 0.8106 ± 0.1064 | 23.90 ± 3.16 |
| 0.25 | 0.7160 ± 0.1037 | 0.7887 ± 0.1510 | 23.80 ± 3.20 |
| 0.40 | 0.7641 ± 0.1604 | 0.7021 ± 0.2019 | 26.05 ± 4.64 |

### Interpretation

A clear regime change appears between weak interaction (0.05–0.10) and stronger interaction (around 0.20–0.40): stronger interaction generally produces lower relational entropy and larger dominant relations.

The effect is not monotonic at the highest tested coupling, so no claim of a universal threshold is made.

## Critical limitation

The two-step support rule explicitly rewards relations that participate in strong two-step paths. Therefore the emergence of non-uniform structure is not spontaneous from an unspecified relation ontology; it is a consequence of the candidate interaction rule. The experiment establishes that the rule is capable of producing the behavior, not that Ω requires it.

## Relation to collapse/attractor hypothesis

The result suggests a useful next measurement: distinguish concentration from collapse. A low-entropy relation matrix is not automatically a collapse. We must check whether multiple distinguishable relation configurations remain and whether the state continues evolving, settles, or loses all relational differentiation.

## Next test

Compare three controls under identical initialization and metrics:

1. no relation interaction;
2. one-step local interaction;
3. two-step relational interaction.

Then inspect whether stable structure appears only when relation-to-relation interaction is present.

No physical interpretation is claimed.
