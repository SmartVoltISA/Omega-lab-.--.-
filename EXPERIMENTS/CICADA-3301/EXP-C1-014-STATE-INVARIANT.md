# EXP-C1-014 — State Invariant Across Representation Spaces

**Status:** PLAUSIBLE / not proved
**Date:** 2026-08-28

## Objective
Test whether the useful invariant in Cicada is not a static key but a state transition: representation -> transform -> next representation.

## Confirmed observations

1. Gematria Primus maps 29 runes to indices 0..28 and the first 29 prime values. This gives a reversible representation layer.
2. Solved Vigenere material uses stateful key-position handling: F-skip means the key index does not advance at designated F positions; another solved reconstruction documents quote-based key reset. These are state transitions, not a static substitution.
3. The research RuneSolver contains prime and Fibonacci streams, but these are community tooling and must not be treated as proof of author intent.
4. The unresolved pages show a distribution compatible with a stream-like cipher, while word separators remain visible. This preserves structural constraints even when symbol values are encrypted.

## Current model

Let S_t be the state before symbol t, E_t the operation/edge type, and C_t the observed symbol/constraint.

    S_(t+1) = T(S_t, E_t, C_t)
    output_t = O(S_t, C_t)

A static-key model is the special case where S_t is just a periodic key index. The Cicada evidence permits a broader state-machine model.

## Critical test

A valid invariant must:

- reproduce at least two independently solved transitions;
- require no page-specific hand tuning;
- beat shuffled/null state sequences;
- preserve word-boundary and known-plaintext constraints;
- generate a new prediction on an unresolved page.

## Important correction

This does **not** prove that Cicada's creators used graph theory. The defensible claim is narrower: the puzzle contains repeated typed transitions and state-dependent transformations. A graph is a representation of those relations, not evidence of authorship intent.

## Next test

Construct a transition signature for each solved page using only observable state changes: key advance, skip, reset, direction, modulus, prime/totient stream, and output constraints. Cluster signatures and test whether unresolved pages can be assigned to a known transition family without fitting the plaintext.

## Expected decisive result

If one transition signature predicts a nontrivial property of an unresolved page before decryption, promote the invariant to STRONG PLAUSIBLE. If shuffled controls perform equally well, reject the model.
