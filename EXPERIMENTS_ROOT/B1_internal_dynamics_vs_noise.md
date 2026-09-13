# Ω-B1 — Internal dynamics vs matched white noise

## Question

Does structured internal dynamics produce statistics that differ from white noise with matched variance?

## Reported setup

The reported control run used matched variance for the internal forcing. Exact source code and seed set are not yet archived in this repository.

Therefore the numerical results below are **preliminary reported results**, not yet independently reproducible results.

## Reported results

| Metric | Internal chaos `v` | Matched white noise | Ratio |
|---|---:|---:|---:|
| Number of domains | 23 | 101 | 0.23× |
| Mean lifetime | 644 steps | 181 steps | 3.6× |
| Mean domain size | 8.7 | 2.0 | 4.4× |
| Birth rate | 0.049 | 0.221 | 0.22× |

The reported run therefore shows substantially larger and longer-lived domains under the internal dynamics than under matched white noise.

## Interpretation

This does **not** establish “will”. It establishes a narrower candidate effect:

> The particular internal dynamics used in the model may contain temporal and/or spatial correlations that produce statistics different from independent white noise of the same variance.

## Important caveat

A difference between chaos and white noise can have many explanations:

- temporal autocorrelation;
- spatial correlation;
- non-Gaussian amplitude distribution;
- finite-size effects;
- nonlinear coupling to the field;
- implementation details.

The next control must separate these possibilities.

## Required replication

Run at least 100 independent seeds for each condition while fixing:

- `N`;
- `T`;
- initial-condition distribution;
- diffusion parameters;
- nonlinear parameters;
- forcing variance;
- boundary conditions.

Report mean, standard deviation, confidence intervals and effect sizes.

## Classification

**C — potentially interesting, requires replication and mechanistic controls.**
