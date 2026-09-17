# REL-68 — Blind Time-Series Functional Fingerprint Pilot

**Date:** 2026-09-17
**Layer:** Ω-Lab
**Status:** PILOT / COMPUTATIONAL CONTROL

## FACT

A blind synthetic time-series test was run without using physical names during feature extraction. Six anonymous systems (A–F) were driven by the same forward/reverse input protocol.

The candidate fingerprint used observable behavior rather than mechanism labels:

`F = (N_states, hysteresis_area, retention/persistence, response_range, transition_roughness)`

The test deliberately included:
- two bistable hysteretic systems with different thresholds;
- one memoryless threshold switch;
- one continuous saturating response;
- one leaky/lagged response;
- one multi-threshold hysteretic system.

## CHECK

Observed pilot features:

| ID | States | Hysteresis area | Range | Interpretation before reveal |
|---|---:|---:|---:|---|
| A | 2 | 1.809 | 2.000 | bistable + strong hysteresis |
| B | 2 | 1.005 | 2.000 | bistable + weaker hysteresis |
| C | 2 | 0.000 | 2.000 | threshold switching without hysteresis |
| D | 150 | ~0 | 1.999 | continuous nonlinear response |
| E | 309 | 0.353 | 1.848 | lagged/history-dependent continuous response |
| F | 2 | 2.010 | 2.000 | multi-threshold hysteretic response |

The crucial control is A/B/C: all have two coarse states and similar response range, but hysteresis area separates A/B from C. Therefore `number of states + topology` is insufficient.

A/B/F remain close at the broad functional level (persistent alternative states + history-dependent switching), while threshold structure can distinguish subtypes.

## RESULT

The pilot supports the following methodological decomposition:

`coarse topology → insufficient`

`trajectory + directionality + history → informative`

Functional equivalence should therefore be computed from the observable transition behavior, not from static graph shape alone.

## LIMITATIONS

This is a synthetic computational control, not a physical validation. The fingerprints were generated from known model families, so it does not yet test whether Ω can recover classes from genuinely unknown physical data.

The next experiment must use externally sourced experimental curves/time series and freeze the extraction algorithm before revealing system identity.

## DECISION

Proceed to REL-69:

`published/experimental time-series → blind preprocessing → automatic fingerprint extraction → unsupervised clustering → name reveal → correspondence audit`.

Required controls:
1. negative-control systems with similar topology but different dynamics;
2. shuffled-history control to test whether history features are actually informative;
3. noise perturbation;
4. held-out physical systems;
5. preregistered similarity metric and tolerance.

## FIXATION

REL-68 is a new anchor. It does not overwrite REL-66 or REL-67.

Current methodological chain:

`Observation → Trajectory → Transition → Fingerprint → Functional Class → Physical Correspondence`
