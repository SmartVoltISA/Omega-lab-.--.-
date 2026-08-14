# Ω-MARKET-1 — Experimental Market Horizon Lab

## Purpose

Ω-MARKET-1 is a research branch derived from Ω-LINK-1 for testing whether the concepts of state, distinguishability, minimal future horizon, memory, and multi-scale influence can be measured on real market data.

This is a research system first. It is not a trading bot yet.

## Core question

Can a market's observable state be characterized by the **minimal future horizon H** at which alternative current states become statistically distinguishable?

We will test both directions:

- large horizon → small horizon;
- small horizon → large horizon.

The goal is to determine whether information propagates across scales in a measurable and repeatable way.

## Initial data layers

1. Price / returns.
2. Volume and volatility.
3. Order-flow or order-book features where reliable data is available.
4. News/event timestamps and sentiment only after the market-only baseline is established.
5. Macro / sector variables for longer horizons.

## Principle

Do not begin with a prediction target such as "price goes up".

First measure:

`H_market(t) = minimal horizon at which competing future regimes become distinguishable.`

Then test whether changes in `H_market` contain out-of-sample information about subsequent returns, volatility, regime changes, or transition probabilities.

## Experimental order

1. Build market-only baseline.
2. Define states without future leakage.
3. Measure minimal horizon.
4. Test scale directionality.
5. Add volume/volatility.
6. Add order flow.
7. Add news/events.
8. Perform strict out-of-sample validation.
9. Include fees, spread, slippage, latency and turnover.
10. Paper trading.
11. Only after robustness is demonstrated: evaluate a live execution system.

## Non-negotiable research rules

- No future information in features.
- No random train/test leakage across overlapping windows.
- Every discovered rule must be tested on unseen data.
- Transaction costs are part of the experiment, not an afterthought.
- No claim of profitability from backtest alone.
- Preserve negative results.
- Separate scientific measurement from trading execution.

## Relationship to Ω-LINK-1

Ω-LINK-1 provides the conceptual and computational primitives:

- state;
- internal distinguishability;
- minimal sufficient state;
- memory depth;
- future divergence;
- minimal horizon;
- explicit recording of methodological failures.

Ω-MARKET-1 applies those primitives to empirical time-series data without assuming that the market must obey the laboratory's synthetic laws.
