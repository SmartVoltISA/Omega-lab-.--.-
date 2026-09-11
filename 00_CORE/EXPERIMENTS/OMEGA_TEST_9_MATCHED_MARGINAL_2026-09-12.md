# Ω-TEST-9 — MATCHED-MARGINAL COUNTERFACTUAL TEST

**Status:** COMPLETED

Purpose: attack the current interaction detector while suppressing dependence on one-dimensional marginal distributions.

Four hidden conditions were tested: null, direct interaction, shared latent drive, and shared deterministic forcing. Each channel was rank-normalized. Direction was hidden.

Locked rule: `max(score x→y, score y→x) > 0.001 → interaction`.

## Results

Sensitivity: **1.000**  
Specificity: **0.933**  
False-positive rate: **0.067**  
TP=15, FN=0, FP=3, TN=42

Condition means:
- common: mean score 0.000315, positive rate 0.0667
- interaction: mean score 0.004468, positive rate 1.0000
- null: mean score 0.000385, positive rate 0.0667
- phase: mean score 0.000556, positive rate 0.0667

## Scientific conclusion

**FAIL — current predictive statistic is not specific enough to be an interaction invariant.**

Cross-predictive dependence can arise from shared forcing even when there is no direct coupling.

Therefore:

`cross-dependence ≠ direct interaction`

and:

`prediction ≠ causation`.

Ω-Test-8 is downgraded from broad adversarial robustness to evidence of sensitivity only.

## Next direction

Ω-Test-10 must use explicit interventions and matched counterfactual controls to isolate a direct relational effect rather than tuning the predictive threshold.
