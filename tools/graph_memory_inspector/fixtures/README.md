# Validation fixtures

The first validation set must contain six deterministic fixtures:

- `clean` — valid graph, no findings expected;
- `duplicate_node` — two records claiming the same identity;
- `conflicting_state` — same entity with incompatible state claims;
- `missing_provenance` — relation or node without provenance;
- `dangling_edge` — relation references a missing node;
- `mixed_failures` — multiple defects in one graph.

Each fixture must have an expected finding set and a mutation checksum/hash so that the inspector can be tested for read-only behaviour.