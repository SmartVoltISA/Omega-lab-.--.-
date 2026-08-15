import unittest
from copy import deepcopy

from inspector import inspect_graph, inspect_without_mutation


class GraphMemoryInspectorTests(unittest.TestCase):
    def test_clean(self):
        graph = {
            "nodes": [{"id": "A", "provenance": "src:A"}, {"id": "B", "provenance": "src:B"}],
            "relations": [{"id": "r1", "source": "A", "target": "B", "type": "supports", "provenance": "src:r1"}],
        }
        self.assertEqual(inspect_graph(graph), [])

    def test_duplicate_node(self):
        graph = {"nodes": [{"id": "A", "provenance": "1"}, {"id": "A", "provenance": "2"}], "relations": []}
        self.assertTrue(any(f.code == "DUPLICATE_NODE" for f in inspect_graph(graph)))

    def test_conflicting_state(self):
        graph = {
            "nodes": [
                {"id": "A", "state": "active", "provenance": "1"},
                {"id": "A", "state": "blocked", "provenance": "2"},
            ],
            "relations": [],
        }
        codes = {f.code for f in inspect_graph(graph)}
        self.assertIn("DUPLICATE_NODE", codes)
        self.assertIn("CONFLICTING_STATE", codes)

    def test_missing_provenance(self):
        graph = {"nodes": [{"id": "A"}], "relations": []}
        self.assertTrue(any(f.code == "MISSING_PROVENANCE" for f in inspect_graph(graph)))

    def test_dangling_edge(self):
        graph = {
            "nodes": [{"id": "A", "provenance": "1"}],
            "relations": [{"id": "r1", "source": "A", "target": "B", "type": "supports", "provenance": "2"}],
        }
        self.assertTrue(any(f.code == "DANGLING_TARGET" for f in inspect_graph(graph)))

    def test_edge_requires_identity_and_type(self):
        graph = {
            "nodes": [{"id": "A", "provenance": "1"}, {"id": "B", "provenance": "2"}],
            "relations": [{"source": "A", "target": "B", "provenance": "3"}],
        }
        codes = {f.code for f in inspect_graph(graph)}
        self.assertIn("MISSING_RELATION_ID", codes)
        self.assertIn("MISSING_RELATION_TYPE", codes)

    def test_duplicate_edge_identity_and_signature(self):
        graph = {
            "nodes": [{"id": "A", "provenance": "1"}, {"id": "B", "provenance": "2"}],
            "relations": [
                {"id": "r1", "source": "A", "target": "B", "type": "supports", "provenance": "3"},
                {"id": "r1", "source": "A", "target": "B", "type": "supports", "provenance": "4"},
            ],
        }
        codes = {f.code for f in inspect_graph(graph)}
        self.assertIn("DUPLICATE_RELATION", codes)
        self.assertIn("DUPLICATE_EDGE_SIGNATURE", codes)

    def test_mixed_failures_and_no_mutation(self):
        graph = {
            "nodes": [{"id": "A"}, {"id": "A", "state": "x", "provenance": "2"}],
            "relations": [{"id": "r", "source": "A", "target": "Z", "type": "supports"}],
        }
        before = deepcopy(graph)
        findings, unchanged = inspect_without_mutation(graph)
        codes = {f.code for f in findings}
        self.assertTrue(unchanged)
        self.assertEqual(graph, before)
        self.assertTrue({"DUPLICATE_NODE", "MISSING_PROVENANCE", "DANGLING_TARGET"}.issubset(codes))


if __name__ == "__main__":
    unittest.main()
