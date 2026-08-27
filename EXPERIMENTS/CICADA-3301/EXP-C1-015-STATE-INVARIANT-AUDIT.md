# EXP-C1-015 — State invariant audit

Date: 2026-08-28
Status: negative/partial result

## Question
Does the confirmed F-skip behavior imply a common state-transition invariant that can predict unresolved LP2 pages?

## Evidence
The community reconstruction documents F-skip on solved Vigenere pages: rune F (Gematria value 0) does not advance the key stream. This is a stateful decoding rule, not proof of graph theory. Current repositories disagree on the scope of solved LP2; the more conservative archive marks LP2 pages 17–74 as unsolved and explicitly says the reported P56/P57 totient solution is not independently verified.

## Audit result
F-skip proves only that at least one solved-page cipher has state-dependent key advancement. It does NOT establish a cross-page invariant, a graph mechanism, or an endpoint-generation function.

The 2025/2026 "95% solution" claim based on Fibonacci/Lucas master indices remains a candidate model. It reproduces its own selected solved-page constraints, but it is not an independent confirmation of author intent or of the unresolved LP2 pages.

## Decision
Do not promote the state-machine hypothesis above PLAUSIBLE.
Do not use the claimed 95% algorithm as a foundation for generating an endpoint.

## Next test
Use only independently verified solved plaintext/ciphertext pairs. Derive state-transition signatures (advance, skip, reset, direction, modulus) and test whether one rule predicts a held-out page without page-specific tuning. Compare against shuffled/null state sequences.

## Key observation
The strongest current structural fact remains: Cicada repeatedly couples content with numerical structure and authentication/verification. The stronger claim — that the same transition function connects all rounds — is still unproven.
