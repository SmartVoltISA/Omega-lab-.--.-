# Ω REL-007 — Direct Comparison of Relation Interaction Depth

Date: 2026-08-13
Status: EXPLORATORY RESULT / NOT HISTORICAL REPRODUCTION

## Question

What changes when relation weights interact through no interaction, one-step local competition, or two-step relational paths?

## Controlled setup

- N = 12 elements
- 132 directed relations
- 300 steps
- coupling = 0.25
- seeds = 0..19 (20 runs per mode)
- same initialization distribution and normalization
- outgoing relation weight normalized per source after each update
- no explicit decay

Only the interaction rule was changed.

## Results

| Mode | Mean entropy | Max relation weight | Strong relations (weight >= 0.10) |
|---|---:|---:|---:|
| No interaction | 2.3257 ± 0.0085 | 0.1646 ± 0.0107 | 55.85 ± 2.57 |
| One-step | 0.0000 ± 0.0000 | 1.0000 ± 0.0000 | 12.00 ± 0.00 |
| Two-step | 0.7160 ± 0.1037 | 0.7887 ± 0.1510 | 23.80 ± 3.20 |

## Direct observation

- No interaction preserves a relatively distributed relation field.
- One-step positive feedback drives complete winner-take-all concentration: one outgoing relation per source reaches weight 1.0.
- Two-step interaction produces a structured intermediate regime: strong concentration appears, but it does not collapse completely to one relation per source.

## Important methodological warning

The one-step mode is a deliberately simple local positive-feedback control and therefore its winner-take-all behavior cannot by itself be interpreted as a fundamental Ω result.

The two-step result is also model-dependent. It demonstrates that a specific relation-interaction rule can generate non-uniform structure without an explicit decay term, but does not establish a universal law.

## Current interpretation

The comparison supports a narrower statement:

> In this exploratory relation-only model, the depth/form of interaction between relations materially changes the resulting organization of relation weights.

The next test should separate the effect of interaction depth from the effect of the chosen positive-feedback rule.

## Honesty rule

`Execution verified for this script. Historical Ω reproduction: NOT CLAIMED.`
