import unittest

from space.organs.language_organ import LanguageOrgan, SemanticRelation


class LanguageOrganTests(unittest.TestCase):
    def setUp(self):
        self.organ = LanguageOrgan()

    def test_understand_to_semantic_relation(self):
        result = self.organ.understand("память связана с графом")
        self.assertEqual(result, [SemanticRelation("память", "связь", "графом")])

    def test_round_trip_semantic_render(self):
        relations = self.organ.understand("орган хранит память")
        self.organ.remember(relations, "working")
        rendered = self.organ.render(relations)
        self.assertIn("орган — хранит → память", rendered)

    def test_three_memory_tiers_are_separate(self):
        relation = SemanticRelation("орган", "имеет", "состояние")
        self.organ.remember([relation], "fast")
        self.assertEqual(len(self.organ.memory.fast), 1)
        self.assertEqual(len(self.organ.memory.working), 0)
        self.assertEqual(len(self.organ.memory.long_term), 0)
        self.organ.promote(relation, "fast", "working")
        self.assertEqual(len(self.organ.memory.fast), 0)
        self.assertEqual(len(self.organ.memory.working), 1)

    def test_local_memory_answer_does_not_require_graph(self):
        relation = SemanticRelation("память", "связь", "граф")
        self.organ.remember([relation], "long_term")
        self.assertIn("память — связь → граф", self.organ.answer_from_local_memory("память"))

    def test_provenance_is_preserved(self):
        relation = self.organ.understand("орган хранит память", provenance="dialogue:1")[0]
        self.assertEqual(relation.provenance, "dialogue:1")
        self.organ.remember([relation], "working")
        self.assertEqual(self.organ.memory.working[0].provenance, "dialogue:1")

    def test_confidence_is_bounded(self):
        relation = SemanticRelation("орган", "имеет", "состояние", confidence=0.75)
        self.assertEqual(relation.confidence, 0.75)
        with self.assertRaises(ValueError):
            SemanticRelation("орган", "имеет", "состояние", confidence=1.1)

    def test_unknown_language_is_rejected(self):
        with self.assertRaises(ValueError):
            self.organ.understand("это предложение вне контракта")

    def test_memory_tier_is_explicit(self):
        with self.assertRaises(ValueError):
            self.organ.remember([], "global")


if __name__ == "__main__":
    unittest.main()
