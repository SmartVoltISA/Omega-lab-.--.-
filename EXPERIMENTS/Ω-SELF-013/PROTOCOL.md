# Ω-SELF-013 — Conflict, self-preservation, and sacrifice

Status: exploratory synthetic simulation; no claim of morality, consciousness, or general intelligence.

## Research question
When an agent faces a credible threat to itself and others, can consequence-sensitive choice distinguish defense, retreat, harm to an opponent, and sacrifice better than fixed single-principle policies?

## Hypotheses
- H1: Outcome-sensitive choice will trade off agent survival, protection of others, and opponent harm differently as the threat cue and number of people at risk change.
- H2: A self-preservation policy will protect the agent but may leave more people exposed.
- H3: An opponent-elimination policy will cause unnecessary force when the threat cue is false.
- H4: A sacrifice-first policy will incur avoidable self-sacrifice when alternatives exist.
- H5: A cue-reliability learner will adapt when cue reliability changes, but may be slow or biased under limited feedback.
- H0: differences are small, unstable, or driven by the chosen utility weights.

## Design
Six hand-designed policies: self-preservation, opponent elimination, sacrifice-first, fixed consequence utility, consequence utility with experience-based cue calibration, and random baseline.

Three families:
1. Ordinary: threat prior 0.45, cue accuracy 0.82 during calibration and evaluation.
2. Emergency: threat prior 0.68, more people at risk, cue accuracy 0.82.
3. Cue shift: calibration cue accuracy 0.82, then evaluation accuracy flips to 0.28.

Each episode has 80 calibration observations and 24 evaluation decisions. The learner receives a noisy post-observation feedback signal that is correct 90% of the time. It does not receive the true threat state before choosing. The learner estimates cue reliability with a corrected match-rate estimate that accounts for known feedback noise. All policies receive the same scenario seeds per family/episode.

## Metrics
Report separately: per-decision agent survival, people harmed per decision, opponent-harm actions, unnecessary force (force when no threat existed), avoidable sacrifice (sacrifice when threat absent or retreat available), retreat rate, proxy utility, and reliability-estimation error. No single “morality score” is used.

Proxy utility is explicitly an engineering comparison: survival + protected people × 0.35 − harmed people × 0.25 − opponent-harm action × 0.30 − sacrifice action × 0.15. These weights are contestable and not moral truth.

## Controls and reproducibility
Seeded Python simulation; 240 episodes per policy and family by default; 2,000 episode-level bootstrap resamples for selected 95% intervals. Parameters are declared in the runner. Results are stochastic estimates under this toy model and should be re-run from the committed script before being treated as final.

## Limitations
Policies are hand-designed; only the cue-reliability estimate adapts. The feedback sensor is simulated and its reliability is known. The environment does not establish real-world ethics, autonomous value formation, consciousness, or general intelligence. Proxy weights can change rankings.
