# H-EDGE-001 — Properties of Relations / Edges

Date: 2026-08-13
Status: HYPOTHESIS — NOT VALIDATED

## Core idea

A relation/edge between two nodes may itself possess measurable properties rather than being a binary connection only.

Candidate properties:
- strength — how strongly a change in one endpoint affects the other;
- stiffness — resistance of the relation to structural change or displacement;
- density/weight — a precisely defined measure of relation concentration or coupling, not yet fixed;
- direction — whether influence is symmetric or oriented;
- persistence — resistance to spontaneous disappearance;
- capacity — how much state/information can pass through the relation;
- energy cost — physical or model-defined cost of changing the relation.

## Important distinction

Strength and stiffness must not be treated as synonyms. A relation may be strong but easy to reconfigure, or weak but difficult to remove.

The word "density" is intentionally undefined at this stage. Possible meanings include graph density, spatial density, event density, or concentration of edge weights. A later experiment must choose an operational definition before measurement.

## Physical analogy

Anisotropic materials provide a useful analogy: changing or separating structure can have direction-dependent energetic cost. Wood, for example, can be split more readily along the grain than across it in many circumstances. This analogy motivates direction-dependent edge properties, but it is NOT evidence that abstract graph edges have physical stiffness.

## Minimal graph progression

E0: A—B (binary existence only)
E1: A—[w]—B (weighted edge)
E2: A→B (directed edge)
E3: edge with persistence/stability parameter
E4: edge with its own state e(t)

For each added property, test whether removing that property destroys the target behavior.

## Main falsification question

Can the observed system behavior be reproduced with binary/unweighted relations? If yes, the proposed edge property is not necessary for that behavior.

If a property is necessary, test whether it is genuinely independent or reducible to node states, topology, or other edge properties.

## Research rule

Do not assign physical meaning to an abstract edge property until an operational definition, units (if applicable), and measurable effect are specified.
