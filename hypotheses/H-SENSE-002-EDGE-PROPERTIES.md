# H-SENSE-002 — Properties of Relations / Edges

Date: 2026-08-13
Status: **HYPOTHESIS / NOT TESTED**

## Core idea

In a graph representation, nodes are not the only carriers of structure. Relations (edges) may themselves have state/properties. A useful next research direction is to test whether edge properties are required to explain observed system behavior.

## Candidate edge properties

These are hypotheses, not assumed fundamentals:

- **strength** — how strongly a relation couples two nodes;
- **stiffness** — resistance of the relation to change or rewiring;
- **density** — how much interaction/connection capacity is concentrated in a relation or local edge neighborhood;
- **direction** — whether influence is symmetric or directed;
- **weight** — a general quantitative relation magnitude;
- **age / persistence** — how long a relation remains stable;
- **bandwidth / capacity** — how much state/information can pass through the relation per update;
- **energy cost** — physical or abstract cost associated with creating, maintaining, or changing the relation.

These terms must not be conflated. In particular, graph-theoretic edge weight is not automatically physical force, energy, density, or stiffness.

## Minimal question

Can a model with identical nodes but unweighted, memoryless edges reproduce the same behavior as a model whose edges carry state?

If not, which minimum edge property is necessary?

## Proposed progression

E0 — binary unweighted edges.
E1 — scalar edge weight.
E2 — directed weighted edges.
E3 — edge persistence/age.
E4 — edge memory/history.
E5 — edge update cost/stiffness.

For each level, attempt to remove the added property while preserving the target observations.

## Falsification principle

If every tested edge property can be eliminated without loss of the target behavior, the corresponding property is not necessary for that model class.

If a property is necessary, that establishes necessity only within the declared model and observation criterion; it does not establish that the property is a universal physical primitive.

## Important separation

"Density" needs an explicit definition before coding. It may refer to graph density (a property of a subgraph/network), spatial density, interaction-event density, or concentration of edge weight. These are different quantities and must not be silently merged.

"Strength" and "stiffness" also require operational definitions before experiment. A relation cannot be declared to have a property merely because the metaphor sounds physically plausible.

## Next experiment candidate

Ω-EDGE-001 should start with the smallest graph in which an edge state can make a measurable difference: two or three nodes, deterministic update rules, and a controlled edge-rewiring perturbation.

No experimental result is claimed by this document.
