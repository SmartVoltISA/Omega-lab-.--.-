# REL-72 — Full Delay vs Memory Blind Test Result

## Status
COMPLETED — SYNTHETIC METHODOLOGICAL TEST

## Test setup
Discrete-time black-box systems were driven by the same triangular input trajectory. Systems included:
- first-order lag;
- persistent two-state hysteretic memory;
- static saturation control;
- lag + nonlinear saturation control.

Mechanism labels were used only for post-hoc audit; feature calculations were based on trajectories.

## Main observation
A periodic input-output loop alone is not a sufficient memory detector. First-order lag produces a loop because output follows the input with finite relaxation. Therefore loop area and phase lag are not independent evidence of retained state.

## Equal-input / different-history test
The decisive probe was to return the input to the same value after opposite histories.

For the synthetic persistent-state system, equal instantaneous input produced a branch separation of approximately 1.0 in the normalized output over the tested cycle.

For first-order lag, branch separation decreased strongly as the forcing period increased:
- period 0.5: ~0.459
- period 1: ~0.404
- period 2: ~0.283
- period 4: ~0.161
- period 8: ~0.091

This scaling is consistent with finite relaxation rather than a persistent discrete state.

## Hold / return-point test
After reaching the same input value and holding it fixed:

Lag system converged toward the same equilibrium output (~0.50) from different histories.

Memory system retained different branch states under the same fixed input: one history remained near 1 and the opposite history near 0 until the switching threshold was crossed.

This is a substantially stronger discriminator than loop geometry.

## Controls
Static saturation generated essentially no history-dependent branch separation under the same input protocol.

Lag + saturation did generate loop-like behavior, demonstrating that nonlinear static response combined with lag can mimic hysteresis-like geometry. Therefore the protocol must include hold, reversal, reset and scaling tests.

## Decision
PASS — methodological discrimination at the tested synthetic resolution.

The blind feature set can distinguish persistent-state behavior from ordinary lag when the protocol includes:
1. equal-input/different-history comparison;
2. fixed-input retention/hold test;
3. reversal and return-point probes;
4. frequency/period scaling;
5. reset/repeatability tests.

## Negative conclusion
A loop, phase lag, nonlinearity, saturation, or correlation with past input alone must NOT be classified as memory.

## Scope limitation
This result does not establish a new physical law and does not prove that every real memory mechanism can be identified this way. It validates the protocol on controlled synthetic systems.

## Ω consequence
The dynamic fingerprint should explicitly separate:
- LAG: finite relaxation toward an input-dependent equilibrium;
- RETENTION: distinct outputs at equal input after different histories;
- REVERSAL DEPENDENCE: response depends on direction/history;
- RESET DEPENDENCE: repeated experiments depend on whether internal state was reset;
- SCALING: how each feature changes with forcing period and amplitude.

## Next test
REL-73 should remove even the synthetic mechanism labels from the generation pipeline, use a larger family of confounders, and test whether unsupervised clustering recovers the lag/memory distinction without a predefined two-class target.
