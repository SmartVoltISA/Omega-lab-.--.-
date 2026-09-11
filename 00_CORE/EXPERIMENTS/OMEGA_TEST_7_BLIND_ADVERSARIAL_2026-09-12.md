# Ω-TEST-7 — BLIND / ADVERSARIAL INTERACTION DETECTION (CORRECTED)

**Status:** COMPLETED after numerical-stability audit.

The first run produced 3 non-finite scores in the linear/interaction condition. That run is **INVALID for inference** and is retained as a methodological failure. The simulation was stabilized and the entire 180-dataset blind test was rerun.

## Design

180 hidden-label datasets: 3 generative families × 3 conditions × 20 replicates.

Conditions:
- `null`: no interaction
- `interaction`: explicit coupling
- `common_drive`: no interaction, but an adversarial shared delayed input

The detector sees only `(x,y)`; family and condition are hidden.

## Fixed detector

`score = (MSE[y|past y] − MSE[y|past y,past x]) / MSE[y|past y]`

Fixed threshold:

`score > 0.001 → interaction`

## Corrected blind results

- Sensitivity: **1.000**
- Specificity: **0.975**
- Overall false-positive rate: **0.025**
- Common-drive false-positive rate: **0.050**
- Null false-positive rate: **0.000**

Confusion counts: TP=60, FN=0, FP=3, TN=117.

All 180 corrected scores are finite.

## Interpretation

The blind test checks whether the candidate detector can recognize interaction without being told the generating family or condition.

The detector survived the tested adversarial common-drive confound with a 5% false-positive rate.

**Ω classification: PASS — corrected blind/adversarial candidate test.**

This supports the synthetic claim that the detector can identify explicit interaction across the tested families while resisting the tested common-drive confound.

It does **not** establish a universal physical invariant.

## Falsification boundary

Before any foundational promotion, test matched marginal distributions, randomized/downsampled observations, unknown coupling direction, asymmetric and time-varying coupling, stronger shared-drive confounds, and a locked analysis protocol.

## Methodological note

The initial unstable run is not discarded. It is retained as an INVALID methodological run; the corrected run supersedes it for inference while preserving provenance.
