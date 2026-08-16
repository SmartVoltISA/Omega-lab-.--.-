import unittest
from space.core.decision_support import DecisionSupport, Option

class DecisionSupportTests(unittest.TestCase):
    def test_builds_options_without_deciding(self):
        support = DecisionSupport()
        brief = support.build(
            "b1", "Which path?",
            [
                Option("left", "go left", "outcome A", 0.2, ("risk A",)),
                Option("right", "go right", "outcome B", 0.3, ("risk B",)),
            ],
            evidence=["observation-1"],
            recommendation="right",
        )
        self.assertEqual(brief.recommendation, "right")
        self.assertTrue(brief.understanding_required)
        self.assertEqual(support.explain(brief)["decision_owner"], "HUMAN")

    def test_human_decision_is_explicit(self):
        support = DecisionSupport()
        brief = support.build("b2", "Choose", [Option("a", "A", "x"), Option("b", "B", "y")])
        decision = support.record_human_decision(brief, "b")
        self.assertEqual(decision["decision_owner"], "HUMAN")
        self.assertEqual(decision["option_id"], "b")

    def test_unknown_option_rejected(self):
        support = DecisionSupport()
        brief = support.build("b3", "Choose", [Option("a", "A", "x")])
        with self.assertRaises(ValueError):
            support.record_human_decision(brief, "unknown")

if __name__ == "__main__":
    unittest.main()
