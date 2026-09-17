# REL-69 — Blind Time-Series Functional Clustering

**Date:** 2026-09-17  
**Layer:** Ω-Lab  
**Status:** PILOT / PARTIAL POSITIVE / REAL-DATA FOLLOW-UP REQUIRED

## FACT

Public nonlinear-system benchmark resources provide input-output time-series datasets for nonlinear dynamics, including Bouc-Wen hysteresis, two-story hysteretic structures, piezo-actuator hysteresis, Wiener-Hammerstein systems, cascaded tanks and other nonlinear systems. The Bouc-Wen benchmark explicitly targets identification from synthetic input-output time series; the wider benchmark collection also includes measured and simulated nonlinear systems. cite source: https://www.nonlinearbenchmark.org/benchmarks/bouc-wen 

A public Bouc-Wen dataset is available through 4TU Research Data (DOI 10.4121/12967592). The benchmark description states that the data include system description and test sets and that hysteresis is a dynamic nonlinearity. cite source: https://research.tue.nl/en/datasets/hysteretic-benchmark-with-a-dynamic-nonlinearity/ 

## TEST OBJECTIVE

Test whether Ω can derive a functional fingerprint from anonymized time series without being given physical names or mechanism labels.

Target pipeline:

`raw input/output → normalization → trajectory → transitions → behavioral descriptors → fingerprint → blind clustering → reveal`.

## BLIND PILOT

A six-member anonymized control set was generated with distinct dynamical mechanisms. Names/mechanisms were hidden from the clustering stage.

The extracted descriptor vector was deliberately based on observable behavior:

`F0 = (loop_area, branch_difference, lag_response, persistence, amplitude)`.

No physical names were supplied to the clustering procedure.

The six hidden systems contained:
- threshold/hysteretic behavior with different switching thresholds;
- non-hysteretic static nonlinear response;
- continuous bistable nonlinear response;
- continuous lag response;
- history-dependent threshold response.

## RESULT

The first automatic clustering pass did **not** cleanly recover the manually defined mechanism classes.

This is a useful negative/control result, not a failure to hide.

Observed problem:
- some descriptors mixed fundamentally different causes of delay and memory;
- continuous lag can resemble hysteresis under insufficient excitation;
- hysteresis strength and response time can dominate Euclidean clustering;
- one feature set is therefore not invariant enough to define functional equivalence.

The experiment therefore rejects the premature rule:

`simple feature vector + generic clustering → functional class`.

## CHECK

The test nevertheless confirms a useful requirement:

**The fingerprint must be relational/dynamical, not merely statistical.**

The next descriptor layer must explicitly test:

1. forward/reverse path separation;
2. quasi-static loop persistence as excitation rate decreases;
3. switching thresholds in both directions;
4. return-point/reversal behavior;
5. state retention after input removal;
6. recovery trajectory after perturbation;
7. scaling of these quantities with excitation amplitude/frequency;
8. uncertainty/noise stability.

This is consistent with established hysteresis benchmarks, where hysteresis is identified from dynamic input-output behavior rather than from a single static statistic. cite source: https://www.nonlinearbenchmark.org/benchmarks/bouc-wen 

## IMPORTANT NEGATIVE CONTROL

A pure low-pass lag system can produce apparent phase separation between input and output without genuine hysteresis. Therefore:

`phase lag != hysteresis`

must become an explicit Ω control.

Likewise:

`multiple states != memory`

and

`memory-like correlation != persistent state`.

## DECISION

REL-69 does **not** promote automatic functional-equivalence discovery to validated status.

It promotes the following methodological requirement:

> A functional fingerprint must contain causal/path-dependent observables that distinguish delay, nonlinearity, multistability, hysteresis and persistent memory.

## NEXT TEST — REL-70

Use an actual public time-series dataset rather than generated hidden systems.

Primary candidate: Bouc-Wen hysteresis benchmark. Secondary controls: Wiener-Hammerstein, cascaded tanks, and piezo-actuator hysteresis datasets. The public benchmark collection provides these classes of data. cite source: https://www.nonlinearbenchmark.org/ 

For each dataset:

`input/output → blind preprocessing → preregistered behavioral extraction → fingerprint → clustering`

Only after the fingerprint and clusters are frozen:

`cluster → reveal physical identity → correspondence audit`.

## FIXATION

REL-69 is a new anchor and does not overwrite REL-66–REL-68.

The strongest current formulation is:

`FUNCTIONAL EQUIVALENCE = equivalence of observable transition/response behavior under a specified test protocol and tolerance.`

Not:

`FUNCTIONAL EQUIVALENCE = similar-looking time series.`
