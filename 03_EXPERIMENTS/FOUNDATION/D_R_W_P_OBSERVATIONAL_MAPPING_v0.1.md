# D/R/W/P OBSERVATIONAL MAPPING v0.1

Status: WORKING EXPERIMENT / NOT CANONICAL
Date: 2026-08-28

## Purpose
Map D/R/W/P hypotheses onto the neutral machine without assigning capability semantics to machine instructions.

## Neutral machine observables

The machine exposes only:
- configuration sequence;
- symbol values;
- control-state values;
- positions;
- rule application trace;
- termination/repetition.

No observable is named as distinction, relation, will, prohibition, state, memory, or choice.

## Mapping rule

A primitive hypothesis is represented as a constraint over machine data, not as a machine operation.

D: requires at least two observationally non-identical configurations or values.
R: requires an ordered/typed correspondence between components across configurations.
W: requires a deterministic selector function over a set of candidates.
P: requires a predicate that excludes at least one otherwise executable transition.

These are observer-side predicates only. They are not inserted into the generator.

## Minimality protocol

For each primitive budget B subset {D,R,W,P}:
1. generate neutral machines independently of B;
2. execute all machines within the fixed bound;
3. evaluate observational predicates;
4. record the smallest witness and its trace;
5. rerun after random alpha-renaming of all primitive labels;
6. compare against matched null machines;
7. require exact replay of the witness.

## Important limitation

The mapping defines operational observables for the hypotheses. It does not prove that an observable is metaphysically identical to the named concept. Therefore any positive result is a construction/reducibility result only.

## Required output

For each capability and primitive budget:
- witness trace;
- budget;
- depth;
- observer result;
- null result;
- permutation result;
- replay result;
- status.

No canonical change until independent replay.
