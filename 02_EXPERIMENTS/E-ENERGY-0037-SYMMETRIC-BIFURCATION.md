# E-ENERGY-0037 — Symmetric bifurcation under equal excitation

## Question
If a balanced system receives equal excitation and contains a symmetric instability, does the neutral state remain dominant, or does the system split into two approximately equal opposite populations?

## Model
1000 links, initial state x=0. Equal total excitation. Symmetric nonlinear update with zero-mean conservation enforced after each step. No red/blue labels are assigned in the dynamics. Sign is only the resulting state: negative/positive. Neutral is |x| <= 0.1.

## Control sweep
20 independent seeds per parameter value.

| instability alpha | negative | neutral | positive |
|---:|---:|---:|---:|
| 0.001 | 37.28% | 25.23% | 37.49% |
| 0.010 | 46.11% | 7.71% | 46.19% |
| 0.030 | 49.785% | 0.31% | 49.905% |
| 0.050 | 49.99% | 0.02% | 49.99% |

## Result
A symmetric instability with conserved zero mean produces spontaneous separation into two opposite populations. As instability increases, the neutral population collapses toward zero while the two opposite populations approach 50/50.

## Interpretation
This supports the narrower structural hypothesis that a balanced system does not necessarily remain neutral. Under symmetric excitation plus an instability, it can bifurcate into two complementary states while preserving global balance.

This is compatible with the user's proposed mapping:
- red = one separating/repulsive polarity;
- blue = complementary/connecting polarity;
- green = neutral state.

However, the simulation does NOT establish that physical light colors correspond to these signs, nor that matter fundamentally splits into red/blue states. It only tests the abstract bifurcation mechanism.

## Important correction
The earlier statement that the system might simply "split into two halves" is condition-dependent. Without the symmetric instability, neutral can remain stable. The 50/50 split emerges here because the dynamics are symmetric and globally balanced.

## Next experiment
Introduce explicit network topology and coupling between links, then apply equal excitation while keeping the total resource fixed. Test whether the two-polarity split becomes spatially organized into complementary domains rather than random positive/negative assignment.
