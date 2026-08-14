# Ω-MARKET-1 — Research Protocol v0.1

## Objective

Test whether a measurable minimal future horizon can be extracted from market time series and whether that horizon carries information across time scales.

## Phase A — Market-only baseline

Start with one liquid instrument and historical OHLCV data. No news, no external labels, no execution.

### Candidate horizons

Use nested horizons, for example:

- 1 minute
- 5 minutes
- 15 minutes
- 1 hour
- 4 hours
- 1 day

The exact set is data-dependent and must be frozen before evaluation.

### State construction

Construct the current state only from information available at time t:

- returns over fixed lookback windows;
- realized volatility;
- volume relative to its own history;
- range / trend descriptors;
- optional market microstructure features when available.

No future-derived normalization, labels, thresholds, or feature selection.

### Distinguishability test

For pairs or clusters of current states that are observationally similar at time t, compare their future trajectories at each candidate horizon H.

Define the first horizon at which the futures become statistically distinguishable under a pre-registered criterion.

Record:

- state representation;
- horizon H;
- sample count;
- effect size;
- confidence interval;
- multiple-testing correction where applicable;
- train/test period;
- transaction-cost assumptions for any downstream trading test.

## Phase B — Directionality

Test both:

1. large horizon features predicting small-horizon transitions;
2. small-horizon transitions aggregating into large-horizon regime changes.

Do not assume causality from predictive lead-lag structure.

## Phase C — Information layers

Add one layer at a time:

1. price/return;
2. volume/volatility;
3. order flow/order book;
4. news/events;
5. macro/sector context.

Each added layer must beat the frozen baseline out of sample to justify inclusion.

## Phase D — Trading relevance

Only after predictive stability is established:

- define an executable signal;
- model spread, fees, slippage and latency;
- cap turnover;
- use walk-forward validation;
- maintain untouched final test data;
- run paper trading before live execution.

## Bot architecture target

The eventual bot should be separated into four layers:

`DATA → STATE/HORIZON ENGINE → SIGNAL/RISK → EXECUTION`

The research engine must remain usable without the execution layer.

## Scientific rule

A profitable-looking result that disappears after realistic costs, unseen-data testing, or regime changes is a negative result and must be preserved as such.
