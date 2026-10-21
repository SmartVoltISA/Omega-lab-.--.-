# Ω-SELF-009 — Experience transfer across structurally analogous tasks

**Status:** Local reference run completed; exploratory pilot.  
**Date:** 2026-10-21

## Question
Can experience in one task be reused in a different task when the underlying causal principle is shared but surface cues differ?

## Design
- Training/source family: `heat`.
- Transfer/test family: `battery`.
- Conditions: no transfer, episode/surface-threshold replay, abstract normalized-risk rule, random intervention rule.
- 250 seeds per family and condition; 180 steps per episode; 500 episodes per condition.
- The same hidden high-risk principle exists in both families, but battery cues have a different scale/offset.
- The abstract-rule condition uses a provided normalization transform. It therefore tests the value of applying an abstract rule, **not** whether the system discovers the abstraction on its own.
- Paired bootstrap intervals: 4,000 resamples, paired by seed within the battery test family.

## Results

| Condition | Heat score | Battery score | Battery violations | Battery final risk |
|---|---:|---:|---:|---:|
| No transfer | 130.014 | 104.213 | 22.056 | 0.732 |
| Episode replay | 129.830 | 129.000 | 0 | 0.282 |
| Abstract rule | 129.830 | **130.099** | 0 | 0.527 |
| Random rule | 101.210 | 100.835 | 1.780 | 0.247 |

Scores are mean per episode. Fractional violations are averages across episodes.

### Paired comparisons on the battery test family

| Comparison (abstract minus baseline) | Score difference, 95% CI | Violations difference, 95% CI |
|---|---:|---:|
| Versus no transfer | +25.886 [25.190, 26.590] | −22.056 [−22.644, −21.492] |
| Versus episode replay | +1.099 [1.051, 1.142] | 0 [0, 0] |
| Versus random rule | +29.264 [28.434, 30.072] | −1.780 [−2.052, −1.532] |

The abstract rule achieved a slightly higher score than replay, but its final risk was higher by 0.246 on average. This illustrates why a single score is insufficient: a controller can produce more useful work while leaving less safety margin.

## Interpretation
The pilot is consistent with the idea that **transferring a normalized principle can outperform carrying over a surface-level threshold**, especially compared with having no transfer at all. However, both replay and abstract-rule conditions avoided violations, and the abstract rule ended at higher residual risk. The advantage over replay is small and specific to this simulator.

The experiment does not show autonomous abstraction discovery: the normalization rule is provided explicitly. The next experiment should require the system to infer the shared relation from source-task examples, then test it on several held-out task families without supplying the mapping.

## Limitations
- Synthetic environment and hand-designed controllers.
- Abstract normalization is provided by the experimenter.
- Only one transfer family is tested.
- Results do not demonstrate consciousness or general intelligence.
- Raw episode data is produced locally by the runner; the committed summary and confidence intervals are derived from that reference run. Re-run the committed script to reproduce them exactly.

## Decision
Proceed to Ω-SELF-010: infer an invariant from experience rather than receiving the normalization rule. Evaluate task performance, constraint violations, residual risk, and transfer to multiple held-out families separately.
