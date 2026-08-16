import unittest
from space.core.space_hierarchy import SpaceHierarchy

class SpaceHierarchyTests(unittest.TestCase):
    def setUp(self):
        self.h = SpaceHierarchy()
        self.h.register_root("space-root", "model-root", "foundation organism")
        self.h.register_child("space-a", "model-a", "space-root", "vision specialist", reason="specialize perception")
        self.h.register_child("space-b", "model-b", "space-root", "market specialist", reason="specialize market work")
        self.h.register_child("space-a1", "model-a1", "space-a", "vision submodel", reason="decompose vision")

    def test_lineage(self):
        self.assertEqual(self.h.get("space-a").parent_space_id, "space-root")
        self.assertEqual([m.space_id for m in self.h.ancestors("space-a1")], ["space-a", "space-root"])
        self.assertEqual([m.space_id for m in self.h.descendants("space-root")], ["space-a", "space-b", "space-a1"])

    def test_relationships(self):
        self.assertEqual(self.h.relationship("space-a", "space-root")["relation"], "CHILD_OF")
        self.assertEqual(self.h.relationship("space-root", "space-a")["relation"], "PARENT_OF")
        self.assertEqual(self.h.relationship("space-a", "space-b")["relation"], "SIBLING_OR_PEER")
        self.assertEqual(self.h.relationship("space-a1", "space-root")["relation"], "DESCENDANT_OF")

    def test_duplicate_root_and_unknown_parent_are_rejected(self):
        with self.assertRaises(ValueError):
            self.h.register_root("another", "model", "bad")
        with self.assertRaises(KeyError):
            self.h.register_child("space-x", "model-x", "missing", "bad")

if __name__ == "__main__":
    unittest.main()
