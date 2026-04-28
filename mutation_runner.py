from dataclasses import dataclass
from typing import Callable

from main import LoanEvaluator


class MutantAmountBoundary(LoanEvaluator):
    def validate_loan_amount(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount < 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"


class MutantMediumIncomeNeedsNoCosigner(LoanEvaluator):
    def evaluate_application(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income == 0 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5:
            return "manual_review"

        return "rejected"

    
class MutantCreditThreshold(LoanEvaluator):
    def evaluate_application(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income == 0 else existing_debt / monthly_income

        if credit_score <= 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"


@dataclass(frozen=True)
class Mutant:
    name: str
    description: str
    evaluator_factory: Callable[[], LoanEvaluator]


def core_suite(evaluator: LoanEvaluator) -> None:
    assert evaluator.validate_loan_amount(3_000) == "small"
    assert evaluator.validate_loan_amount(12_000) == "medium"
    assert evaluator.validate_loan_amount(35_000) == "large"
    assert evaluator.calculate_interest_rate(25_000, 12, True) == 0.085
    assert evaluator.calculate_interest_rate(15_000, 48, False) == 0.135
    assert (
        evaluator.evaluate_application(720, 6_000, 2_000, False) == "approved"
    )
    assert (
        evaluator.evaluate_application(540, 9_000, 500, True) == "rejected"
    )
    assert (
        evaluator.evaluate_application(550, 5_500, 1_000, False) == "manual_review"
    )
    assert (
        evaluator.evaluate_application(650, 5_500, 1_000, False) == "manual_review"
    )
    assert (
        evaluator.evaluate_application(610, 3_500, 1_200, True) == "manual_review"
    )
    assert (
        evaluator.evaluate_application(680, 4_000, 2_500, True) == "rejected"
    )


def extended_suite(evaluator: LoanEvaluator) -> None:
    core_suite(evaluator)
    assert evaluator.validate_loan_amount(5_000) == "small"
    assert (
        evaluator.evaluate_application(620, 3_500, 1_000, False) == "rejected"
    )


def run_suite(
    mutants: list[Mutant],
    suite_name: str,
    suite: Callable[[LoanEvaluator], None],
) -> None:
    print(f"Mutation report for {suite_name}")
    print("-" * 60)

    killed = 0
    survived = 0

    for mutant in mutants:
        try:
            suite(mutant.evaluator_factory())
        except AssertionError:
            status = "KILLED"
            killed += 1
        else:
            status = "SURVIVED"
            survived += 1

        print(f"{mutant.name}: {status} | {mutant.description}")

    print("-" * 60)
    print(f"Killed: {killed}")
    print(f"Survived: {survived}")
    print()


def main() -> None:
    mutants = [
        Mutant(
            "M1",
            "Boundary change: `amount <= 5000` -> `amount < 5000`.",
            MutantAmountBoundary,
        ),
        Mutant(
            "M2",
            "Medium-income rule no longer requires a cosigner.",
            MutantMediumIncomeNeedsNoCosigner,
        ),
        Mutant(
            "M3",
            "Credit rejection threshold changed from `< 550` to `<= 550`.",
            MutantCreditThreshold,
        ),
    ]

    run_suite(mutants, "core suite", core_suite)
    run_suite(mutants, "core + additional tests", extended_suite)


if __name__ == "__main__":
    main()
