"""CICADA-GRAPH-001

Small dependency-free scaffold for the first structural graph test.
It intentionally does not infer missing edges: all input edges must carry
provenance/status supplied by the researcher.
"""
from collections import Counter, defaultdict, deque
import random

STATUSES = {"OBSERVED", "DERIVED", "HYPOTHESIZED", "REJECTED", "UNKNOWN"}


def validate_edges(edges):
    for e in edges:
        if len(e) != 5:
            raise ValueError("edge must be (source, relation, target, status, evidence)")
        source, relation, target, status, evidence = e
        if not source or not relation or not target:
            raise ValueError("source/relation/target must be non-empty")
        if status not in STATUSES:
            raise ValueError(f"invalid status: {status}")
        if not evidence:
            raise ValueError("every edge needs provenance/evidence")


def graph_stats(edges, accepted_statuses=("OBSERVED", "DERIVED")):
    validate_edges(edges)
    accepted = [e for e in edges if e[3] in accepted_statuses]
    out_degree = Counter()
    in_degree = Counter()
    relation_counts = Counter()
    nodes = set()
    adjacency = defaultdict(set)

    for source, relation, target, *_ in accepted:
        nodes.update((source, target))
        out_degree[source] += 1
        in_degree[target] += 1
        relation_counts[relation] += 1
        adjacency[source].add(target)
        adjacency[target].add(source)

    # Undirected connected components for structural diagnostics.
    seen = set()
    components = []
    for start in sorted(nodes):
        if start in seen:
            continue
        q = deque([start])
        seen.add(start)
        comp = []
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adjacency[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        components.append(sorted(comp))

    return {
        "nodes": len(nodes),
        "edges": len(accepted),
        "components": len(components),
        "largest_component": max((len(c) for c in components), default=0),
        "out_degree": dict(out_degree),
        "in_degree": dict(in_degree),
        "relation_counts": dict(relation_counts),
    }


def relation_motifs(edges, length=2, accepted_statuses=("OBSERVED", "DERIVED")):
    """Count relation-pairs sharing a target/source junction."""
    accepted = [e for e in edges if e[3] in accepted_statuses]
    incoming = defaultdict(list)
    outgoing = defaultdict(list)
    for s, r, t, *_ in accepted:
        outgoing[s].append((r, t))
        incoming[t].append((s, r))

    motifs = Counter()
    if length != 2:
        raise ValueError("only length=2 motifs are implemented")
    for node in set(incoming) & set(outgoing):
        for _, rin in incoming[node]:
            for rout, _ in outgoing[node]:
                motifs[(rin, rout)] += 1
    return dict(motifs)


def degree_preserving_null(edges, seed=3301, accepted_statuses=("OBSERVED", "DERIVED")):
    """Null control: shuffle targets within each relation.

    Node identities and relation counts are preserved while specific
    source→target pairings are randomized. This is a deliberately simple
    baseline; future rounds should add stronger degree-preserving controls.
    """
    rng = random.Random(seed)
    accepted = [e for e in edges if e[3] in accepted_statuses]
    by_relation = defaultdict(list)
    for e in accepted:
        by_relation[e[1]].append(e)

    result = []
    for relation, group in by_relation.items():
        targets = [e[2] for e in group]
        rng.shuffle(targets)
        for e, target in zip(group, targets):
            result.append((e[0], relation, target, e[3], "NULL_SHUFFLED_TARGET"))
    return result


if __name__ == "__main__":
    # Minimal smoke test; replace with a sourced corpus before interpreting results.
    demo = [
        ("image", "CONTAINS", "payload", "OBSERVED", "primary-artifact"),
        ("payload", "DERIVES", "url", "DERIVED", "reproduction-01"),
        ("url", "POINTS_TO", "endpoint", "OBSERVED", "primary-artifact"),
    ]
    print(graph_stats(demo))
    print(relation_motifs(demo))
    print(graph_stats(degree_preserving_null(demo)))
