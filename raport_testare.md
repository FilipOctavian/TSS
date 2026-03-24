# Raport testare unitara

## 1. Clasa testata

Exemplul folosit este clasa `LoanEvaluator` din `main.py`. Ea contine trei functionalitati:

- `validate_loan_amount(amount)` valideaza suma si o clasifica in `small`, `medium`, `large`.
- `calculate_interest_rate(amount, months, has_salary_account)` calculeaza dobanda in functie de suma, perioada si existenta unui cont de salariu.
- `evaluate_application(credit_score, monthly_income, existing_debt, has_cosigner)` decide daca o cerere este `approved`, `manual_review` sau `rejected`.

Framework-ul ales este `unittest`, din biblioteca standard Python.

## 2. Strategii de generare a testelor

### Partiționare in clase de echivalenta

Pentru `validate_loan_amount` au fost folosite urmatoarele clase:

- suma invalida sub minim: exemplu `500`
- suma valida mica: exemplu `3000`
- suma valida medie: exemplu `12000`
- suma valida mare: exemplu `35000`
- suma invalida peste maxim: exemplu `70000`

Testele sunt in `tests/test_loan_evaluator_core.py`.

### Analiza valorilor de frontiera

Frontierele alese pentru suma imprumutului:

- `999`, `1000`, `1001`
- `49999`, `50000`, `50001`

Aceste cazuri verifica exact tranzitia intre intrari invalide si valide.

### Acoperire la nivel de instructiune

Testul `test_statement_coverage_for_interest_rate` executa toate instructiunile relevante din:

- validarea sumei
- reducerea pentru suma mare
- reducerea pentru perioada scurta
- reducerea pentru cont de salariu

### Acoperire la nivel de decizie

Testul `test_decision_coverage_reaches_long_term_branch` forteaza ramura `months >= 36`, care este diferita de ramura `months <= 12`.

### Acoperire la nivel de conditie

Testele pentru `evaluate_application` exercita combinatii in care:

- `credit_score >= 700` este adevarat
- `has_cosigner` este adevarat
- `monthly_income >= 5000` este adevarat sau fals
- `debt_ratio <= 0.4` si `debt_ratio <= 0.5` sunt adevarate sau false

### Circuite independente

Pentru `evaluate_application` au fost alese 5 trasee independente:

1. scor de credit sub 550 -> `rejected`
2. venit mare + datorie acceptabila + scor mare -> `approved`
3. venit mare + datorie acceptabila + scor sub 700 fara codebitor -> `manual_review`
4. venit mediu + codebitor + datorie acceptabila -> `manual_review`
5. alt caz ramas -> `rejected`

Acestea sunt ilustrate de testele `test_basis_path_*`.

## 3. Mutații si analiza raportului

Scriptul `mutation_runner.py` joaca rolul unui generator simplu de mutanti si evalueaza doua suite:

- suita de baza: aceleasi idei ca in `tests/test_loan_evaluator_core.py`
- suita extinsa: suita de baza + testele suplimentare din `tests/test_loan_evaluator_additional.py`

Mutantii definiti:

- `M1`: schimba `amount <= 5000` in `amount < 5000`
- `M2`: elimina conditia `has_cosigner` din regula pentru venit mediu
- `M3`: schimba pragul de respingere din `credit_score < 550` in `credit_score <= 550`

### Interpretare asteptata a raportului

Cu suita de baza:

- `M3` este omorat
- `M1` si `M2` supravietuiesc

Motiv:

- suita de baza nu testeaza exact valoarea `5000`
- suita de baza nu testeaza cazul de venit mediu fara codebitor

### Teste suplimentare pentru a omori 2 mutanti neechivalenti ramasi in viata

In `tests/test_loan_evaluator_additional.py` au fost adaugate doua teste:

- `test_amount_boundary_exactly_5000_is_still_small` omoara mutantul `M1`
- `test_application_is_rejected_without_cosigner_on_medium_income` omoara mutantul `M2`

Astfel, dupa extinderea suitei, toti cei 3 mutanti sunt omorati.

## 4. Rulare

Pentru teste:

```powershell
.\myvenv\Scripts\python.exe -m unittest discover -s tests -v
```

Pentru raportul de mutatii:

```powershell
.\myvenv\Scripts\python.exe mutation_runner.py
```
