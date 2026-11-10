"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core, reports


class TestCore(unittest.TestCase):
    def test_check_answer_is_case_insensitive(self):
        card = {"id": 1, "question": "Capital of France?", "answer": "Paris", "category": "geo"}
        self.assertTrue(core.check_answer(card, "paris"))
        self.assertFalse(core.check_answer(card, "London"))

    def test_add_card_gives_a_new_id(self):
        data = {"cards": [{"id": 1, "question": "q", "answer": "a", "category": "general"}]}
        card = core.add_card(data, "New question?", "yes")
        self.assertEqual(card["id"], 2)
        self.assertEqual(len(data["cards"]), 2)

    def test_review_missed(self):
        cards = ["Card A", "Card B", "Card C"]

        #Test mixed case: some incorrect, some correct
        mixed_results = [True, False, True]

        self.assertEqual(
            core.review_missed(cards, mixed_results),
            ["Card B"],
            "Review missed cards with mixed results test failed"
        )

        #Test nothing missed case: all correct
        all_correct_results = [True, True, True]

        self.assertEqual(
            core.review_missed(cards, all_correct_results),
            [],
            "Review missed cards with all correct results test failed"
        )

    def test_category_reports(self):
        #Sample card bank with different categories
        sample_mixed = {
            "cards" : [
                {"category": "syntax"},
                {"category": "lists"},
                {"category": "lists"},
                {"category": "syntax"},
                {"category": "types"},
                {"category": "syntax"}
            ]
        }

        self.assertEqual(
            reports.category_report(sample_mixed), {'syntax': 3, 'lists': 2, 'types': 1}
        )

        #Sample card bank with no categories
        sample_none = {
            "cards" : [
                {"question" : "Q1"},
                {"question" : "Q2"}
            ]
        }

        self.assertEqual(
            reports.category_report(sample_none), {}
        )




if __name__ == "__main__":
    unittest.main()
