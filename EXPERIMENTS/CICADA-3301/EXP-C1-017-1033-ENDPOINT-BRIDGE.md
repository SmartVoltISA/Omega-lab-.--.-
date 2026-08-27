# EXP-C1-017 — 1033 as Cross-Layer Bridge / Endpoint Label

**Status:** STRONG PLAUSIBLE structural invariant; endpoint semantics not yet proved.
**Date:** 2026-08-28

## Observation

The 5x5 Liber Primus magic square has row/column/diagonal constant 1033. The same matrix is reported in OOB data, so 1033 is a cross-channel invariant.

Independently, the documented 2014 walkthrough shows the first onion service serving an image named `1033.jpg`. The walkthrough then extracts a PGP-signed payload from that image and continues to a second onion service. Thus the literal token `1033` occurs as a filename/identifier at an actual transition node, not only as an arithmetic row-sum.

## Why this matters

This is stronger than the earlier claim `3301 -> 1033` by digit reversal. The useful relation is instead:

    MAGIC SQUARE invariant = 1033
              |
              +----> 1033.jpg (2014 transition artifact)

The same token therefore appears in two different representation spaces:

    numerical structure -> file identifier -> hidden signed payload -> next endpoint

This is exactly the type of cross-space bridge predicted by the graph model.

## Important restraint

We have NOT proved that the magic-square constant generated the filename. The file could have been independently labelled 1033. We therefore treat `1033` as a candidate bridge/identifier, not a recovered key.

We also do not treat 3301 -> 1033 as an established transformation. Digit reversal is only an observation unless it predicts an independent downstream value.

## Falsifiable tests

1. Enumerate every occurrence of `1033` in primary 2014 artifacts and classify whether it is generated, supplied, or incidental.
2. Determine whether the 1033.jpg artifact is cryptographically/structurally connected to the 1033 magic-square data rather than merely sharing a label.
3. Test the other magic-square constants (3301 and 1033) against filenames, URLs, page numbers, hash fragments, and cryptographic parameters in the same round.
4. Check whether the same numeric invariant-to-identifier transition occurs elsewhere in 2012/2013/2014.
5. Require a downstream prediction before promoting 1033 to KEY/ADDRESS status.

## Current conclusion

The graph hypothesis gains a concrete bridge candidate: `1033` appears both as a structural invariant and as an identifier at a documented transition artifact. This is stronger than a generic claim that Cicada uses numbers, but it remains insufficient to infer the final endpoint or key.
