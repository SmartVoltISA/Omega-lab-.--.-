import math
import unittest

from space.organs.audio_acoustic_features import analyze, estimate_f0


class AudioAcousticFeatureTests(unittest.TestCase):
    def test_empty_signal(self):
        result = analyze([], 16000)
        self.assertEqual(result.duration_s, 0.0)
        self.assertIsNone(result.f0_hz)
        self.assertFalse(result.voiced)

    def test_sine_f0_is_deterministic(self):
        sr = 16000
        hz = 200.0
        samples = [0.8 * math.sin(2 * math.pi * hz * i / sr) for i in range(sr)]
        first = estimate_f0(samples, sr)
        second = estimate_f0(samples, sr)
        self.assertIsNotNone(first)
        self.assertEqual(first, second)
        self.assertAlmostEqual(first, hz, delta=2.0)

    def test_constant_signal_is_unvoiced(self):
        result = analyze([0.25] * 1000, 16000)
        self.assertIsNone(result.f0_hz)
        self.assertFalse(result.voiced)

    def test_basic_measurements(self):
        result = analyze([-1.0, 0.0, 1.0, 0.0], 8000)
        self.assertAlmostEqual(result.duration_s, 4 / 8000)
        self.assertAlmostEqual(result.peak, 1.0)
        self.assertGreater(result.rms, 0.0)
        self.assertGreater(result.zero_crossing_rate, 0.0)


if __name__ == "__main__":
    unittest.main()
