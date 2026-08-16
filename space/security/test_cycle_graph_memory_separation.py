import unittest

from space.core.graph import GraphCore
from space.integration.space_memory_guardian_cycle import SpaceMemoryGuardianCycle


class CycleGraphMemorySeparationTests(unittest.TestCase):
    def test_graph_and_cycle_are_independent_domains(self):
        graph = GraphCore()
        graph.upsert_node("node-a")
        graph.upsert_node("node-b")
        graph.connect("node-a", "node-b", "ordinary")

        cycle = SpaceMemoryGuardianCycle()
        cycle_snapshot = cycle.cycle_snapshot()

        self.assertEqual(graph.whole_state()["edge_count"], 1)
        self.assertEqual(cycle_snapshot["states"], [])
        self.assertEqual(cycle_snapshot["relations"], [])

    def test_cycle_has_no_graph_reference(self):
        cycle = SpaceMemoryGuardianCycle()
        forbidden = [name for name in dir(cycle) if "graph" in name.lower() and not name.startswith("_")]
        self.assertEqual(forbidden, ["graph_snapshot", "inspect_feedback_graph"])

    def test_no_cross_domain_combination_method_exists(self):
        cycle = SpaceMemoryGuardianCycle()
        for name in ("merge_graph", "attach_graph", "connect_graph", "graph_cycle", "materialize_graph"):
            self.assertFalse(hasattr(cycle, name), name)


if __name__ == "__main__":
    unittest.main()
