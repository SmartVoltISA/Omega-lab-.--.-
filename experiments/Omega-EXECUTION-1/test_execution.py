"""Executable Ω-EXECUTION-1 boundary tests."""

import unittest
from dataclasses import replace

from execution import BoundedExecutor, Guardian


class ExecutionTests(unittest.TestCase):
    def test_authorized_registered_action_produces_result(self):
        guardian = Guardian()
        executor = BoundedExecutor()
        observed = []
        executor.register("collect-test-data", lambda: observed.append("ran") or "data-ready")

        plan = type("Plan", (), {"plan_id": "plan-1"})()
        step = type("Step", (), {"step_id": "step-1", "action": "collect-test-data"})()
        auth = guardian.authorize(plan.plan_id, step.step_id, authorized_by="test", reason="controlled test")
        result = executor.execute(plan, step, auth)

        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.actual_result, "data-ready")
        self.assertEqual(observed, ["ran"])
        self.assertEqual(result.authorization_id, auth.authorization_id)

    def test_unauthorized_execution_is_blocked(self):
        executor = BoundedExecutor()
        executor.register("safe-test", lambda: "must-not-run")
        plan = type("Plan", (), {"plan_id": "plan-1"})()
        step = type("Step", (), {"step_id": "step-1", "action": "safe-test"})()
        auth = Guardian().authorize(plan.plan_id, step.step_id, authorized_by="test", reason="test")
        denied = replace(auth, granted=False)
        with self.assertRaises(PermissionError):
            executor.execute(plan, step, denied)

    def test_unregistered_action_is_blocked(self):
        executor = BoundedExecutor()
        plan = type("Plan", (), {"plan_id": "plan-1"})()
        step = type("Step", (), {"step_id": "step-1", "action": "unknown"})()
        auth = Guardian().authorize(plan.plan_id, step.step_id, authorized_by="test", reason="test")
        with self.assertRaises(PermissionError):
            executor.execute(plan, step, auth)

    def test_failed_operation_becomes_explicit_result(self):
        executor = BoundedExecutor()
        executor.register("failing-test", lambda: 1 / 0)
        plan = type("Plan", (), {"plan_id": "plan-1"})()
        step = type("Step", (), {"step_id": "step-1", "action": "failing-test"})()
        auth = Guardian().authorize(plan.plan_id, step.step_id, authorized_by="test", reason="failure test")
        result = executor.execute(plan, step, auth)
        self.assertEqual(result.status, "FAILED")
        self.assertEqual(result.actual_result["error_type"], "ZeroDivisionError")


if __name__ == "__main__":
    unittest.main()
