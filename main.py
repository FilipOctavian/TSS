class LoanEvaluator:
    MIN_AMOUNT = 1_000
    MAX_AMOUNT = 50_000
    MIN_MONTHS = 6
    MAX_MONTHS = 60

    def validate_loan_amount(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def calculate_interest_rate(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("Repayment period must be between 6 and 60 months.")

        rate = 0.12

        if amount >= 20_000:
            rate -= 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

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

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"
