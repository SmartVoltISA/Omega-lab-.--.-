"""Executable Ω-FEEDBACK-1 tests."""

import unittest

from feedback import derive_feedback
from verification import verify


class FeedbackTests(unittest.TestCase):
    def test_confirmed_result_updates_state_direction(self):
        verification = verify(execution_id="exec-1", expected="ok", actual="ok")
        feedback = derive_feedback(verification)
        self.assertEqual(feedback.state_changes["last_verification"], "CONFIRMED")
        self.assertTrue(feedback.next_cycle_required)

    def test_failed_result_is_not_erased(self):
        verification = verify(execution_id="exec-1", expected="ok", actual="bad")
        feedback = derive_feedback(verification)
        self.assertEqual(feedback.state_changes["last_verification"], "FAILED")
        self.assertTrue(feedback.next_cycle_required)


if __name__ == "__main__":
    unittest.main()
