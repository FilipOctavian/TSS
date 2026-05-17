import unittest

from main import LoanEvaluator


class LoanEvaluatorCoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evaluator = LoanEvaluator()

    def test_equivalence_partition_invalid_amount_too_small(self) -> None:
        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(500)

    def test_equivalence_partition_valid_small_amount(self) -> None:
        self.assertEqual("small", self.evaluator.validate_loan_amount(3_000))

    def test_equivalence_partition_valid_medium_amount(self) -> None:
        self.assertEqual("medium", self.evaluator.validate_loan_amount(12_000))

    def test_equivalence_partition_valid_large_amount(self) -> None:
        self.assertEqual("large", self.evaluator.validate_loan_amount(35_000))

    def test_equivalence_partition_invalid_amount_too_large(self) -> None:
        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(70_000)

    def test_boundary_values_for_minimum_amount(self) -> None:
        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(999)

        self.assertEqual("small", self.evaluator.validate_loan_amount(1_000))
        self.assertEqual("small", self.evaluator.validate_loan_amount(1_001))

    def test_boundary_values_for_maximum_amount(self) -> None:
        self.assertEqual("large", self.evaluator.validate_loan_amount(49_999))
        self.assertEqual("large", self.evaluator.validate_loan_amount(50_000))

        with self.assertRaises(ValueError):
            self.evaluator.validate_loan_amount(50_001)

    def test_statement_coverage_for_interest_rate(self) -> None:
        result = self.evaluator.calculate_interest_rate(
            amount=25_000,
            months=12,
            has_salary_account=True,
        )
        self.assertEqual(0.085, result)

    def test_decision_coverage_reaches_long_term_branch(self) -> None:
        result = self.evaluator.calculate_interest_rate(
            amount=15_000,
            months=48,
            has_salary_account=False,
        )
        self.assertEqual(0.135, result)

    def test_condition_coverage_for_approved_with_high_income(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=720,
            monthly_income=6_000,
            existing_debt=2_000,
            has_cosigner=False,
        )
        self.assertEqual("approved", result)

    def test_basis_path_low_credit_score_leads_to_rejection(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=540,
            monthly_income=9_000,
            existing_debt=500,
            has_cosigner=True,
        )
        self.assertEqual("rejected", result)

    def test_condition_boundary_credit_score_550_is_not_auto_rejected(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=550,
            monthly_income=5_500,
            existing_debt=1_000,
            has_cosigner=False,
        )
        self.assertEqual("manual_review", result)

    def test_basis_path_high_income_but_low_score_without_cosigner(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=650,
            monthly_income=5_500,
            existing_debt=1_000,
            has_cosigner=False,
        )
        self.assertEqual("manual_review", result)

    def test_basis_path_medium_income_with_cosigner(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=610,
            monthly_income=3_500,
            existing_debt=1_200,
            has_cosigner=True,
        )
        self.assertEqual("manual_review", result)

    def test_basis_path_rejected_when_debt_ratio_too_high(self) -> None:
        result = self.evaluator.evaluate_application(
            credit_score=680,
            monthly_income=4_000,
            existing_debt=2_500,
            has_cosigner=True,
        )
        self.assertEqual("rejected", result)


if __name__ == "__main__":
    unittest.main()
