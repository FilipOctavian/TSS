import unittest

from main import LoanEvaluator


class LoanEvaluatorMutmutTests(unittest.TestCase):
    """
    Teste suplimentare generate dupa analiza raportului mutmut.
    Fiecare test este etichetat cu ID-urile mutantilor pe care ii ucide.

    Mutanti echivalenti (nu pot fi ucisi - nu schimba comportamentul observabil):
      M12, M23, M52  - modifica textul mesajelor de eroare (ValueError e oricum ridicata)
      M44            - round(rate, 4) vs round(rate, 3): toate ratele posibile
                       au cel mult 3 zecimale exacte, deci rezultatul este identic
    """

    def setUp(self) -> None:
        self.evaluator = LoanEvaluator()

    # ------------------------------------------------------------------ #
    #  validate_loan_amount -- frontiere interne (5000, 20000)            #
    # ------------------------------------------------------------------ #

    def test_boundary_5001_is_medium_not_small(self) -> None:
        # Ucide: M14  (amount <= 5001 ar clasifica 5001 drept "small")
        self.assertEqual("medium", self.evaluator.validate_loan_amount(5_001))

    def test_boundary_20000_is_medium_not_large(self) -> None:
        # Ucide: M16  (amount < 20_000 ar clasifica 20000 drept "large")
        self.assertEqual("medium", self.evaluator.validate_loan_amount(20_000))

    def test_boundary_20001_is_large_not_medium(self) -> None:
        # Ucide: M17  (amount <= 20001 ar clasifica 20001 drept "medium")
        self.assertEqual("large", self.evaluator.validate_loan_amount(20_001))

    # ------------------------------------------------------------------ #
    #  calculate_interest_rate -- frontierele MIN_MONTHS / MAX_MONTHS     #
    # ------------------------------------------------------------------ #

    def test_min_months_boundary_6_is_valid(self) -> None:
        # Ucide: M5  (MIN_MONTHS=7 ar respinge 6 luni)
        #        M20 (months <= MIN_MONTHS ar respinge exact 6 luni)
        # months=6 <= 12  =>  rata = 0.12 - 0.02 = 0.10
        result = self.evaluator.calculate_interest_rate(
            amount=15_000, months=6, has_salary_account=False
        )
        self.assertEqual(0.10, result)

    def test_max_months_boundary_60_is_valid(self) -> None:
        # Ucide: M7  (MAX_MONTHS=61 ar accepta 61 luni ca valida)
        #        M21 (months >= MAX_MONTHS ar respinge exact 60 luni)
        # months=60 >= 36  =>  rata = 0.12 + 0.015 = 0.135
        result = self.evaluator.calculate_interest_rate(
            amount=15_000, months=60, has_salary_account=False
        )
        self.assertEqual(0.135, result)

    def test_months_5_raises_value_error(self) -> None:
        # Ucide: M22  (or -> and: cu AND conditia nu devine niciodata adevarata
        #              daca un singur capat este depasit, deci exceptia nu s-ar
        #              mai ridica pentru months=5)
        with self.assertRaises(ValueError):
            self.evaluator.calculate_interest_rate(
                amount=15_000, months=5, has_salary_account=False
            )

    def test_amount_exactly_20000_gets_large_loan_discount(self) -> None:
        # Ucide: M26  (amount >= 20_000 -> amount > 20_000)
        #        M27  (amount >= 20_000 -> amount >= 20001)
        # amount=20000 >= 20000 => rate -= 0.01
        # months=24: fara bonus de termen  =>  rata = 0.12 - 0.01 = 0.11
        result = self.evaluator.calculate_interest_rate(
            amount=20_000, months=24, has_salary_account=False
        )
        self.assertEqual(0.11, result)

    def test_months_13_does_not_get_short_term_discount(self) -> None:
        # Ucide: M32  (months <= 12 -> months <= 13: ar acorda reducerea si pentru 13 luni)
        # months=13: nu e <= 12, nu e >= 36  =>  rata = 0.12 (doar baza)
        result = self.evaluator.calculate_interest_rate(
            amount=15_000, months=13, has_salary_account=False
        )
        self.assertEqual(0.12, result)

    def test_months_exactly_36_gets_long_term_penalty(self) -> None:
        # Ucide: M36  (months >= 36 -> months > 36)
        #        M37  (months >= 36 -> months >= 37)
        # months=36 >= 36  =>  rata = 0.12 + 0.015 = 0.135
        result = self.evaluator.calculate_interest_rate(
            amount=15_000, months=36, has_salary_account=False
        )
        self.assertEqual(0.135, result)

    # ------------------------------------------------------------------ #
    #  evaluate_application -- validare valori negative                   #
    # ------------------------------------------------------------------ #

    def test_credit_score_zero_is_valid_and_rejected(self) -> None:
        # Ucide: M45  (credit_score < 0 -> credit_score <= 0:
        #              cu M45, score=0 ar ridica ValueError)
        #        M46  (credit_score < 0 -> credit_score < 1: idem)
        # In codul original, 0 nu este negativ, deci nu ridica exceptie.
        # score=0 < 550 => "rejected"
        result = self.evaluator.evaluate_application(
            credit_score=0, monthly_income=5_000,
            existing_debt=1_000, has_cosigner=False,
        )
        self.assertEqual("rejected", result)

    def test_negative_credit_score_alone_raises_value_error(self) -> None:
        # Ucide: M51  (or -> and: cu AND, credit_score=-1 AND monthly_income=5000
        #              ambele negative -> False -> nu s-ar mai ridica exceptia)
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_application(
                credit_score=-1, monthly_income=5_000,
                existing_debt=0, has_cosigner=False,
            )

    def test_monthly_income_zero_does_not_raise_and_returns_rejected(self) -> None:
        # Ucide: M47  (monthly_income < 0 -> monthly_income <= 0: ar ridica exceptie)
        #        M48  (monthly_income < 0 -> monthly_income < 1: idem)
        #        M53  (float("inf") -> float("XXinfXX"): ar pica cu ValueError)
        #        M55  (monthly_income == 0 -> monthly_income == 1:
        #              ar face impartire la zero pentru income=0)
        # income=0 => debt_ratio=inf, score=600>=550, income<5000, income<3000 => "rejected"
        result = self.evaluator.evaluate_application(
            credit_score=600, monthly_income=0,
            existing_debt=500, has_cosigner=False,
        )
        self.assertEqual("rejected", result)

    def test_existing_debt_zero_does_not_raise(self) -> None:
        # Ucide: M49  (existing_debt < 0 -> existing_debt <= 0)
        #        M50  (existing_debt < 0 -> existing_debt < 1)
        # debt=0, income=6000, score=720 => debt_ratio=0.0 <= 0.4 => "approved"
        result = self.evaluator.evaluate_application(
            credit_score=720, monthly_income=6_000,
            existing_debt=0, has_cosigner=False,
        )
        self.assertEqual("approved", result)

    # ------------------------------------------------------------------ #
    #  evaluate_application -- frontierele ramurii high-income            #
    # ------------------------------------------------------------------ #

    def test_income_exactly_5000_enters_high_income_branch(self) -> None:
        # Ucide: M61  (monthly_income >= 5_000 -> monthly_income > 5_000)
        #        M62  (monthly_income >= 5_000 -> monthly_income >= 5001)
        # income=5000, debt=1000, debt_ratio=0.2<=0.4, score=720>=700 => "approved"
        result = self.evaluator.evaluate_application(
            credit_score=720, monthly_income=5_000,
            existing_debt=1_000, has_cosigner=False,
        )
        self.assertEqual("approved", result)

    def test_debt_ratio_exactly_0_4_enters_high_income_branch(self) -> None:
        # Ucide: M63  (debt_ratio <= 0.4 -> debt_ratio < 0.4:
        #              0.4 < 0.4 ar fi False si n-ar intra in ramura)
        # income=5000, debt=2000 => debt_ratio=0.4, score=720>=700 => "approved"
        result = self.evaluator.evaluate_application(
            credit_score=720, monthly_income=5_000,
            existing_debt=2_000, has_cosigner=False,
        )
        self.assertEqual("approved", result)

    def test_debt_ratio_above_0_4_is_rejected(self) -> None:
        # Ucide: M64  (debt_ratio <= 0.4 -> debt_ratio <= 1.4:
        #              0.6 <= 1.4 ar intra gresit in ramura si ar returna "approved")
        # income=5000, debt=3000 => debt_ratio=0.6 > 0.4 => "rejected"
        result = self.evaluator.evaluate_application(
            credit_score=750, monthly_income=5_000,
            existing_debt=3_000, has_cosigner=False,
        )
        self.assertEqual("rejected", result)

    def test_credit_score_exactly_700_is_approved(self) -> None:
        # Ucide: M66  (credit_score >= 700 -> credit_score > 700)
        #        M67  (credit_score >= 700 -> credit_score >= 701)
        # score=700>=700, income=5000, debt_ratio=0.2<=0.4, no cosigner => "approved"
        result = self.evaluator.evaluate_application(
            credit_score=700, monthly_income=5_000,
            existing_debt=1_000, has_cosigner=False,
        )
        self.assertEqual("approved", result)

    # ------------------------------------------------------------------ #
    #  evaluate_application -- frontierele ramurii medium-income          #
    # ------------------------------------------------------------------ #

    def test_income_exactly_3000_with_cosigner_is_manual_review(self) -> None:
        # Ucide: M71  (monthly_income >= 3_000 -> monthly_income > 3_000)
        #        M72  (monthly_income >= 3_000 -> monthly_income >= 3001)
        # income=3000, debt=900, debt_ratio=0.3<=0.5, cosigner=True, score=600 => "manual_review"
        result = self.evaluator.evaluate_application(
            credit_score=600, monthly_income=3_000,
            existing_debt=900, has_cosigner=True,
        )
        self.assertEqual("manual_review", result)

    def test_debt_ratio_exactly_0_5_with_cosigner_is_manual_review(self) -> None:
        # Ucide: M73  (debt_ratio <= 0.5 -> debt_ratio < 0.5:
        #              0.5 < 0.5 ar fi False si n-ar intra in ramura)
        # income=3000, debt=1500 => debt_ratio=0.5, cosigner=True, score=600 => "manual_review"
        result = self.evaluator.evaluate_application(
            credit_score=600, monthly_income=3_000,
            existing_debt=1_500, has_cosigner=True,
        )
        self.assertEqual("manual_review", result)


if __name__ == "__main__":
    unittest.main()


class LoanEvaluatorMutmutExtraTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evaluator = LoanEvaluator()

    def test_months_61_raises_value_error(self) -> None:
        # Ucide: M7  (MAX_MONTHS=61: cu M7, months=61 nu ar mai ridica exceptie)
        # In codul original, 61 > 60 => ValueError
        with self.assertRaises(ValueError):
            self.evaluator.calculate_interest_rate(
                amount=15_000, months=61, has_salary_account=False
            )
