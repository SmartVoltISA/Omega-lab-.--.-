# Ω-MEM-4 — Expressiveness × Structural Match

**Date:** 2026-08-10  
**Status:** 🟡 EXPLORATORY / NEEDS CORRECTED REPLICATION

## Purpose

Test whether the failure observed in Ω-MEM-3 is caused by insufficient expressive capacity, incorrect structural matching, or both.

## Archived artifacts

- `PROTOCOL.md` — pre-registered protocol.
- `omega_mem4_submitted.py` — original submitted implementation, preserved as historical evidence.
- `AUDIT_MEM4_2026-08-10.md` — methodological and code audit.

The original run produced useful exploratory observations but did not satisfy the pre-registered protocol completely.

## Key observations

- 🟢 Periodic-4 Counter reaches 1.000 at S=4.
- 🟢 Random-iid remains approximately 0.50.
- 🟢 The submitted Thue-Morse parity tracker fails to predict reliably.
- 🟢 Context-based representations predict Thue-Morse substantially better than that parity tracker.
- 🟡 Random finite-state machines improve with state count on structured data.
- 🟡 The discretized HMM belief implementation does not beat last-observation context in the reported accuracy.

## Critical audit findings

- Context-2 is incorrectly implemented and effectively stores one symbol.
- P3 Matched is forcibly fixed at S=2; therefore its S sweep is not real.
- P3 Matched is not a true online position/carry representation of Thue-Morse.
- Random S=64 vs Matched S=2 is not a controlled same-capacity comparison.
- The reported Periodic-4 intervention effect is inconsistent with reset_step=500 and a period-4 counter.
- Required raw data, confidence intervals, paired contrasts and several protocol metrics are missing from the submitted run.

## Scientific status

H-MEM-2.2 is **REFINED / NEEDS_RETEST**, not confirmed by this run.

H-MEM-2.3 is **OPEN**.

## Next experiment

### Ω-MEM-4R — Corrected capacity × structural-match replication

Primary question:

> At equal effective capacity, does a correctly matched representation outperform an equally expressive structurally mismatched representation on the same process?

Required controls:

1. Correct Context-k implementations.
2. True same-S comparisons.
3. Actual matched capacity sweep for Thue-Morse.
4. Explicit online position/carry representations for Thue-Morse.
5. Multiple random FSMs per condition.
6. Paired seed-level differences and 95% CIs.
7. Full raw per-seed data.
8. Correct strict intervention and reconvergence metrics.
9. Conditional + unconditional entropy and effective-state metrics.
10. No unsupported complexity claim such as O(log n).

Only after this replication should the project decide whether H-MEM-2.3 is strengthened, weakened, or rejected.
