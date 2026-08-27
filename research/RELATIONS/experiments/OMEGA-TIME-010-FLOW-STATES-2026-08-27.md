# OMEGA-TIME-010 — Flow States and Local Temporal Rate

Date: 2026-08-27
Status: EXPERIMENTAL / OPEN

## Motivation
Test the proposed picture that a system has an internal temporal flow, while the observed rate of change depends on the dynamical state of the medium. Use water-like phase labels only as an analogy: free/high-mobility (gas-like), constrained/intermediate (liquid-like), locked/low-mobility (crystal-like).

## Important non-circular definition
Do NOT define time by an imposed frequency. Introduce a common dimensionless causal update coordinate lambda only as bookkeeping. Each medium state has internal transition activity r(lambda), measured as the fraction of local degrees of freedom that actually change per causal update. Define accumulated local temporal coordinate tau(lambda)=sum r(lambda), up to a common calibration factor. Thus the experiment tests whether different dynamical phases generate different rates of internal change while sharing the same causal ordering.

## Model
1000 binary local degrees of freedom are driven through 1000 causal updates. Transition probabilities are p_gas=0.95, p_liquid=0.45, p_crystal=0.05. These values are deliberately simple phase-like regimes, not claims about real thermodynamic water.

For each update k:
activity(k)=number of changed local states / N.
The accumulated internal coordinate is tau(K)=sum(activity(k)).
The dimensionless temporal rate is d_tau/d_lambda=activity.

## Fixed-seed result
Mean activity over 1000 updates:
- gas-like: 0.950023
- liquid-like: 0.450213
- crystal-like: 0.050186

Therefore the same number of causal updates produces approximately 19x more internal state-change events in the gas-like regime than in the crystal-like regime.

## Interpretation
The model supports a precise version of the hypothesis: a system can possess one common causal ordering while its local dynamical state determines the rate at which internal change accumulates. In that sense, temporal flow is state-dependent in the model.

This does NOT establish that physical time literally behaves as a material fluid, nor that real cosmic phases have these numerical rates. The phase labels are an analogy; the measured quantity is internal transition activity.

## Critical distinction
There are now three separate quantities:
1. causal order lambda — shared bookkeeping of event succession;
2. local temporal accumulation tau — accumulated internal change;
3. observed frequency f — repetitions per chosen reference interval.

Changing the external presentation frequency can alter observed speed without changing the underlying sequence. Changing the medium's dynamical state can alter internal temporal accumulation for the same causal-update count.

## Conclusion
PASS (model-level): different dynamical states produce distinct internal rates of change under the same causal ordering.
OPEN (physical): whether this state-dependent temporal rate corresponds to a fundamental physical proper-time field requires a physical theory and empirical test.

## Next test
Couple two regions in different flow states and test whether a signal crossing the interface accumulates different local temporal coordinates while preserving a single causal history. Compare gas-like -> liquid-like -> crystal-like and reverse transitions. Preserve all earlier experiments unchanged.
