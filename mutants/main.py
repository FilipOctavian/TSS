from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
class LoanEvaluator:
    MIN_AMOUNT = 1_000
    MAX_AMOUNT = 50_000
    MIN_MONTHS = 6
    MAX_MONTHS = 60

    def validate_loan_amount(self, amount: int) -> str:
        args = [amount]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_orig'), object.__getattribute__(self, 'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_mutants'), args, kwargs, self)

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_orig(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_1(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT and amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_2(self, amount: int) -> str:
        if amount <= self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_3(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount >= self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_4(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError(None)

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_5(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("XXLoan amount must be between 1000 and 50000.XX")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_6(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_7(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("LOAN AMOUNT MUST BE BETWEEN 1000 AND 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_8(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount < 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_9(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5001:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_10(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "XXsmallXX"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_11(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "SMALL"
        if amount <= 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_12(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount < 20_000:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_13(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20001:
            return "medium"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_14(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "XXmediumXX"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_15(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "MEDIUM"
        return "large"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_16(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "XXlargeXX"

    def xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_17(self, amount: int) -> str:
        if amount < self.MIN_AMOUNT or amount > self.MAX_AMOUNT:
            raise ValueError("Loan amount must be between 1000 and 50000.")

        if amount <= 5_000:
            return "small"
        if amount <= 20_000:
            return "medium"
        return "LARGE"
    
    xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_1': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_1, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_2': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_2, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_3': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_3, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_4': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_4, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_5': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_5, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_6': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_6, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_7': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_7, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_8': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_8, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_9': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_9, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_10': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_10, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_11': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_11, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_12': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_12, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_13': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_13, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_14': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_14, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_15': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_15, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_16': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_16, 
        'xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_17': xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_17
    }
    xǁLoanEvaluatorǁvalidate_loan_amount__mutmut_orig.__name__ = 'xǁLoanEvaluatorǁvalidate_loan_amount'

    def calculate_interest_rate(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        args = [amount, months, has_salary_account]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_orig'), object.__getattribute__(self, 'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_mutants'), args, kwargs, self)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_orig(
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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_1(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(None)

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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_2(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS and months > self.MAX_MONTHS:
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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_3(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months <= self.MIN_MONTHS or months > self.MAX_MONTHS:
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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_4(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months >= self.MAX_MONTHS:
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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_5(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError(None)

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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_6(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("XXRepayment period must be between 6 and 60 months.XX")

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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_7(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("repayment period must be between 6 and 60 months.")

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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_8(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("REPAYMENT PERIOD MUST BE BETWEEN 6 AND 60 MONTHS.")

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

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_9(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("Repayment period must be between 6 and 60 months.")

        rate = None

        if amount >= 20_000:
            rate -= 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_10(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("Repayment period must be between 6 and 60 months.")

        rate = 1.12

        if amount >= 20_000:
            rate -= 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_11(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("Repayment period must be between 6 and 60 months.")

        rate = 0.12

        if amount > 20_000:
            rate -= 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_12(
        self,
        amount: int,
        months: int,
        has_salary_account: bool,
    ) -> float:
        self.validate_loan_amount(amount)

        if months < self.MIN_MONTHS or months > self.MAX_MONTHS:
            raise ValueError("Repayment period must be between 6 and 60 months.")

        rate = 0.12

        if amount >= 20001:
            rate -= 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_13(
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
            rate = 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_14(
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
            rate += 0.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_15(
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
            rate -= 1.01

        if months <= 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_16(
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

        if months < 12:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_17(
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

        if months <= 13:
            rate -= 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_18(
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
            rate = 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_19(
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
            rate += 0.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_20(
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
            rate -= 1.02
        elif months >= 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_21(
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
        elif months > 36:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_22(
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
        elif months >= 37:
            rate += 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_23(
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
            rate = 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_24(
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
            rate -= 0.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_25(
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
            rate += 1.015

        if has_salary_account:
            rate -= 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_26(
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
            rate = 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_27(
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
            rate += 0.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_28(
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
            rate -= 1.005

        return round(rate, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_29(
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

        return round(None, 3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_30(
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

        return round(rate, None)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_31(
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

        return round(3)

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_32(
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

        return round(rate, )

    def xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_33(
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

        return round(rate, 4)
    
    xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_1': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_1, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_2': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_2, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_3': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_3, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_4': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_4, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_5': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_5, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_6': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_6, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_7': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_7, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_8': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_8, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_9': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_9, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_10': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_10, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_11': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_11, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_12': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_12, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_13': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_13, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_14': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_14, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_15': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_15, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_16': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_16, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_17': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_17, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_18': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_18, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_19': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_19, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_20': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_20, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_21': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_21, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_22': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_22, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_23': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_23, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_24': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_24, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_25': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_25, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_26': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_26, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_27': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_27, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_28': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_28, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_29': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_29, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_30': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_30, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_31': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_31, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_32': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_32, 
        'xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_33': xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_33
    }
    xǁLoanEvaluatorǁcalculate_interest_rate__mutmut_orig.__name__ = 'xǁLoanEvaluatorǁcalculate_interest_rate'

    def evaluate_application(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        args = [credit_score, monthly_income, existing_debt, has_cosigner]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁLoanEvaluatorǁevaluate_application__mutmut_orig'), object.__getattribute__(self, 'xǁLoanEvaluatorǁevaluate_application__mutmut_mutants'), args, kwargs, self)

    def xǁLoanEvaluatorǁevaluate_application__mutmut_orig(
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_1(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 and existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_2(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 and monthly_income < 0 or existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_3(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score <= 0 or monthly_income < 0 or existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_4(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 1 or monthly_income < 0 or existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_5(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income <= 0 or existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_6(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 1 or existing_debt < 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_7(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt <= 0:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_8(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 1:
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_9(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError(None)

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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_10(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("XXApplication values cannot be negative.XX")

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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_11(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("application values cannot be negative.")

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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_12(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("APPLICATION VALUES CANNOT BE NEGATIVE.")

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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_13(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = None

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_14(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float(None) if monthly_income == 0 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_15(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("XXinfXX") if monthly_income == 0 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_16(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("INF") if monthly_income == 0 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_17(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income != 0 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_18(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income == 1 else existing_debt / monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_19(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income == 0 else existing_debt * monthly_income

        if credit_score < 550:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_20(
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

    def xǁLoanEvaluatorǁevaluate_application__mutmut_21(
        self,
        credit_score: int,
        monthly_income: int,
        existing_debt: int,
        has_cosigner: bool,
    ) -> str:
        if credit_score < 0 or monthly_income < 0 or existing_debt < 0:
            raise ValueError("Application values cannot be negative.")

        debt_ratio = float("inf") if monthly_income == 0 else existing_debt / monthly_income

        if credit_score < 551:
            return "rejected"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_22(
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
            return "XXrejectedXX"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_23(
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
            return "REJECTED"

        if monthly_income >= 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_24(
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

        if monthly_income >= 5_000 or debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_25(
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

        if monthly_income > 5_000 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_26(
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

        if monthly_income >= 5001 and debt_ratio <= 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_27(
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

        if monthly_income >= 5_000 and debt_ratio < 0.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_28(
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

        if monthly_income >= 5_000 and debt_ratio <= 1.4:
            if credit_score >= 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_29(
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
            if credit_score >= 700 and has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_30(
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
            if credit_score > 700 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_31(
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
            if credit_score >= 701 or has_cosigner:
                return "approved"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_32(
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
                return "XXapprovedXX"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_33(
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
                return "APPROVED"
            return "manual_review"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_34(
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
            return "XXmanual_reviewXX"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_35(
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
            return "MANUAL_REVIEW"

        if monthly_income >= 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_36(
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

        if monthly_income >= 3_000 and debt_ratio <= 0.5 or has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_37(
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

        if monthly_income >= 3_000 or debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_38(
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

        if monthly_income > 3_000 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_39(
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

        if monthly_income >= 3001 and debt_ratio <= 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_40(
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

        if monthly_income >= 3_000 and debt_ratio < 0.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_41(
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

        if monthly_income >= 3_000 and debt_ratio <= 1.5 and has_cosigner:
            return "manual_review"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_42(
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
            return "XXmanual_reviewXX"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_43(
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
            return "MANUAL_REVIEW"

        return "rejected"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_44(
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

        return "XXrejectedXX"

    def xǁLoanEvaluatorǁevaluate_application__mutmut_45(
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

        return "REJECTED"
    
    xǁLoanEvaluatorǁevaluate_application__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁLoanEvaluatorǁevaluate_application__mutmut_1': xǁLoanEvaluatorǁevaluate_application__mutmut_1, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_2': xǁLoanEvaluatorǁevaluate_application__mutmut_2, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_3': xǁLoanEvaluatorǁevaluate_application__mutmut_3, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_4': xǁLoanEvaluatorǁevaluate_application__mutmut_4, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_5': xǁLoanEvaluatorǁevaluate_application__mutmut_5, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_6': xǁLoanEvaluatorǁevaluate_application__mutmut_6, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_7': xǁLoanEvaluatorǁevaluate_application__mutmut_7, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_8': xǁLoanEvaluatorǁevaluate_application__mutmut_8, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_9': xǁLoanEvaluatorǁevaluate_application__mutmut_9, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_10': xǁLoanEvaluatorǁevaluate_application__mutmut_10, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_11': xǁLoanEvaluatorǁevaluate_application__mutmut_11, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_12': xǁLoanEvaluatorǁevaluate_application__mutmut_12, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_13': xǁLoanEvaluatorǁevaluate_application__mutmut_13, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_14': xǁLoanEvaluatorǁevaluate_application__mutmut_14, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_15': xǁLoanEvaluatorǁevaluate_application__mutmut_15, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_16': xǁLoanEvaluatorǁevaluate_application__mutmut_16, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_17': xǁLoanEvaluatorǁevaluate_application__mutmut_17, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_18': xǁLoanEvaluatorǁevaluate_application__mutmut_18, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_19': xǁLoanEvaluatorǁevaluate_application__mutmut_19, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_20': xǁLoanEvaluatorǁevaluate_application__mutmut_20, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_21': xǁLoanEvaluatorǁevaluate_application__mutmut_21, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_22': xǁLoanEvaluatorǁevaluate_application__mutmut_22, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_23': xǁLoanEvaluatorǁevaluate_application__mutmut_23, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_24': xǁLoanEvaluatorǁevaluate_application__mutmut_24, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_25': xǁLoanEvaluatorǁevaluate_application__mutmut_25, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_26': xǁLoanEvaluatorǁevaluate_application__mutmut_26, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_27': xǁLoanEvaluatorǁevaluate_application__mutmut_27, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_28': xǁLoanEvaluatorǁevaluate_application__mutmut_28, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_29': xǁLoanEvaluatorǁevaluate_application__mutmut_29, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_30': xǁLoanEvaluatorǁevaluate_application__mutmut_30, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_31': xǁLoanEvaluatorǁevaluate_application__mutmut_31, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_32': xǁLoanEvaluatorǁevaluate_application__mutmut_32, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_33': xǁLoanEvaluatorǁevaluate_application__mutmut_33, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_34': xǁLoanEvaluatorǁevaluate_application__mutmut_34, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_35': xǁLoanEvaluatorǁevaluate_application__mutmut_35, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_36': xǁLoanEvaluatorǁevaluate_application__mutmut_36, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_37': xǁLoanEvaluatorǁevaluate_application__mutmut_37, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_38': xǁLoanEvaluatorǁevaluate_application__mutmut_38, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_39': xǁLoanEvaluatorǁevaluate_application__mutmut_39, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_40': xǁLoanEvaluatorǁevaluate_application__mutmut_40, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_41': xǁLoanEvaluatorǁevaluate_application__mutmut_41, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_42': xǁLoanEvaluatorǁevaluate_application__mutmut_42, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_43': xǁLoanEvaluatorǁevaluate_application__mutmut_43, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_44': xǁLoanEvaluatorǁevaluate_application__mutmut_44, 
        'xǁLoanEvaluatorǁevaluate_application__mutmut_45': xǁLoanEvaluatorǁevaluate_application__mutmut_45
    }
    xǁLoanEvaluatorǁevaluate_application__mutmut_orig.__name__ = 'xǁLoanEvaluatorǁevaluate_application'
