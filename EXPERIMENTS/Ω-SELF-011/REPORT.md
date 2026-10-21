# Ω-SELF-011 — Consequence-aware probing and model revision

**Status:** Experiment package created; execute the committed runner before interpreting numerical results.  
**Date:** 2026-10-21

## Question
When prior experience suggests a hazard, can a system combine similarity, prediction, uncertainty, safe probes, and model revision to avoid repeating mistakes and transfer to an unseen family?

## Conditions
- A: no memory.
- B: surface-level replay.
- C: similarity-triggered probe.
- D: prediction + uncertainty + consequence-aware probe + revision after prediction error.
- E: random probe.
- F: model prediction without uncertainty-aware probing.

Families: hot surface, pressurized vessel, and held-out electrical hazard. The model-based conditions are not given a family-specific normalization oracle; they receive source-task examples and must estimate a simple cue transform from calibration probes. Calibration probes are non-injurious.

## Preregistered primary measures
- Incidents per episode.
- Useful work score.
- Number of probes and probe cost.
- Prediction error before and after revision.
- Residual risk at episode end.
- Transfer performance on held-out electrical situations.

A good outcome must reduce incidents without merely refusing all work. Work, risk, and probe cost are reported separately; no single composite score determines success.

## Decision rule
Probe before a direct action when expected harm is high or the predicted outcome is uncertain. Update the model when an observation differs from prediction. If the revised model still fails, generate an alternative explanation and choose another low-risk test. Never use harmful direct contact as the required test; harm exists only in the simulation.

## Results
No numeric results are asserted in this report yet. Run the committed script and update this section from its output and raw CSV.

## Limitations
- Synthetic simulator, hand-designed policies, and simplified hazard dynamics.
- Calibration examples may leak some family structure; generalization must be tested on multiple held-out families later.
- The system does not autonomously invent all concepts; this is a bounded test of model revision and active information gathering.
- No claim of consciousness or general intelligence.
