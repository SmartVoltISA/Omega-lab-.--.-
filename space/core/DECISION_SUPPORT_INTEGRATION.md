# Decision Support Integration

The `DecisionSupport` organ is intentionally isolated from execution.

## Contract

`observe -> analyze -> options -> uncertainty -> recommendation -> human decision -> Guardian -> execution -> feedback`

The organ may create and explain a `DecisionBrief`. It records an explicit human decision when supplied. It does not execute an option and does not convert a recommendation into authority.

## Integration boundary

The organism runtime should expose DecisionSupport alongside Memory, Graph, Nervous, Guardian and Audit. A consequential brief is written to Memory and emitted on the event bus. Execution remains behind the existing Guardian/capability boundary.

## Required invariants

1. No option may execute merely because it was recommended.
2. A human decision must identify one presented option.
3. Decision provenance must remain recoverable.
4. Uncertainty must be retained rather than replaced with certainty.
5. Guardian remains the final authorization boundary.
