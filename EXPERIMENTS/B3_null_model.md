# Ω-B3 — Null model for domain births

## Question

Are domain births genuinely concentrated near the transition region `u ≈ 0`, or is this concentration an artifact of how sign changes and births are defined?

## Reported result

The reported analysis compared the observed dynamics with a spatially shuffled null model.

| Metric | Real dynamics | Null model |
|---|---:|---:|
| Domain births | 73 | 16,147 ± 45 |
| Births near `u = 0` | 100% | 2.7% ± 0.1% |

The reported difference is large.

## Important methodological caveat

The null model produced a very different total number of births. Therefore the comparison of 100% versus 2.7% is **not yet a fully matched null test**. The randomization changes more than spatial organization: it also changes the event-generation process.

The result is therefore classified as **promising but not final**.

## Stronger null model required

Preserve the observed number of births exactly (for the reported run, 73) and preserve their temporal distribution and relevant domain-size distribution where possible. Randomize only their spatial locations.

Then calculate the expected fraction of births falling inside the transition region.

The test should report:

- observed fraction;
- null mean;
- null standard deviation;
- empirical p-value;
- effect size;
- confidence interval.

## Interpretation

If the effect survives the matched null model, the safe conclusion is:

> Domain-birth events are spatially associated with the transition region more strongly than expected under the specified null model.

This still does **not** demonstrate agency, will, or new physics.

## Classification

**C — potentially interesting; stronger null model required.**
