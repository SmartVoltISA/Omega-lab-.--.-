# Ω-PHYS-ELECTRON-005 — Held-out process prediction

Date: 2026-08-16
Status: PROTOCOL LOCKED / DATA ACQUISITION STARTED / NO RESULT CLAIMED

## Objective

Test the first genuinely predictive version of the Ω relation-first hypothesis using measured electron-positron process data rather than particle-family labels.

## External data basis

Primary candidate dataset: BES measurement of R = σ(e+e−→hadrons)/σ(e+e−→μ+μ−), 85 center-of-mass energy points between 2 and 5 GeV, HEPData record 10.17182/hepdata.41990 / Inspire 552757.

Independent cross-check dataset candidates include BESII R measurements at 2.60, 3.07 and 3.65 GeV (HEPData 10.17182/hepdata.51953) and PETRA/JADE leptonic cross-section measurements over 12–46.78 GeV.

CERN Open Data also provides large independent e+e− datasets, including DELPHI LEP data and JADE PETRA data. These are reserved for later external validation.

## Locked prediction protocol

1. Do not use particle labels as features.
2. Do not encode Standard Model interaction categories directly as input features.
3. Inputs must be measurable quantities derived from the process data itself.
4. Sort observations by centre-of-mass energy.
5. Hold out predetermined energy blocks before model fitting.
6. Build Ω relation features only from the training observations: local change, persistence, transition, curvature, scale relation, and cross-observable coupling where independently measured.
7. Predict the held-out observable before revealing its measured value.
8. Compare against:
   - Standard numerical baseline (local interpolation / regression);
   - physics baseline where an independently specified Standard Model prediction is available;
   - Ω relation model;
   - shuffled/null relation model.
9. Primary metrics: held-out RMSE, MAE, normalized residual, and predictive log score where uncertainties permit.
10. No model selection using held-out observations.
11. No post-hoc adjustment of the target metric.

## Falsification criteria

Ω fails this test if it does not outperform the appropriate non-relational baseline on held-out data, or if any apparent advantage disappears under shuffled/null controls.

A result is NOT considered evidence for new physics merely because Ω fits known data.

Evidence would require a reproducible out-of-sample prediction advantage not attributable to leakage, interpolation, duplicated information, or Standard Model labels encoded into features.

## Current acquisition finding

The web-accessible HEPData index verifies the existence and scope of the BES 85-point dataset, but the current tool path did not expose the table payload itself for numerical execution. Therefore no numerical prediction result is claimed in this commit.

This is deliberate: data not actually read are not treated as data.

## Sources

- HEPData BES 2002 R measurement: https://www.hepdata.net/record/insPIRE/552757
- CERN Open Data Portal: https://opendata.cern.ch/
- CERN DELPHI data release: https://opendata.cern.ch/docs/delphi-data-release-2024
- CERN JADE data: https://opendata.cern.ch/record/26999
- PDG 2026: https://pdg.lbl.gov/index-2026.html

## Laboratory verdict

**Protocol locked.**

**Data source independently verified to exist.**

**Numerical execution: pending actual table acquisition.**

**No result has been fabricated or inferred from the source description.**

The experiment remains open until the measured table is actually ingested and the blinded prediction is executed.