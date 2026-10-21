# Ω-SELF-005 — Candidate selection and generalization stress test

**Status:** PILOT COMPLETE — exploratory, not confirmatory  
**Run date:** 2026-10-21  
**Branch:** `experiment/omega-self-005-generalization`

## Question
Does selecting a hand-coded policy from a candidate pool improve performance over a fixed baseline, a feedback heuristic, and one randomly selected candidate when evaluated on held-out seeds and one deliberately unseen environment family?

## Preregistered protocol (as implemented)
- Training families: `rapid`, `slow`, `surprise`; 40 seeds per family.
- Held-out evaluation: 120 seeds per family over `rapid`, `slow`, `surprise`, and `unseen_drift` (a gradual-degradation family not used in candidate selection).
- Horizon: 300 steps per episode.
- Candidate pool: 24 policies; fixed random seed 20261021.
- Selection score: 0.75 × full-survival fraction + 0.25 × mean energy / 100.
- Four primary comparisons: fixed baseline, feedback heuristic, best training-scored candidate, and one randomly selected candidate. All 24 candidates are also evaluated on test seeds to inspect the candidate-score distribution.

## Results
Each primary condition has 480 held-out episodes (120 seeds × 4 families).

| Condition | Full survival | Mean survival steps | Mean energy | Final energy | Composite score |
|---|---:|---:|---:|---:|---:|
| A — fixed baseline | 100% | 300.00 | 36.78 | 34.45 | 0.84194 |
| B — feedback heuristic | 100% | 300.00 | 48.19 | 47.51 | 0.87047 |
| C — selected candidate | 100% | 300.00 | 63.24 | 63.14 | 0.90810 |
| D — random candidate | 100% | 300.00 | 39.75 | 37.36 | 0.84938 |

Selected policy: `candidate_20` (energy threshold 63.66, stress threshold 16.05, cue disabled). Random comparison: `candidate_19` (energy threshold 37.84, stress threshold 9.81, cue disabled).

Across all 24 candidates, the best held-out score was 0.90810, the median was 0.84356, and the randomly selected candidate scored 0.84938.

## Interpretation
- All four primary conditions survived every episode. **Survival therefore saturated and cannot distinguish the policies in this run.**
- The selected candidate's composite score was higher mainly because it maintained more energy. This is evidence that candidate selection can find a better parameter setting for this particular simulator and scoring rule, not evidence of open-ended learning or intelligence.
- The randomly selected candidate did not match the selected policy, but the comparison uses only one random draw. The distribution of all 24 candidates is included so this limitation is visible.
- The unseen gradual-drift family showed the same qualitative ordering in mean energy, but it is only one designed shift and is not broad out-of-distribution validation.

## Limitations and next test
1. Toy hand-coded policies and simulator; no claim about consciousness, subjective experience, or general intelligence.
2. No confidence intervals or formal significance tests in this pilot.
3. No compute-matched search baseline; search receives extra evaluation compute.
4. The objective is hand-selected and partly rewards energy conservation; a policy can score well without demonstrating useful task completion.
5. The environment remains simple and the survival metric hit a ceiling.

**Decision:** Keep as an exploratory result. Next experiment should make task output/productivity an explicit objective, tune environment difficulty before examining the test set, compare against a compute-matched random-search baseline, and report paired uncertainty intervals. Do not promote this result as proof of generalization.
