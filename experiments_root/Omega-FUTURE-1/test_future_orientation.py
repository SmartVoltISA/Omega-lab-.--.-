import unittest

from future_orientation import CandidateAction, orient


class FutureOrientationTests(unittest.TestCase):
    def test_orientation_separates_direction_from_execution(self):
        action = CandidateAction(
            action_id="a1",
            description="collect missing evidence",
            expected_result="evidence available",
            required_data=("evidence",),
        )
        result = orient(
            current={"status": "incomplete"},
            memory={"last_result": "partial"},
            goal="finish verification",
            available_data=("state",),
            constraints=("no_execution",),
            desired_state="verification-ready",
            next_result="evidence inventory",
            data_needed=("evidence", "state"),
            candidate_actions=(action,),
            horizon="NEXT",
        )
        self.assertEqual(result.horizon, "NEXT")
        self.assertEqual(result.data_gap, ("evidence",))
        self.assertEqual(result.candidate_actions[0].expected_result, "evidence available")
        self.assertFalse(hasattr(result, "actual_result"))

    def test_next_is_smaller_than_future_claim(self):
        result = orient(
            current={"status": "started"}, memory={}, goal="progress",
            desired_state="working", next_result="first verified step",
        )
        self.assertEqual(result.horizon, "NEXT")
        self.assertEqual(result.next_result, "first verified step")

    def test_invalid_horizon_is_rejected(self):
        with self.assertRaises(ValueError):
            orient(current={}, memory={}, goal="x", desired_state="y", next_result="z", horizon="NOW")


if __name__ == "__main__":
    unittest.main()
