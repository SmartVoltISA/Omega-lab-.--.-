# Ω-REAL-1 — CausRCA Real-Data Validation Protocol v1.0

**Status:** PREREGISTERED / READY FOR LOCAL EXECUTION

**Date:** 2026-09-12

## 1. Objective

Test whether the intervention-sensitive relational signature developed in Ω-Test-11, Ω-Test-12 and Ω-Test-15 can be evaluated on real industrial-system data without defining the observable from the manipulated relation itself.

This experiment is a validation/falsification experiment. It is **not** a test of a universal physical law and must not be interpreted as proof of Ω-0, struggle, causality, or physical space.

## 2. External dataset

Target dataset: **causRCA** — CNC industrial vertical lathe causal-root-cause-analysis dataset.

Source repository: https://github.com/causalgraph/causRCA
Zenodo record: https://zenodo.org/records/15876410
DOI: 10.5281/zenodo.15876410

The dataset contains real CNC operational data together with fault data and an expert causal graph. The experiment must record the exact downloaded archive/version and file hashes before analysis.

Known provenance limitation: OPC UA timestamps represent publication time of a value change and chronological ordering across variables is not guaranteed. This must be retained as a methodological limitation and not silently corrected.

## 3. Research question

When a known or externally labelled fault/intervention changes a relation between system variables, does the downstream relational predictive signature change across an independently defined system boundary more strongly than matched negative controls?

## 4. Hypotheses

### H1 — relational intervention signature
An intervention that breaks or changes an identified causal relation will produce a measurable suppression of downstream predictive/reachable-state structure across an independently defined boundary, followed by recovery when the relation is restored or the fault condition ends.

### H0 — no relational signature
After controlling for marginal distributions, common drive, temporal ordering artefacts, and fault-independent changes, the intervention does not produce a reproducible boundary-crossing effect beyond negative-control variation.

## 5. Ω-0 interpretation used in this experiment

`0` is used only as a boundary/reference/interaction-front concept.

It is **not** a third relation value.

Do not encode:

- absence as relation state 0;
- boundary as an entity;
- boundary as a relation value;
- path as automatically equivalent to struggle;
- temporal index as physical duration.

The empirical experiment tests an intervention-sensitive relational effect. It does not test the metaphysical interpretation of `0` directly.

## 6. System and boundary definition

The boundary/partition must be defined **before outcome measurement** and independently of the measured effect.

Candidate partitions should be taken from the expert causal graph and/or stable subsystem grouping, for example:

- source subsystem → receiving subsystem;
- Probe → downstream variables;
- Hydraulics → downstream variables;
- Coolant → downstream variables.

The selected partition, node lists and edge relation must be frozen in the experiment record before the final statistic is calculated.

## 7. Intervention definition

Use externally labelled fault/intervention windows from the dataset where the manipulated/faulted variable or relation is known from the dataset metadata/expert graph.

Do not infer the intervention from the outcome statistic.

For each selected case record:

- fault/scenario ID;
- source variable(s);
- receiver/downstream variable(s);
- start/end indices or timestamps;
- relation/edge identified in the expert graph;
- reason this constitutes an intervention or externally imposed perturbation;
- all exclusions.

## 8. Observable

The primary observable must be downstream and independent of the boundary definition and direct edge-flux measurement.

Preferred statistic:

`G(A→B) = 1 - Var(residual_full) / Var(residual_base)`

where the full predictor uses source-side history and the base predictor does not.

For each intervention window calculate:

`S_boundary = G_pre - G_intervention`

`R_boundary = G_post - G_intervention`

Use fixed model class and hyperparameters across pre/intervention/post windows.

If the data do not support a valid time-series predictive statistic because of sampling/timestamp limitations, classify the design as INVALID rather than changing the statistic post hoc.

## 9. Negative controls

At minimum include:

1. no-edge / unrelated variable pairs;
2. matched shared-drive/common-cause pairs where possible;
3. fault windows with no hypothesised direct relation;
4. temporal-shift controls preserving marginal distributions;
5. where feasible, permutation controls preserving relevant marginal structure.

The same analysis pipeline and thresholds must be used for controls.

## 10. Primary decision rule

The primary result is considered **CONDITIONAL PASS** only if all of the following are satisfied:

1. finite valid measurements;
2. boundary and intervention were preregistered/fixed before outcome calculation;
3. direct intervention produces suppression greater than the prespecified null/control distribution;
4. recovery is present after intervention/fault removal when a recovery window exists;
5. false-positive rate among negative controls remains below the preregistered threshold;
6. the effect survives the timestamp/provenance sensitivity analysis;
7. the result is not explained by a direct manipulation of the observable itself.

Suggested initial thresholds, to be frozen before the first final run:

- two-sided permutation `p < 0.01` for the primary intervention effect;
- control false-positive rate ≤ 0.05;
- positive suppression/recovery in at least 80% of eligible direct cases.

If sample size or data structure makes these thresholds impossible to evaluate honestly, mark the experiment **INVALID / INSUFFICIENT DATA**, not PASS.

## 11. Falsification conditions

Reject the hypothesis if:

- intervention and controls are statistically indistinguishable;
- effect is driven by common cause/common drive;
- effect disappears under timestamp sensitivity analysis;
- effect depends on post-hoc boundary selection;
- negative controls show comparable effects;
- the statistic is directly coupled to the manipulated relation;
- insufficient valid cases prevent the prespecified test.

## 12. Analysis lock

Before execution, freeze:

- dataset version/hash;
- selected subsystem/partition;
- node/edge lists;
- intervention windows;
- preprocessing;
- missing-value policy;
- timestamp policy;
- predictor lags;
- train/test or windowing scheme;
- statistic;
- permutation count;
- significance threshold;
- control definitions;
- PASS/FAIL/INVALID criteria.

No parameter may be tuned after seeing the primary result. Any correction creates a new version and preserves the original result.

## 13. Provenance

The raw external dataset must not be committed to this repository unless licensing and repository-size constraints explicitly permit it.

Commit instead:

- source URL/DOI;
- dataset/version identifier;
- SHA-256 hashes of used files;
- selected file paths;
- extraction/selection script;
- analysis script;
- configuration/preregistration;
- derived aggregate results;
- logs and failure records.

## 14. Execution target

Local execution is preferred to avoid GitHub Actions compute limits.

Minimum environment:

- Python 3.x
- NumPy
- pandas
- SciPy
- deterministic random seed

Recommended structure:

```text
00_CORE/EXPERIMENTS/
  OMEGA_REAL_1_CausRCA_PROTOCOL_v1.0.md
  OMEGA_REAL_1_CausRCA_CONFIG.json
  OMEGA_REAL_1_CausRCA_ANALYSIS.py
  OMEGA_REAL_1_CausRCA_REPORT.md
  OMEGA_REAL_1_CausRCA_RESULTS.csv
  OMEGA_REAL_1_CausRCA_HASHES.txt
```

## 15. Epistemic status

A positive result would mean:

> The preregistered intervention-sensitive relational statistic has evidence of transfer to this real industrial dataset under the stated controls.

It would **not** mean:

- Ω-0 is a proven law of nature;
- all boundaries are fronts of struggle;
- correlation is causation;
- the same geometry exists physically at every scale;
- the result is universal across physical systems.

A negative result is scientifically valid and must remain permanently recorded.

## 16. Canonical rule

`RESULT ≠ TRUTH`

`RESULT → VERIFY → CLASSIFY → RECORD`

**Next action:** obtain the exact causRCA archive locally, freeze its hash and execute this protocol without changing the primary observable after inspecting results.
