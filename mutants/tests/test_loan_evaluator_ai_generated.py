import unittest
from main import LoanEvaluator


class TestLoanEvaluatorAI(unittest.TestCase):
    """
    Teste generate automat de Claude (claude.ai) pe baza clasei LoanEvaluator.
    Utilizate pentru comparatie cu suita proprie in raportul AI.
    Data generarii: 29 aprilie 2026
    """

    def setUp(self):
        self.evaluator = LoanEvaluator()

    # --- validate_loan_amount ---

    def test_amount_below_minimum_raises(self):
        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(500)

    def test_amount_above_maximum_raises(self):
        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(100000)

    def test_amount_small(self):
        self.assertEqual("small", self.evaluator.validate_loan_amount(1000))

    def test_amount_medium(self):
        self.assertEqual("medium", self.evaluator.validate_loan_amount(10000))

    def test_amount_large(self):
        self.assertEqual("large", self.evaluator.validate_loan_amount(30000))

    # --- calculate_interest_rate ---

    def test_interest_rate_basic(self):
        rate = self.evaluator.calculate_interest_rate(10000, 24, False)
        self.assertEqual(0.12, rate)

    def test_interest_rate_large_amount_discount(self):
        rate = self.evaluator.calculate_interest_rate(25000, 24, False)
        self.assertEqual(0.11, rate)

    def test_interest_rate_short_term_discount(self):
        rate = self.evaluator.calculate_interest_rate(10000, 12, False)
        self.assertEqual(0.10, rate)

    def test_interest_rate_long_term_penalty(self):
        rate = self.evaluator.calculate_interest_rate(10000, 48, False)
        self.assertEqual(0.135, rate)

    def test_interest_rate_salary_account_discount(self):
        rate = self.evaluator.calculate_interest_rate(10000, 24, True)
        self.assertEqual(0.115, rate)

    def test_interest_rate_invalid_months_raises(self):
        with self.assertRaises(ValueError):
            self.evaluator.calculate_interest_rate(10000, 3, False)

    # --- evaluate_application ---

    def test_application_approved(self):
        result = self.evaluator.evaluate_application(750, 6000, 1000, False)
        self.assertEqual("approved", result)

    def test_application_rejected_low_score(self):
        result = self.evaluator.evaluate_application(400, 8000, 500, False)
        self.assertEqual("rejected", result)

    def test_application_manual_review(self):
        result = self.evaluator.evaluate_application(600, 5500, 1500, False)
        self.assertEqual("manual_review", result)

    def test_application_negative_values_raises(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_application(-1, 5000, 1000, False)

    def test_application_with_cosigner(self):
        result = self.evaluator.evaluate_application(600, 3500, 1000, True)
        self.assertEqual("manual_review", result)


if __name__ == "__main__":
    unittest.main()
