import unittest

from space.organs.audio_sequence_graph import AudioSequenceGraphBuilder, SoundCandidateNode


class AudioSequenceGraphTests(unittest.TestCase):
    def test_orders_nodes_and_connects_next(self):
        builder = AudioSequenceGraphBuilder()
        b = SoundCandidateNode("b", "a", 0.7, 0.10, 0.20)
        a = SoundCandidateNode("a", "m", 0.8, 0.00, 0.10)
        graph = builder.build([b, a])
        self.assertEqual([n.node_id for n in graph.nodes], ["a", "b"])
        self.assertEqual(len(graph.relations), 1)
        self.assertEqual(graph.relations[0].relation, "NEXT")
        self.assertEqual(graph.relations[0].source, "a")
        self.assertEqual(graph.relations[0].target, "b")

    def test_candidates_remain_unconfirmed(self):
        graph = AudioSequenceGraphBuilder().build([
            SoundCandidateNode("x", "s", 0.51, 0.0, 0.05)
        ])
        self.assertFalse(graph.nodes[0].confirmed)

    def test_duplicate_id_rejected(self):
        node = SoundCandidateNode("x", "s", 0.5, 0.0, 0.1)
        with self.assertRaises(ValueError):
            AudioSequenceGraphBuilder().build([node, node])

    def test_invalid_confidence_rejected(self):
        with self.assertRaises(ValueError):
            AudioSequenceGraphBuilder().build([
                SoundCandidateNode("x", "s", 1.2, 0.0, 0.1)
            ])


if __name__ == "__main__":
    unittest.main()
