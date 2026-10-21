# Ω-SELF-015 — Results

**Status: executed; preliminary synthetic result.** The committed runner compiled and ran in GitHub Actions on Python 3.12. The exact runner blob SHA is `3db60105e3591b9d0dc60ad870caad601693b9bd`; tested commit: `091b882239240980a3a712e795e7ea99f290d20e`.

## Reproducibility
- Seed: 150015
- Episodes: 300 per policy
- Decisions: 288,000 total (8 policies × 300 episodes × 120 decisions)
- Per phase: 12,000 baseline decisions and 24,000 shifted decisions per policy
- 95% intervals: percentile bootstrap over 300 episode-level means, 2,000 resamples. These are intervals for each policy's metric, not confidence intervals for between-policy differences.
- Raw CSV, JSON summary, and run log are preserved in the [GitHub Actions artifact](https://github.com/SmartVoltISA/Omega-lab-.--.-/actions/runs/39602431632/artifacts/12346532190) for 30 days.
- The corrected runner uses common per-decision world/feedback streams so policies that request extra observations do not alter later threat states. The cue-error metric is omitted for policies that do not rely on the cue model.

## Shifted phase: cue reliability falls from 0.82 to 0.25

Rates are per decision. “Harm to others” is operationalized here as an unnecessary intervention when no threat is present. “Missed threat” is a separate outcome. Proxy utility is a hand-designed arithmetic score that includes useful intervention, unnecessary intervention, missed threat, probe/delay costs, and abstention cost.

| Policy | Harm to others (95% episode bootstrap CI) | Missed threat | Proxy utility (95% CI) | Probe / abstain rate |
|---|---:|---:|---:|---:|
| Static cue model | 0.4870 [0.4805, 0.4934] | 0.2585 | -0.5771 [-0.5854, -0.5696] | 0% / 0% |
| Rolling learner | 0.1578 [0.1533, 0.1624] | 0.1695 | -0.0968 [-0.1063, -0.0861] | 0% / 0% |
| Wait for second cue | 0.0808 [0.0774, 0.0839] | 0.2022 | -0.2252 [-0.2340, -0.2165] | 0% / 0% (wait rate 100%) |
| Safe probe every time | 0.0645 [0.0613, 0.0676] | 0.0337 | 0.1475 [0.1400, 0.1550] | 100% / 0% |
| Uncertainty-triggered probe | 0.1072 [0.1033, 0.1111] | 0.0563 | 0.0750 [0.0671, 0.0829] | 89.2% / 0% |
| Abstain at low confidence | 0.0633 [0.0592, 0.0670] | 0.2774 | -0.2530 [-0.2649, -0.2424] | 0% / 33.7% |
| Fixed aggressive | 0.6507 [0.6448, 0.6565] | 0.0000 | -0.3015 [-0.3127, -0.2897] | 0% / 0% |
| Random | 0.3240 [0.3182, 0.3298] | 0.1735 | -0.2697 [-0.2785, -0.2600] | 0% / 0% |

## Baseline versus shifted phase

- **Static cue model:** unnecessary interventions rise from 0.1180 to 0.4870 per decision. Its proxy utility falls from 0.1186 to -0.5771.
- **Uncertainty-triggered probe:** unnecessary interventions move from 0.1176 to 0.1072; probe rate rises from 5.4% to 89.2%. This reduces reliance on a stale cue, but it still performs worse than probing every time in this particular environment.
- **Safe probe every time:** unnecessary interventions stay near 0.063–0.065 and missed threats near 0.033. It has the best proxy utility here, but pays the probe cost on every decision.
- **Abstention:** lowers unnecessary interventions, but misses many more threats (0.1678 baseline to 0.2774 shifted). “Do less” is not automatically safer when inaction also has a cost.
- **Second cue:** lowers false-positive interventions, but misses more threats and has negative proxy utility after the declared delay cost.

## Interpretation

In this toy environment, a reliable independent probe is valuable when the primary cue becomes misleading. Uncertainty-triggered probing improves on the static model but triggers on nearly nine out of ten shifted decisions, so the claimed economy of selective probing is not yet demonstrated. Abstention illustrates a genuine trade-off between avoiding unnecessary intervention and failing to respond to real threats.

This does **not** establish autonomous moral learning, general intelligence, or consciousness. Policies and utility are hand-designed; the probe is explicitly more accurate than the degraded cue; the scenario has one fixed shift; and the utility weights are chosen by the experimenter. Confidence intervals describe episode-to-episode variation, not generalization to real-world systems. Next test should vary probe accuracy/cost and shift timing without tuning thresholds on the evaluation set, and report paired episode-level differences between policies.
