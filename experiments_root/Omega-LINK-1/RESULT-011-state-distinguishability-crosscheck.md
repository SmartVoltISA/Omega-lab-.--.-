# RESULT-011 — STATE-DISTINGUISHABILITY CROSS-CHECK

## Status
Confirmed computational result on four controlled transition rules.

## Question
Is the number of distinguishable next-state classes determined by history depth alone, or by the transition rule?

## Verification run
- GitHub Actions run: Ω-LINK-1 #61
- Commit: `e542b24383ebbb409933764547f4e5f4d5508196`
- Event: `workflow_dispatch`
- Conclusion: `success`
- Artifact: `omega-link-1-results`
- The workflow executed both the original state-distinguishability experiment and the rule cross-check.

## Controlled rules
1. PARITY_BINARY
2. FIRST_BINARY
3. CONSTANT_BINARY
4. SUM_MOD3

## Result matrix

| Rule | N=1 | N=2 | N=3 | N=4 | N=5 | N=6 |
|---|---:|---:|---:|---:|---:|---:|
| PARITY_BINARY | 2 | 2 | 2 | 2 | 2 | 2 |
| FIRST_BINARY | 2 | 2 | 2 | 2 | 2 | 2 |
| CONSTANT_BINARY | 1 | 1 | 1 | 1 | 1 | 1 |
| SUM_MOD3 | 3 | 3 | 3 | 3 | 3 | 3 |

For binary history space the total number of histories is 2^N. For the ternary SUM_MOD3 construction it is 3^N.

## Observation
History-space size grows with depth, while the number of distinct next-state classes remains constant across depth for each controlled rule. The number of classes differs between rules.

Therefore, in these controlled constructions:

**memory/history depth is not identical to the number of distinguishable next-state classes.**

## Boundary
This is not a universal theorem about arbitrary systems. It is a validated property of the tested controlled constructions and a methodological separation between two measurements.

## Research chain
RESULT-010 established recovery of known minimal history depth.
RESULT-011 now separates history-space growth from next-state distinguishability and confirms the distinction across multiple rules.

## Next question
Test whether the number of distinguishable next-state classes can be related to a minimal sufficient state representation, rather than directly to raw history depth.