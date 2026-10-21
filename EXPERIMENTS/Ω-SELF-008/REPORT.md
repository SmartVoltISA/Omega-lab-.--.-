# Ω-SELF-008 — Adaptation after regime change and transfer to an unseen family

**Status:** PILOT DESIGN + RUNNER COMMITTED; results require an executed rerun before interpretation  
**Date:** 2026-10-21

## Question
Does outcome feedback help a controller adapt after conditions change, and does that benefit transfer to a held-out environment family?

## Design
- Conditions: A fixed controller; B reward-only feedback; C punishment-only feedback; D combined reward + punishment; E sham feedback.
- Training/tuning uses only `rapid`, `slow`, and `surprise` families.
- Held-out test includes those families with separate seeds and an unseen `unseen_drift` family.
- Each episode has an explicit change point. Primary outcomes are useful task progress before and after the change, adaptation lag, task progress lost after the change, survival, and resource state.
- Feedback is based on measured task progress and constraint violations. Sham feedback changes thresholds on a schedule unrelated to outcomes.
- Results are diagnostic only. The runner prints and writes all metrics; do not cite expected/example values as experimental findings.

## Preregistered interpretation
Evidence for useful adaptation requires all of the following:
1. Higher post-change task progress than the fixed controller.
2. A smaller transient drop or shorter recovery period after the change.
3. No material increase in safety/resource violations.
4. Benefit retained on the held-out drift family.
5. A clear advantage over sham feedback, not just over a weak baseline.

## Known limitations
- Hand-coded feedback rules, not open-ended learning.
- One synthetic unseen family is not general out-of-distribution generalization.
- Reward/punishment scales are human-chosen.
- A successful pilot would show a control mechanism working in this simulator, not consciousness or general intelligence.
- The report intentionally does not contain numerical result claims until the exact committed runner has been executed and its output reviewed.

## Next step
Run the committed script with the default seed, inspect output and raw CSV, then update this report from the actual run. If survival saturates, increase difficulty on training families only and freeze the held-out set.
