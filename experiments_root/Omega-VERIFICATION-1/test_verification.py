"""Executable Ω-VERIFICATION-1 tests."""

import unittest

from verification import verify


class VerificationTests(unittest.TestCase):
    def test_confirmed(self):
        result = verify(execution_id="exec-1", expected="ok", actual="ok")
        self.assertEqual(result.status, "CONFIRMED")

    def test_failed(self):
        result = verify(execution_id="exec-1", expected="ok", actual="bad")
        self.assertEqual(result.status, "FAILED")

    def test_unknown(self):
        result = verify(execution_id="exec-1", expected="ok", actual=None)
        self.assertEqual(result.status, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
