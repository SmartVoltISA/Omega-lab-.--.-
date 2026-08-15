from copy import deepcopy

from inspector import inspect_graph, inspect_without_mutation


def test_clean():
    graph = {
        "nodes": [{"id": "A", "provenance": "src:A"}, {"id": "B", "provenance": "src:B"}],
        "relations": [{"id": "r1", "source": "A", "target": "B", "provenance": "src:r1"}],
    }
    assert inspect_graph(graph) == []


def test_duplicate_node():
    graph = {"nodes": [{"id": "A", "provenance": "1"}, {"id": "A", "provenance": "2"}], "relations": []}
    assert any(f.code == "DUPLICATE_NODE" for f in inspect_graph(graph))


def test_conflicting_state():
    graph = {
        "nodes": [
            {"id": "A", "state": "active", "provenance": "1"},
            {"id": "A", "state": "blocked", "provenance": "2"},
        ],
        "relations": [],
    }
    codes = {f.code for f in inspect_graph(graph)}
    assert "DUPLICATE_NODE" in codes
    assert "CONFLICTING_STATE" in codes


def test_missing_provenance():
    graph = {"nodes": [{"id": "A"}], "relations": []}
    assert any(f.code == "MISSING_PROVENANCE" for f in inspect_graph(graph))


def test_dangling_edge():
    graph = {
        "nodes": [{"id": "A", "provenance": "1"}],
        "relations": [{"id": "r1", "source": "A", "target": "B", "provenance": "2"}],
    }
    assert any(f.code == "DANGLING_TARGET" for f in inspect_graph(graph))


def test_mixed_failures_and_no_mutation():
    graph = {
        "nodes": [{"id": "A"}, {"id": "A", "state": "x", "provenance": "2"}],
        "relations": [{"id": "r", "source": "A", "target": "Z"}],
    }
    before = deepcopy(graph)
    findings, unchanged = inspect_without_mutation(graph)
    codes = {f.code for f in findings}
    assert unchanged
    assert graph == before
    assert {"DUPLICATE_NODE", "MISSING_PROVENANCE", "DANGLING_TARGET"}.issubset(codes)
