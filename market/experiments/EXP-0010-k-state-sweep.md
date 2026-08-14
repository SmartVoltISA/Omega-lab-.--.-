# EXP-0010 — K-State Sweep

## Status
Protocol fixed. No trading claim.

## Question
Does an unsupervised state representation of BTCUSDT 1H market observations remain structurally meaningful when the number of states is varied rather than chosen in advance?

## Input
BTCUSDT spot, 1H candles. For each candle derive only normalized, contemporaneous features:
- log return
- high-low range / close
- body / range
- close location within candle range
- volume / rolling median volume
- optional rolling volatility

No future information may enter the feature vector.

## State counts
Run independently for k = 4, 5, 6, 7.

## Validation
For each k:
1. Fit state representation on the training segment only.
2. Assign the unseen test segment using the frozen representation.
3. Build the transition matrix from consecutive states.
4. Measure state occupancy, transition entropy, self-transition rate and mean dwell time.
5. Measure forward returns conditional on current state at H = 1, 2, 3, 6, 12 and 24 hours.
6. Compare with a shuffled-label surrogate preserving the marginal state frequencies.
7. Compare against a simple volatility/return quantile baseline.

## Falsification criteria
A state system is not accepted merely because clusters look visually plausible.
It must show out-of-sample structure that is materially stronger than the surrogate and baseline. If the advantage disappears out of sample, reject the state interpretation.

## Important constraint
Do not rename clusters as S0, S1, etc. until after all statistical tests. Cluster IDs are arbitrary labels.

## Current data observation
The fresh BTCUSDT 1H stream contains visibly different regimes, including compressed low-range periods and high-volume expansion/shock periods. This is an observation for experiment setup, not evidence that the discovered states are predictive.

## Expected output
A compact table for k=4..7 containing:
- occupancy entropy
- transition entropy
- self-transition rate
- mean dwell time
- out-of-sample conditional return by horizon
- surrogate delta
- baseline delta

Decision: RETAIN / REJECT / INCONCLUSIVE.
