"""Deterministic local runner used by CI to exercise autonomous-organ tests."""
import unittest


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromName("space.organs.test_autonomous_organ")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
