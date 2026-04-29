# Raport privind utilizarea unui tool de Inteligenta Artificiala in testarea software

## 1. Tool utilizat

**Claude** (claude.ai) — model de limbaj de mare dimensiune dezvoltat de Anthropic.  
Data generarii: 29 aprilie 2026  
Referinta: Anthropic, Claude, https://claude.ai, Data generarii: 29 aprilie 2026

---

## 2. Promptul utilizat

Urmatorul prompt a fost trimis catre Claude pentru generarea automata a testelor:

```
Am urmatoarea clasa Python care simuleaza un evaluator de credite bancare:

[codul clasei LoanEvaluator din main.py]

Genereaza o suita completa de teste unitare folosind unittest.
Acopera cat mai multe cazuri posibil.
```

---

## 3. Testele generate automat de Claude

```python
import unittest
from main import LoanEvaluator


class TestLoanEvaluatorAI(unittest.TestCase):

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
```

---

## 4. Comparatie: suita proprie vs. suita generata de AI

| Criteriu | Suita proprie | Suita generata de AI |
|---|---|---|
| Numar total de teste | 37 | 15 |
| Partiționare clase echivalenta | Da (explicit etichetat) | Partial (implicit) |
| Analiza valori de frontiera | Da (999, 1000, 1001, 49999, 50000, 50001) | Nu (lipsesc valorile exacte de frontiera) |
| Acoperire instrucțiune | Da (etichetat explicit) | Partial |
| Acoperire decizie | Da (etichetat explicit) | Nu (neetichetat, partial acoperit) |
| Acoperire condiție | Da (etichetat explicit) | Nu |
| Circuite independente (basis path) | Da (4 cai independente derivate) | Nu |
| Testare mutanti (mutmut) | Da (69/73 mutanti ucisi) | Nu |
| Teste suplimentare post-mutmut | Da (20 teste dedicate) | Nu |
| Frontiera interna 5000 (small vs medium) | Da | Nu |
| Frontiera interna 20000 (medium vs large) | Da | Nu |
| Frontiera 6 luni (MIN_MONTHS) | Da | Nu |
| Frontiera 60 luni (MAX_MONTHS) | Da | Nu |
| Frontiera 36 luni (termen lung exact) | Da | Nu |
| Frontiera 13 luni (fara bonus scurt) | Da | Nu |
| monthly_income = 0 (debt_ratio infinit) | Da | Nu |
| existing_debt = 0 (fara eroare) | Da | Nu |
| credit_score = 0 (valid, respins) | Da | Nu |
| credit_score = 550 exact (nu e respins) | Da | Nu |
| credit_score = 700 exact (aprobat) | Da | Nu |
| monthly_income = 5000 exact | Da | Nu |
| monthly_income = 3000 exact | Da | Nu |
| debt_ratio = 0.4 exact | Da | Nu |
| debt_ratio = 0.5 exact | Da | Nu |

---

## 5. Rularea testelor generate de AI

Testele generate au fost salvate in `tests/test_loan_evaluator_ai_generated.py`
si rulate cu:

```bash
python -m pytest tests/test_loan_evaluator_ai_generated.py -v
```

**Rezultat:** 15 teste, toate trec (`PASSED`).

**Scor de mutatie al suitei AI** (rulat cu mutmut pe aceleasi mutante):  
Suita AI ucide aproximativ 40-45% dintre mutantii generati de mutmut,
comparativ cu 94.5% pentru suita proprie.

---

## 6. Interpretare si concluzii

**Ce face bine AI-ul:**
- Genereaza rapid o suita de baza care acopera cazurile uzuale (happy path + cateva erori)
- Identifica corect cele 3 metode si parametrii lor
- Produce cod sintactic corect, gata de rulat

**Ce lipseste din suita AI:**
- Nu aplica sistematic nicio tehnica de testare (partiționare, frontiere, acoperire)
- Nu testeaza valorile exacte de frontiera (5000, 20000, 6 luni, 60 luni etc.) — tocmai unde apar cel mai frecvent bug-urile
- Nu genereaza teste capabile sa ucida mutantii subtili (de ex. `<=` vs `<`)
- Nu testeaza cazuri-limita importante: income=0, debt=0, score=0, score=700 exact
- Nu deriva circuitele independente din graful de control

**Concluzie:**
Suita generata de AI este un bun punct de plecare — economiseste timp pentru cazurile evidente.
Insa nu poate inlocui o abordare sistematica bazata pe tehnicile formale de testare.
Combinatia optima este: AI pentru schelet initial + tehnici formale aplicate manual pentru
acoperire completa si scor de mutatie ridicat.

---

## 7. Referinte

[1] Anthropic, Claude, https://claude.ai, Data generarii: 29 aprilie 2026  
[2] Aniche, Mauricio. *Effective Software Testing: A developer's guide*. Simon and Schuster, 2022  
[3] mutmut - mutation testing tool, https://mutmut.readthedocs.io/, Data ultimei accesari: 29 aprilie 2026
