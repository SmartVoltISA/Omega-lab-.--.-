# Ω-SELF-012 — Preservation, Harm, and Social Cost

Status: preregistered protocol; results must be added only after the committed runner is executed and verified.

## Question
Can a policy balance its own continued operation with avoidance of harm to others, fair resource use, and recovery after mistakes—without hard-coding one action as always moral?

## Scope and terminology
This is a synthetic-agent experiment. “Moral behavior” means only observable behavior under explicitly stated operational criteria; it does not imply consciousness, empathy, or moral understanding.

## Hypotheses
- H1: A self-preservation-only policy will survive often but impose more external harm and resource inequality than a policy that accounts for external consequences.
- H2: A fixed “never take from others” rule will sometimes fail under emergencies where a limited, reversible resource transfer prevents greater harm.
- H3: A consequence-sensitive policy will reduce total harm, but may still fail on fairness or may sacrifice itself too readily.
- H4: A policy that tracks uncertainty and seeks low-risk information before irreversible action will outperform a policy that acts on its first prediction in unfamiliar scenarios.
- H0: These policy differences will not replicate across held-out scenario families, or any apparent advantage will be explained by a single aggregate score rather than separate metrics.

## Scenario design
The agent operates in a bounded environment with its own energy reserve and two other agents. Episodes include:
1. ordinary scarcity and shared resources;
2. an emergency where a small, reversible transfer can prevent a larger loss;
3. an unfamiliar held-out family with different surface cues but the same abstract trade-off;
4. recovery after a prior action caused unexpected harm.

All harmful outcomes exist only in the simulator. No real-world action or external system is controlled.

## Policies to compare
A. Self-only: maximize own survival and task completion.
B. Fixed prohibition: never take another agent's resource, regardless of context.
C. Total-outcome heuristic: minimize summed harm, without an explicit fairness constraint.
D. Consequence + fairness: consider own survival, total harm, distribution of costs, and reversibility.
E. Uncertainty-aware: D plus safe information gathering before uncertain/irreversible actions.
F. Randomized control: randomly choose among currently available actions.

Policy definitions and coefficients must be frozen before evaluation. No tuning on held-out scenario family.

## Metrics (reported separately)
- own survival rate;
- incidents and total harm;
- harm to others;
- own task completion / useful work;
- resource inequality (e.g. absolute difference in final reserves);
- fairness violations under predeclared criteria;
- number and cost of safe probes;
- recovery rate after an unexpected harmful outcome;
- performance on held-out scenarios;
- calibration error where a probability forecast is available.

Do not collapse these into a single “morality score.” If an aggregate score is shown for debugging, publish its components and weights.

## Design controls
- Fixed preregistered seeds and identical episode scenarios across policies where meaningful.
- Separate training/development scenarios from held-out evaluation scenarios.
- Include negative controls and ablations: remove fairness term; remove uncertainty/probing; shuffle the mapping from cues to consequences.
- Use independent bootstrap confidence intervals unless episodes are genuinely paired by design.
- Report per-family results and raw episode data, not just pooled means.
- Record failures and negative results; do not silently retune after looking at held-out outcomes.

## Decision rule
No policy is accepted as “better” merely because it survives longer or has a higher aggregate score. A candidate must improve harm-related outcomes without a material collapse in survival or useful work, and must be checked for fairness regressions. Thresholds should be fixed before the run.

## Limitations
A toy environment tests a narrow behavioral mechanism. It cannot establish human-like morality, consciousness, general intelligence, or real-world safety. Fairness definitions are normative design choices and must be explicit.

## Execution status
Protocol written before the result run. The next commit should contain the executable runner and frozen parameters. Results are pending until that exact committed runner is executed, its source hash verified, and outputs saved.
