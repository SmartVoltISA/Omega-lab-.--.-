"""Executable Ω-PLAN-1 boundary tests."""

import unittest

from plan import build_plan


class PlanTests(unittest.TestCase):
    def test_builds_a_structured_plan(self):
        plan = build_plan(
            source_future_id="future-001",
            source_state_id="state-001",
            desired_state="verification complete",
            next_result="verification result available",
            steps=[
                {
                    "action": "run verification",
                    "expected_result": "verification report produced",
                    "required_data": ["test data"],
                },
                {
                    "action": "compare expected and actual",
                    "expected_result": "status classified",
                },
            ],
        )
        self.assertEqual(plan.status, "PROPOSED")
        self.assertEqual(len(plan.steps), 2)
        self.assertEqual(plan.steps[0].expected_result, "verification report produced")

    def test_rejects_action_without_expected_result(self):
        with self.assertRaises(ValueError):
            build_plan(
                source_future_id="future-001",
                source_state_id="state-001",
                desired_state="done",
                next_result="result",
                steps=[{"action": "do something"}],
            )

    def test_plan_does_not_execute(self):
        plan = build_plan(
            source_future_id="future-001",
            source_state_id="state-001",
            desired_state="done",
            next_result="result",
            steps=[{"action": "inspect", "expected_result": "report"}],
        )
        self.assertEqual(plan.status, "PROPOSED")


if __name__ == "__main__":
    unittest.main()
