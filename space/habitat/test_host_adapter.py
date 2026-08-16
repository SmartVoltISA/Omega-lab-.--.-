import unittest
from space.habitat.host_adapter import HostAdapter

class HostAdapterTests(unittest.TestCase):
    def test_snapshot_is_read_only_and_structured(self):
        snapshot = HostAdapter().snapshot()
        for key in ("os", "kernel", "architecture", "cpu_count", "ram_bytes", "storage_free_bytes", "gpus", "network_interfaces", "bluetooth", "usb", "cameras", "audio_devices", "displays"):
            self.assertIn(key, snapshot)
        self.assertIsInstance(snapshot["network_interfaces"], tuple)
        self.assertIsInstance(snapshot["gpus"], tuple)

if __name__ == "__main__":
    unittest.main()
