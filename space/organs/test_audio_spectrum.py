import math
import unittest

from space.organs.audio_spectrum import spectrum_features


class AudioSpectrumTests(unittest.TestCase):
    def test_empty_and_silent(self):
        self.assertEqual(spectrum_features([], 16000).dominant_hz, None)
        self.assertEqual(spectrum_features([0.0] * 64, 16000).spectral_centroid_hz, None)

    def test_single_tone_has_dominant_frequency(self):
        sr = 16000
        n = 1024
        samples = [math.sin(2 * math.pi * 500 * i / sr) for i in range(n)]
        result = spectrum_features(samples, sr)
        self.assertIsNotNone(result.dominant_hz)
        self.assertAlmostEqual(result.dominant_hz, 500.0, delta=20.0)

    def test_features_are_candidates(self):
        result = spectrum_features([1.0, -1.0] * 32, 16000)
        self.assertIsNotNone(result.spectral_centroid_hz)
        self.assertTrue(result.f1_hz is None or result.f1_hz >= 0)


if __name__ == "__main__":
    unittest.main()
