# Ω-INF-2 — Results

**Date:** 2026-08-13
**Status:** COMPLETED / DESCRIPTIVE
**Seed:** 20260813
**Text length:** 855 characters

## Question

What happens to organization-sensitive measures when a text is altered at progressively different organizational levels while the underlying character inventory is preserved?

## Conditions

- **T0** — original text.
- **T1** — global character permutation.
- **T2** — word order shuffled independently inside each paragraph.
- **T3** — sentence order shuffled independently inside each paragraph.
- **T4** — paragraph order shuffled globally.

These are interventions at different levels. They are **not** assumed to destroy equal amounts of information.

## Results

| Condition | Characters | Symbol entropy | Conditional entropy | Unique bigrams | zlib bytes |
|---|---:|---:|---:|---:|---:|
| T0 original | 855 | 4.632675 | 2.997873 | 281 | 654 |
| T1 character shuffle | 855 | 4.632675 | 3.755484 | 443 | 827 |
| T2 word shuffle | 855 | 4.632675 | 3.015446 | 285 | 658 |
| T3 sentence shuffle | 855 | 4.632675 | 3.000215 | 282 | 658 |
| T4 paragraph shuffle | 855 | 4.632675 | 2.997873 | 281 | 656 |

## Observations

1. Character composition and symbol entropy remain invariant across all conditions.
2. Global character scrambling produces a large change in local-transition statistics and compression.
3. Word, sentence and paragraph permutation produce only small changes in these particular metrics for this particular short text.
4. Therefore, these metrics are sensitive to some forms of organization but are not semantic-information detectors.
5. The weak T2–T4 response is itself a useful negative/control result: destroying a higher-level textual organization does not necessarily cause a large change in low-level statistical metrics.

## Interpretation

The experiment supports a narrower claim than "information is in relations": measurable properties can depend on organization even when the element inventory is unchanged. It does **not** establish that semantic information is captured by the selected metrics.

The contrast between T1 and T2–T4 is especially important. It shows that low-level relational statistics and higher-level textual organization are not interchangeable.

## Counterevidence / limitation

The experiment does not provide a semantic metric. A human reader can regard T2 or T3 as substantially altered while the selected numerical measures move only slightly. This prevents us from equating metric change with information loss.

The text is short and was authored specifically for the experiment. The result therefore requires replication on longer, independently sourced texts and with additional controls.

## Next step

Ω-INF-3 should preserve local relations while destroying longer-range relations. This will test whether information-sensitive measurements can distinguish local from global organization without relying on semantic judgment.

## Status

**H-INF-2: OPEN.**

No universal conclusion is accepted from this experiment.
