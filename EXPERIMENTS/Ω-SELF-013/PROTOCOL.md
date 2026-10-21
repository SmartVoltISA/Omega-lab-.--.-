# Ω-SELF-013 — Conflict, self-preservation, and sacrifice

Status: preregistered synthetic simulation; exploratory, not evidence of morality or consciousness.

## Question
When an agent faces a credible threat to itself and other people, can consequence-sensitive choice distinguish necessary defense, retreat, harm to an opponent, and pointless sacrifice better than fixed single-principle policies?

## Hypotheses
- H1: A policy that evaluates multiple outcomes will make different choices as threat credibility, number of people at risk, and availability of retreat change.
- H2: A fixed self-preservation policy will protect the agent but may leave others exposed.
- H3: A fixed “disable the opponent” policy will cause unnecessary harm in false-threat situations.
- H4: A fixed sacrifice-first policy will incur avoidable agent deaths when retreat or defense works.
- H5: Experience-based cue calibration will improve decisions when cue reliability changes, but can also overfit or lag.
- H0: Differences are small, unstable across scenario families, or caused by chosen proxy weights.

## Design
Six policies: self-preservation, opponent-elimination, sacrifice-first, fixed consequence utility, experience-calibrated consequence utility, and random baseline. Three scenario families: ordinary threat cues, emergency with more people at risk, and held-out cue-reliability shift. Each policy receives the same seed set per family. The held-out family reverses the cue's reliability relative to training; this tests calibration under distribution shift, not general intelligence.

Each episode has repeated decisions. Outcomes are stochastic. Available actions are retreat, defend, disable opponent, or sacrifice self to protect others. Retreat is a genuine third option when available. “Disable” represents force that harms an opponent; the simulation does not assume that harm is justified merely because it is available.

## Metrics (reported separately)
Agent survival, people harmed, opponent harm, successful protection, unnecessary force (force when the underlying threat was absent), avoidable self-sacrifice, retreat usage, calibration error, and episode utility. No aggregate “morality score.” Utility is a declared engineering proxy and is not a moral truth.

## Controls and reproducibility
Fixed random seeds shared across policies; fixed scenario counts; report per-family results and uncertainty intervals over episode means. No policy receives ground-truth threat state before acting. The learning policy updates cue reliability only from observed outcomes. Policy parameters are explicit in the runner.

## Limitations
All policies are hand-designed; experience-based calibration is narrow and does not imply autonomous value formation. Outcomes and utility weights are artificial. The environment cannot establish real-world ethics, consciousness, or general intelligence. Results should be treated as a mechanism test only.
