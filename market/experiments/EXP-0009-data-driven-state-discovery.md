# EXP-0009 — Data-driven state discovery, first pass

**Date:** 2026-08-14
**Instrument:** BTCUSDT spot
**Source:** Binance spot klines
**Primary interval:** 1h
**Sample:** 1000 most recent 1h bars for the first pass; a 100-bar recent slice was separately inspected for concrete regime examples.

## Objective

Test whether candidate market states can be derived from observable variables rather than imposed visually as S0–S5.

## Inputs allowed for current-state construction

- close-to-close return `r_t = C_t/C_(t-1)-1`
- intrabar range normalized by price `(H_t-L_t)/C_(t-1)`
- volume
- volume relative to a rolling baseline
- candle body/range relationship

Future return is **not** used to construct the current state. It is reserved for validation.

## First-pass normalization concept

Use rolling, causal baselines rather than fixed dollar thresholds:

- `z_return` = current return relative to recent return scale
- `z_range` = current range relative to recent range scale
- `z_volume` = current volume relative to recent volume scale
- `body_fraction` = `abs(C-O)/(H-L)`
- `close_location` = `(C-L)/(H-L)`

The exact window and clustering method are intentionally not frozen yet; this file records the discovery stage rather than a final classifier.

## Direct observations from the real sample

The 1h Binance sample contains clearly separated observable regimes:

1. **Low-range / low-activity compression:** repeated narrow candles around stable price zones with comparatively small volumes.
2. **Large displacement / impact:** bars with unusually large range and volume, e.g. observed bars around the 61.7k–63.5k area and later around 64.0k–65.6k.
3. **Continuation:** sequences where several consecutive bars maintain a directional displacement after an impact.
4. **Absorption candidate:** large intrabar displacement with a close returning toward the opening/previous balance zone, followed by smaller opposing movement. A concrete example in the sample is the bar opening around 63,420, reaching ~62,802 and closing near 63,160, followed by recovery toward ~63,408.
5. **Recovery:** post-impact movement returning toward a prior local balance without immediately restoring the previous extreme.
6. **New compression:** after a displacement/recovery sequence, activity and range contract again around a new price region.

These are observations from the data; the labels are provisional interpretations.

## Important finding

The raw variables appear capable of separating visually different regimes without requiring a price-level rule such as "BTC below X = state Y". This supports proceeding to quantitative state discovery.

However, this is **not yet evidence that S0–S5 are the correct states**. The next step must derive clusters/states mechanically and then compare them with the provisional labels.

## Proposed mechanical discovery test

1. Build the causal feature vector from each bar.
2. Standardize features using only the training segment.
3. Discover a small number of clusters (initially k=4, 5, 6, 7 as a sensitivity sweep).
4. Map each cluster to descriptive statistics only after clustering.
5. Build the transition matrix between discovered clusters.
6. Measure persistence (self-transition probability and run length).
7. For each state and transition, evaluate future returns/volatility at H=1, 2, 3, 6, 12 and 24 hours.
8. Repeat on a chronologically later holdout segment.
9. Compare against a null/surrogate sequence with temporal structure destroyed.

## Falsification criteria

The candidate state model is considered unsupported if:

- cluster identities are unstable under small parameter changes;
- transition structure disappears out of sample;
- future distributions are indistinguishable from the baseline after costs/controls;
- the same effect appears in time-shuffled data;
- apparent performance is explained by leakage or overlapping-window contamination.

## Current status

**DATA-DRIVEN DISCOVERY: IN PROGRESS**

We have completed the real-data inspection and feature specification. We have **not** yet claimed a numerical transition matrix, win rate, or profitability result from this experiment.

The next result must contain actual counts/probabilities generated mechanically from the data, not hand-labelled examples.
