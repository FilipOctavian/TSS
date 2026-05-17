import unittest

from main import LoanEvaluator


class LoanEvaluatorAdditionalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evaluator = LoanEvaluator()

    def test_amount_boundary_exactly_5000_is_still_small(self) -> None:
        self.assertEqual("small", self.evaluator.validate_loan_amount(5_000))

    def test_application_is_rejected_without_cosigner_on_medium_income(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=620,
            monthly_income=3_500,
            existing_debt=1_000,
            has_cosigner=False,
        )
        self.assertEqual("rejected", result)


if __name__ == "__main__":
    unittest.main()
