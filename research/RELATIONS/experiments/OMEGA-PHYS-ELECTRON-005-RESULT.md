# Ω-PHYS-ELECTRON-005 — BES R masked holdout prediction

Date: 2026-08-16
Status: COMPLETED RETROSPECTIVE MASKED-HOLDOUT PILOT / NEGATIVE

## Dataset
BES measurement of R = sigma(e+e- -> hadrons) / sigma(e+e- -> mu+mu-) at 85 center-of-mass energies between 2 and 4.8 GeV. Primary paper: Phys. Rev. Lett. 88 (2002) 101802; arXiv hep-ex/0102003. The source reports an average precision of about 6.6%. HEPData record 41990 contains the measured table.

## Important epistemic status
The full published table was visible to the analyst before this retrospective computational test. Therefore this is NOT a preregistered blind experiment. It is a masked-holdout reproducibility/pilot test: test values were masked from the fitting calculation, but the analyst had already inspected the source.

## Masking rule
Deterministic every-5th observation was designated test data. The model received all other observations. No test R values were used to fit the predictor.

## Models
Baseline: local linear interpolation between the nearest available observations bracketing each masked point.

Ω relation pilot: local quadratic relation-state reconstruction using the two nearest available observations on each side. The representation uses local value, first-change relation and curvature relation; no Standard Model formula or particle labels were supplied.

## Results
For the 16 test points for which both models had complete bracketing support:

Linear baseline:
- MAE = 0.16347
- RMSE = 0.20566
- R² = 0.90692

Ω local-quadratic relation model:
- MAE = 0.17102
- RMSE = 0.22145
- R² = 0.89208

Thus the Ω relation reconstruction was WORSE than the simple linear baseline on this test.

The last masked point was excluded because the deterministic test position had no right-hand training observation for interpolation. It was not imputed or used to improve the score.

## Interpretation
This is a negative result for the tested Ω predictor. The relation representation did not demonstrate predictive improvement over a trivial local interpolation baseline.

This does NOT falsify every possible Ω model. It falsifies only the tested local quadratic relation predictor on this dataset and split.

## What remains untested
A stronger Ω model could use a preregistered state-transition representation, uncertainty weighting, multiple independent experiments, and genuinely unseen datasets. Such a model must be specified before test values are opened.

## Verdict
Known experimental structure is reproducible. The tested Ω relation predictor did NOT beat the simple baseline.

Status: NEGATIVE / VALID CONTROL RESULT.

## Sources
- arXiv: https://arxiv.org/abs/hep-ex/0102003
- HEPData record: https://www.hepdata.net/record/ins552757
- Independent PDF copy containing Table III: https://citeseerx.ist.psu.edu/document?doi=9357dccfcbe176b4cce5ad28c01b6731c597c533&repid=rep1&type=pdf
