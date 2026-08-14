# EXP-0011 — Open Interest × Price Divergence

**Date:** 2026-08-14
**Instrument:** BTCUSDT perpetual/futures market data, Binance
**Status:** candidate signal under validation

## Objective

Test whether changes in Open Interest (OI), when combined with price movement, provide more useful information than OI alone.

## Current observation

In the latest synchronized hourly data, OI increased while price weakened. Near the end of the sample:

- OI: approximately 111,394 BTC → 114,144 BTC (+2.47%)
- Price: approximately 62,945 → 62,662 USDT (-0.45%)

This is an **OI↑ / Price↓ divergence**.

The observation does not determine whether shorts or longs dominate. It is therefore treated as a market-state candidate, not a directional signal by itself.

## Historical examples noticed

There are multiple episodes in which OI expands rapidly while price changes little or moves against the recent direction. Some are followed by large expansion; others are followed by OI contraction and price reversal/continuation. This is exactly the population to test rather than selecting examples retrospectively.

## Test definition

For every hourly observation meeting a predefined OI-change threshold, classify:

1. OI ↑ + Price ↑
2. OI ↑ + Price ↓
3. OI ↓ + Price ↑
4. OI ↓ + Price ↓
5. OI change large + Price change small (compression/divergence)

For each event calculate forward price response at:

- H+1
- H+3
- H+6
- H+12
- H+24

Record:

- direction hit rate;
- median forward return;
- mean forward return;
- adverse excursion;
- favorable excursion;
- event count;
- result by market-volatility regime.

## Important control

Compare the OI-conditioned result against a price-only baseline using the same timestamps. A signal is retained only if the OI information provides measurable incremental value.

## Current conclusion

**OI alone is rejected as a directional signal.**

**OI + price divergence remains a candidate and requires a full historical test.**

No trading conclusion is made from the current live observation.

## Next

Run the complete historical event matrix and separate:

- continuation;
- reversal;
- liquidation/unwind candidate;
- neutral/noise.

Then combine only surviving features with the previously tested impulse/response and multiscale state model.
