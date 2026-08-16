import unittest
from pathlib import Path

from foundation_guard import FOUNDATION_GIT_BLOB_SHA, FOUNDATION_PATH, foundation_integrity_ok, protected_foundation_identity


class FoundationGuardTests(unittest.TestCase):
    def test_active_foundation_is_pinned_and_intact(self):
        self.assertTrue((Path.cwd() / FOUNDATION_PATH).is_file())
        self.assertTrue(foundation_integrity_ok())

    def test_identity_is_explicit_and_immutable(self):
        identity = protected_foundation_identity()
        self.assertEqual(identity["path"], str(FOUNDATION_PATH))
        self.assertEqual(identity["git_blob_sha"], FOUNDATION_GIT_BLOB_SHA)
        self.assertEqual(FOUNDATION_GIT_BLOB_SHA, "6d5649a0ebe86226dd8c35d4009cff3bbc27dd44")


if __name__ == "__main__":
    unittest.main()
