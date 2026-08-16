import unittest

from space.core.space_hierarchy import SpaceHierarchy
from space.core.space_relationship import SpaceRelationship
from space.core.trust import TrustLedger

class SpaceRelationshipTests(unittest.TestCase):
    def setUp(self):
        self.h = SpaceHierarchy()
        self.h.register_root("root", "model-root", "foundation")
        self.h.register_child("child", "model-child", "root", "specialized", reason="specialization")
        self.t = TrustLedger()
        self.t.set_initial("child", 0.2, "initial trust")
        self.r = SpaceRelationship(self.h, self.t)

    def test_initial_trust_is_recorded(self):
        self.assertEqual(self.t.score("child"), 0.2)
        events = self.t.history("child")
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["previous"], 0.0)
        self.assertEqual(events[0]["current"], 0.2)

    def test_lineage_does_not_create_trust(self):
        ctx = self.r.context("root", "child", "observe", "request metadata")
        self.assertEqual(ctx.relation, "PARENT_OF")
        self.assertEqual(ctx.trust_score, 0.2)
        self.assertFalse(self.r.can_request(ctx))

    def test_trust_change_is_reflected(self):
        self.t.update("child", 0.7, "verified interaction")
        ctx = self.r.context("root", "child", "observe", "request metadata", ("verified-interaction",))
        self.assertTrue(self.r.can_request(ctx))
        explanation = self.r.explain(ctx)
        self.assertTrue(explanation["trust_sufficient"])

if __name__ == "__main__":
    unittest.main()
