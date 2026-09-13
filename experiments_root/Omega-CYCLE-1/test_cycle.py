"""Ω-CYCLE-1: minimal end-to-end proof of the operational loop."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Omega-PLAN-1"))
sys.path.insert(0, str(ROOT / "Omega-EXECUTION-1"))
sys.path.insert(0, str(ROOT / "Omega-VERIFICATION-1"))
sys.path.insert(0, str(ROOT / "Omega-FEEDBACK-1"))

from plan import build_plan  # noqa: E402
from execution import BoundedExecutor, Guardian  # noqa: E402
from verification import verify  # noqa: E402
from feedback import derive_feedback  # noqa: E402


class CycleTests(unittest.TestCase):
    def test_plan_to_feedback(self):
        plan = build_plan(
            source_future_id="future-1",
            source_state_id="state-0",
            desired_state="test completed",
            next_result="test result available",
            steps=[{"action": "controlled-test", "expected_result": "PASS"}],
        )

        guardian = Guardian()
        executor = BoundedExecutor()
        executor.register("controlled-test", lambda: "PASS")
        step = plan.steps[0]
        auth = guardian.authorize(plan.plan_id, step.step_id, authorized_by="cycle-test", reason="proof")
        execution = executor.execute(plan, step, auth)

        verification = verify(
            execution_id=execution.execution_id,
            expected=step.expected_result,
            actual=execution.actual_result,
        )
        feedback = derive_feedback(verification)

        self.assertEqual(execution.status, "SUCCESS")
        self.assertEqual(verification.status, "CONFIRMED")
        self.assertEqual(feedback.state_changes["last_verification"], "CONFIRMED")
        self.assertTrue(feedback.next_cycle_required)


if __name__ == "__main__":
    unittest.main()
