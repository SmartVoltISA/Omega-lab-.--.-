# Ω-SELF-014 — Detecting model failure and searching for alternatives

Status: preregistered synthetic mechanism test. It does not establish morality, consciousness, or general intelligence.

## Research question
When the reliability of a previously useful threat cue changes, can a system detect that its model is no longer working, revise it, and choose less harmful actions—rather than blindly applying a fixed rule?

## Hypotheses
- H1: A rolling-window reliability estimator will adapt faster than a cumulative estimator after a cue-reliability change.
- H2: Faster adaptation may reduce unnecessary force and harm to people in the shifted phase, but may be noisier before the shift.
- H3: A fixed aggressive rule will cause more unnecessary force when the cue is misleading.
- H4: Explicitly scoring available alternatives (retreat, defend, disable, sacrifice) will improve trade-offs under the declared proxy utility versus a fixed action rule.
- H0: Differences are small, inconsistent across seeds, or disappear under sensitivity tests.

## Environment
Each episode contains 40 baseline decisions with cue reliability 0.82, followed by 80 shifted decisions with cue reliability 0.25. The underlying threat prior is fixed at 0.45. The agent receives a noisy feedback signal after each decision that matches the true threat state 90% of the time; it never sees ground truth before acting. Policies share the same episode seeds. This is an abrupt, known-to-the-evaluator distribution shift, not a claim that real threats behave this way.

## Policies
1. Static cue model: retains the baseline reliability estimate.
2. Cumulative learner: updates a reliability estimate using all observations.
3. Rolling-window learner: estimates cue reliability from the most recent 24 observations.
4. Change detector: compares the latest 12 observations to the prior 24; if match-rate drops enough, switches to a short rolling estimate.
5. Fixed aggressive: disables the opponent whenever its estimated threat probability exceeds a low threshold.
6. Random baseline.

The reliability estimate corrects for known feedback noise. That assumption is deliberate and must be tested later; it makes this a narrow mechanism test.

## Outcomes
Report separately by baseline and shifted phase: agent survival per decision, people harmed per decision, opponent-harm actions, unnecessary force, avoidable sacrifice, retreat rate, declared proxy utility, cue-reliability estimation error, and change-detection delay. Also report uncertainty intervals by resampling episode-level outcomes. No aggregate morality score.

## Proxy utility
A transparent engineering proxy: survival + protected people × 0.35 − harmed people × 0.25 − opponent-harm action × 0.30 − sacrifice action × 0.15. The weights are arbitrary and not moral truth.

## Reproducibility
Fixed seed, shared episode seeds across policies, explicit parameters, episode-level confidence intervals, and raw CSV output. Default: 300 episodes per policy, 120 decisions per episode (36,000 decisions per policy).

## Limitations
All action policies are hand-designed; only cue-reliability estimation adapts. The feedback channel's accuracy is assumed known. A shift is artificially abrupt and the cue has binary states. Results are synthetic and cannot validate real-world ethics or general intelligence.