import math
import unittest

from space.organs.audio_organ import AudioOrgan


class AudioOrganTests(unittest.TestCase):
    def test_empty_signal_is_safe(self):
        f = AudioOrgan().analyze([])
        self.assertEqual(f.duration_s, 0.0)
        self.assertFalse(f.voiced)
        self.assertIsNone(f.f0_hz)

    def test_constant_signal_has_no_false_pitch(self):
        f = AudioOrgan().analyze([0.25] * 1000)
        self.assertFalse(f.voiced)
        self.assertIsNone(f.f0_hz)

    def test_detects_deterministic_tone_near_200hz(self):
        sr = 16000
        samples = [math.sin(2 * math.pi * 200 * i / sr) for i in range(4000)]
        f = AudioOrgan(sr).analyze(samples)
        self.assertTrue(f.voiced)
        self.assertIsNotNone(f.f0_hz)
        self.assertLess(abs(f.f0_hz - 200), 5)

    def test_features_are_inspectable(self):
        f = AudioOrgan(8000).analyze([(-1.0) ** i * 0.5 for i in range(800)])
        self.assertAlmostEqual(f.duration_s, 0.1)
        self.assertAlmostEqual(f.peak, 0.5)
        self.assertGreater(f.zero_crossing_rate, 0.9)


if __name__ == "__main__":
    unittest.main()
