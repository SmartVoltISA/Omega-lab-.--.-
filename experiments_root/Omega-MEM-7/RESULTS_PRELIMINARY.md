# Ω-MEM-7 — Preliminary Execution Results

**Status:** PRELIMINARY / executed locally; not final audited result
**N:** 80,000 transitions per condition
**Seeds:** 30
**Memory capacity:** fixed at 8 states for all B
**Branching:** B = 1, 2, 4, 8

## Aggregate results

| B | H(next | current) | H(next | current,memory) | H(next | current,random memory) | I(next;memory | current) | distinct next transitions | fraction changed after reset |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1 | 0.0000 |
| 2 | 0.5436 | 0.0000 | 0.5434 | 0.5436 | 2 | 0.4999 |
| 4 | 1.3568 | 0.0000 | 1.3565 | 1.3568 | 4 | 0.7497 |
| 8 | 2.4036 | 0.0000 | 2.4032 | 2.4036 | 8 | 0.8749 |

## Immediate observations

1. With fixed memory capacity, increasing controlled branching increases current-state-only next-transition uncertainty.
2. Relevant memory removes that uncertainty in this deterministic construction.
3. Capacity-matched irrelevant memory provides essentially no predictive reduction.
4. The intervention changes the realized next transition frequently while the current observable state remains fixed: approximately 50%, 75%, and 87.5% for B=2,4,8.
5. The empirical number of next-transition alternatives matches the controlled B exactly.

## Important limitation

This construction is intentionally causal and controlled, but it is also simple: the relevant memory directly encodes the next-transition class. Therefore this result demonstrates the mechanism under the specified model; it does not establish a universal law about physical systems.

The marginal transition distribution after memory reset changes because the generator uses a deliberately non-uniform branch occupancy. This prevents a reset from being invisible at the marginal level, while keeping the current observable state fixed.

## Status

The primary Ω-MEM-7 protocol remains the authority. These are preliminary execution results and require independent audit before interpretation or promotion to a final result.
