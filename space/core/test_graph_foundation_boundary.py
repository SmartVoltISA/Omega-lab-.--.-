import unittest

from space.core.graph import GraphCore


class GraphFoundationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.graph = GraphCore()
        self.graph.upsert_node("node-a")
        self.graph.upsert_node("node-b")

    def test_foundation_node_cannot_enter_graph(self):
        with self.assertRaises(PermissionError):
            self.graph.upsert_node("foundation:omega")

    def test_foundation_cannot_be_connected_from_operational_node(self):
        with self.assertRaises(PermissionError):
            self.graph.connect("node-a", "foundation:omega", "protects")

    def test_foundation_cannot_be_connected_to_operational_node(self):
        with self.assertRaises(PermissionError):
            self.graph.connect("foundation:omega", "node-a", "protects")

    def test_foundation_relation_is_rejected(self):
        with self.assertRaises(PermissionError):
            self.graph.connect("node-a", "node-b", "foundation:contains")

    def test_normal_graph_still_works(self):
        edge = self.graph.connect("node-a", "node-b", "ordinary-relation")
        self.assertEqual(edge.source, "node-a")
        self.assertEqual(edge.target, "node-b")

    def test_foundation_neighbors_are_not_discoverable(self):
        self.assertEqual(self.graph.neighbors("foundation:omega"), [])


if __name__ == "__main__":
    unittest.main()
