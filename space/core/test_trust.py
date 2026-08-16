import unittest
from space.core.space_hierarchy import SpaceHierarchy
from space.core.trust import TrustLedger

class TrustTests(unittest.TestCase):
    def test_lineage_does_not_grant_trust(self):
        hierarchy = SpaceHierarchy()
        hierarchy.register_root("root", "model-root", "foundation")
        hierarchy.register_child("child", "model-child", "root", "specialized")
        trust = TrustLedger()
        self.assertEqual(hierarchy.relationship("root", "child")["relation"], "PARENT_OF")
        self.assertEqual(trust.score("child"), 0.0)

    def test_trust_history_is_append_only(self):
        trust = TrustLedger()
        trust.update("space-b", 0.4, "initial evidence")
        trust.update("space-b", 0.8, "successful interaction")
        trust.update("space-b", 0.2, "violation")
        history = trust.history("space-b")
        self.assertEqual([e["current"] for e in history], [0.4, 0.8, 0.2])
        self.assertEqual(trust.score("space-b"), 0.2)

if __name__ == "__main__":
    unittest.main()
