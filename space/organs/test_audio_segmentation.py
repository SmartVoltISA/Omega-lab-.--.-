import math
import unittest

from space.organs.audio_segmentation import AudioSegmenter


class AudioSegmentationTests(unittest.TestCase):
    def test_empty_signal(self):
        self.assertEqual(AudioSegmenter().segment([]), [])

    def test_silence_is_unvoiced(self):
        samples = [0.0] * 1600
        segments = AudioSegmenter().segment(samples)
        self.assertTrue(segments)
        self.assertFalse(any(s.voiced for s in segments))

    def test_tone_is_voiced(self):
        sr = 16000
        samples = [0.4 * math.sin(2 * math.pi * 200 * i / sr) for i in range(sr // 5)]
        segments = AudioSegmenter().segment(samples)
        self.assertTrue(any(s.voiced for s in segments))

    def test_energy_is_recorded(self):
        samples = [0.2] * 1600
        segments = AudioSegmenter().segment(samples)
        self.assertGreater(segments[0].mean_energy, 0.0)


if __name__ == "__main__":
    unittest.main()
