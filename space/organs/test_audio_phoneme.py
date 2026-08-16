import unittest

from space.organs.audio_phoneme import vowel_candidates


class AudioPhonemeTests(unittest.TestCase):
    def test_candidates_are_ranked_and_explicit(self):
        result = vowel_candidates(700.0, 1100.0)
        self.assertGreaterEqual(len(result), 3)
        self.assertEqual(result[0].symbol, "a")
        self.assertTrue(all(0.0 < item.score <= 1.0 for item in result))
        self.assertTrue(all(item.reason == "F1/F2 proximity" for item in result))

    def test_invalid_measurement_is_ambiguous(self):
        self.assertEqual(vowel_candidates(0.0, 1100.0), ())
        self.assertEqual(vowel_candidates(700.0, 0.0), ())

    def test_candidates_do_not_claim_certainty(self):
        result = vowel_candidates(700.0, 1100.0)
        self.assertGreater(len(result), 1)
        self.assertLess(result[0].score, 1.0)


if __name__ == "__main__":
    unittest.main()
