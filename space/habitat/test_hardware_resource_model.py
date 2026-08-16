import unittest

from space.habitat.hardware_resource_model import Resource, ResourceClaim, ResourceManager


class HardwareResourceTests(unittest.TestCase):
    def test_capacity_and_release(self):
        manager = ResourceManager()
        manager.register(Resource("ram", "RAM", 16, "GB"))
        self.assertTrue(manager.claim(ResourceClaim("c1", "space", "ram", 12, "GB")))
        self.assertFalse(manager.claim(ResourceClaim("c2", "space", "ram", 8, "GB")))
        self.assertTrue(manager.release("c1"))
        self.assertTrue(manager.claim(ResourceClaim("c2", "space", "ram", 8, "GB")))

    def test_unknown_resource_is_rejected(self):
        manager = ResourceManager()
        self.assertFalse(manager.claim(ResourceClaim("c1", "space", "gpu", 1)))


if __name__ == "__main__":
    unittest.main()
