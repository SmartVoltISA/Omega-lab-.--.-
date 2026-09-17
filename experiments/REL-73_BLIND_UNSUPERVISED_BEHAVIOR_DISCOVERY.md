# REL-73 — Blind Unsupervised Behavior Discovery

**Date:** 2026-09-17  
**Status:** RESULT RECORDED  
**Principle:** FACT → CHECK → RESULT → DECISION → FIXATION

## 1. Question

Can Ω discover distinct behavioral classes from input/output trajectories **without being given mechanism names or a predefined binary distinction such as lag vs memory**?

## 2. Blind protocol

A standardized excitation suite was applied to 11 hidden synthetic system families. For each family, 6 independent seeds were generated. The observer received only concatenated input/output trajectories.

Excitation conditions:
- triangular ramps;
- periods: 1.0, 2.0, 4.0 s;
- amplitudes: 0.25, 0.40 around center 0.5;
- 100 samples retained per episode/condition;
- 6 seeds per hidden family.

No hidden mechanism label was used during normalization, dimensionality reduction, clustering, or selection of cluster count.

## 3. Hidden generator families

Labels were withheld from the clustering stage and revealed only for post-hoc audit:

1. first-order lag;
2. pure transport delay;
3. second-order underdamped response;
4. static saturation;
5. static dead-zone;
6. rate limiter;
7. lag + saturation;
8. Schmitt-type bistable switching;
9. slow/leaky integrator;
10. multilevel hysteretic switching;
11. noisy first-order lag.

The noisy lag family was intentionally included as a confounder rather than as a new mechanism class.

## 4. Unsupervised pipeline

1. concatenate raw input/output trajectories across the standardized excitation suite;
2. standardize trajectory dimensions;
3. reduce dimensionality by PCA, retaining 95% explained variance;
4. perform agglomerative Ward clustering for candidate k = 2…11;
5. choose k using silhouette score only;
6. reveal hidden labels only after clustering for audit.

No semantic features named “memory”, “hysteresis”, “delay”, etc. were supplied to the clustering stage.

## 5. FACT

The unsupervised clustering selected **k = 10** by maximum silhouette score among k=2…11.

Silhouette scores:
- k=2: 0.703
- k=3: 0.771
- k=4: 0.714
- k=5: 0.662
- k=6: 0.757
- k=7: 0.847
- k=8: 0.888
- **k=9: 0.956**
- **k=10: 0.996**
- k=11: 0.923

Post-hoc audit at k=10 produced one pure cluster for each of 10 behavioral groups, while first-order lag and noisy-lag occupied the same cluster. The hidden families were therefore recovered as 10 observable behavioral groups rather than 11 mechanism labels.

Audit metrics at k=10:
- Adjusted Rand Index against hidden generator labels: **0.893**
- Normalized Mutual Information: **0.973**
- silhouette: **0.996**

Confusion structure:
- lag + noisy-lag → same cluster;
- delay → separate;
- second-order → separate;
- saturation → separate;
- dead-zone → separate;
- rate limiting → separate;
- lag+saturation → separate;
- bistable Schmitt switching → separate;
- slow/leaky integration → separate;
- multilevel hysteretic switching → separate.

## 6. CHECK

The important check is not that the hidden labels were recovered exactly. The important result is that the clustering was performed without those labels and nevertheless formed stable groups that largely corresponded to distinct observable dynamics.

The failure/merge of lag and noisy-lag is informative: at the tested trajectory resolution and noise level, the system did not invent a distinction that was not sufficiently visible in behavior.

This is consistent with the Ω rule:

> **NON-SEPARABLE-AT-THIS-RESOLUTION** when the available observations do not support a reliable distinction.

The k=11 solution did not improve the unsupervised geometry: silhouette fell from 0.996 to 0.923 while the audit did not separate noisy-lag from lag. Thus forcing the number of hidden mechanisms would have been an artificial split.

## 7. RESULT

**PASS — blind unsupervised behavioral discovery at the tested synthetic resolution.**

Ω-style trajectory geometry was able to recover multiple distinct behavioral classes without being told in advance that the systems represented lag, delay, saturation, rate limiting, hysteretic switching, or other named mechanisms.

The result is stronger than REL-72 in one specific methodological sense: the observer was no longer asked to discriminate a predefined pair. It had to determine how many observable behavioral groups were present.

## 8. DECISION

Accepted as a **methodological result**, not as a new physical law.

Supported claim:

> Distinct dynamical behavior classes can emerge from blind comparison of input/output trajectories when the excitation protocol contains sufficient variation in reversal, amplitude, and timescale.

Not supported:
- that Ω has discovered fundamental physical mechanisms;
- that the chosen clustering method is universal;
- that all real physical systems will separate at this resolution;
- that behavioral equivalence implies identical physical mechanism.

## 9. Next falsification step

REL-74 should remove the fixed triangular-wave family as the sole excitation basis and test whether unsupervised behavioral classes persist under richer, partly randomized excitation. It should also test robustness to sampling rate, observation window, measurement noise, and unseen mechanism families.

The strongest next question is:

> **If Ω is given no mechanism vocabulary and no fixed excitation shape, does the same behavioral structure reappear?**
