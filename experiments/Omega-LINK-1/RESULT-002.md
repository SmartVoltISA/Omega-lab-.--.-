# Ω-LINK-1 — RESULT-002

**Status:** OBSERVED RESULT / not a universal law
**Run:** 31778380650
**Commit:** 16439368aff52255367c98e1d3f1a7fe23611c54

## Observation

Influence-1 measured the effect of removing each individual edge while keeping the node set and graph transition rules fixed.

For G1 the number of lost reachable source→target pairs was:

- `A→B`: 2
- `B→C`: 3
- `C→D`: 2
- `A→D`: 0

For G2 every tested edge produced a loss of 1 reachable pair:

- `A→B`: 1
- `A→C`: 1
- `B→D`: 1
- `C→D`: 1

## Observation

Equal node count and equal edge count do not imply equal distribution of structural influence among edges.

An edge can exist without contributing uniquely to global reachability when an alternative path preserves the same reachable pairs. Conversely, another edge in the same graph can account for several reachable pairs.

## Interpretation boundary

The measured influence is a property of the tested edge within its surrounding topology and the chosen reachability definition. It is not yet a universal definition of causal importance or of the essence of a relation.

## Next question

Can edge influence be separated into local transition loss and global structural loss, and does the distinction remain stable when alternative paths, graph size, and topology are varied?
