# First-Class Edge Model v1.0

## Purpose

A connection is not merely a pointer between two nodes. It is an independently inspectable object.

## Edge structure

```text
EDGE
├── id
├── source
├── target
├── type
├── provenance
└── history/state (future extension)
```

## Meaning

- `source` — where the relation starts;
- `target` — where it ends;
- `type` — what the relation means (`supports`, `depends_on`, `derived_from`, etc.);
- `provenance` — where the relation came from;
- `id` — stable identity of the relation itself.

## What the Inspector verifies

1. Edge has an identity.
2. Source node exists.
3. Target node exists.
4. Edge has a semantic type.
5. Edge has provenance.
6. Edge identity is not duplicated.
7. Identical source-target-type edges are not duplicated accidentally.
8. Inspection does not mutate the graph.

## Why this matters

Without first-class edges, a graph can contain nodes but cannot reliably answer why two nodes are connected, what the connection means, or where that connection came from.

With first-class edges:

`node → edge → node`

becomes an auditable unit.

## Completion gate

The edge layer is considered **implemented** when the Inspector code, tests and CI all pass the edge integrity suite.

It is considered **validated for Space integration** only after the same checks are run against an actual Space memory export rather than synthetic fixtures alone.
