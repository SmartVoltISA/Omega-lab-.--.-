import tempfile
import unittest
from pathlib import Path

from security_scan_lab import SecurityScanLab


class SecurityScanLabTests(unittest.TestCase):
    def test_quarantine_and_hash_without_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "sample.bin"
            source.write_bytes(b"safe test payload")
            lab = SecurityScanLab(root / "quarantine")
            staged = lab.quarantine(source)
            result = lab.inspect(staged)
            self.assertTrue(staged.exists())
            self.assertEqual(result.verdict, "UNSCANNED")
            self.assertEqual(result.engine, "metadata-only")
            self.assertEqual(len(result.sha256), 64)

    def test_never_promotes_or_executes_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "payload.txt"
            source.write_text("data", encoding="utf-8")
            lab = SecurityScanLab(root / "quarantine")
            staged = lab.quarantine(source)
            self.assertEqual(lab.inspect(staged).verdict, "UNSCANNED")
            self.assertFalse(hasattr(lab, "promote"))
            self.assertFalse(hasattr(lab, "execute"))


if __name__ == "__main__":
    unittest.main()
