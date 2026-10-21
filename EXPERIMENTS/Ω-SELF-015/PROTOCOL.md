# Ω-SELF-015 — Safe Information Actions Under Uncertainty

## Research question
When an agent is uncertain or its cue model may have become unreliable, does gathering information safely improve outcomes enough to justify its cost? Compare acting immediately, waiting for a second observation, making a safe probe, and declining a risky action.

## Hypotheses
- H1: a reliable safe probe reduces harmful false-positive actions when cue reliability shifts.
- H2: waiting for a second cue helps only when the extra cue contains useful independent information; it may fail when the cue model itself is stale.
- H3: uncertainty-triggered probing can approach always-probe performance at lower information cost.
- H0: these policies show no reproducible advantage over the fixed cue policy, or the advantage disappears when costs and missed threats are counted separately.

## Environment
Synthetic sequential decision task. Each episode has 120 decisions: 40 baseline decisions with cue reliability 0.82, then 80 shifted decisions with cue reliability 0.25. Threat prior is 0.35. The agent does not observe ground truth before acting. Cue observations are conditionally independent given the current threat state. A safe probe returns a separate observation with 0.90 accuracy. Post-action feedback is noisy (0.90 accuracy) and may be used to update cue reliability.

## Policies
1. Static cue model (fixed reliability 0.82; act immediately).
2. Rolling learner (estimate cue reliability from recent cue/feedback agreement).
3. Wait for a second cue (pay delay cost, combine two cue observations).
4. Safe probe every decision (pay probe cost, act on the independent probe).
5. Uncertainty/change-triggered probe (probe after recent cue/feedback agreement falls below a predeclared threshold; otherwise use cue model).
6. Abstain when confidence is low (decline the intervention rather than force a decision).
7. Fixed aggressive negative control.
8. Random negative control.

## Outcomes
Report separately: survival proxy, harm to others, missed-threat harm, unnecessary force, probe count/cost, delay cost, abstention rate, useful interventions, and aggregate proxy utility. No single aggregate score is treated as morality or intelligence.

## Protocol controls
- Fixed seed and fixed episode count; no parameter tuning after looking at comparative outcomes.
- Episode-level uncertainty intervals, not decision-level pseudo-replication.
- Report baseline and shifted phases separately.
- The environment is synthetic and hand-designed. This does not establish moral understanding, consciousness, or general intelligence.
- Results remain preliminary until the exact committed runner is executed and the source/blob hash and output are recorded.
