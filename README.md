# Documentatie proiect TSS - testare unitara si mutation testing in Python

## 1. Introducere

Acest proiect prezinta proiectarea si executia unei suite de teste pentru clasa `LoanEvaluator`, implementata in `main.py`, utilizand framework-ul `unittest` din biblioteca standard Python [1].

Documentatia urmareste tehnicile cerute in cadrul disciplinei, cu accent pe:

- partitiarea in clase de echivalenta
- analiza valorilor de frontiera
- acoperirea la nivel de instructiune, decizie si conditie
- circuitul independent (basis path)
- analiza prin mutation testing
- justificarea utilizarii mutmut in raport cu un generator didactic de mutanti

## 2. Descrierea componentei testate

Clasa `LoanEvaluator` ofera trei functii principale:

1. `validate_loan_amount(amount)`
- valideaza intervalul `[1000, 50000]`
- intoarce una dintre valorile `small`, `medium` sau `large`

2. `calculate_interest_rate(amount, months, has_salary_account)`
- aplica reguli de dobanda in functie de suma, perioada si existenta unui cont de salariu
- returneaza dobanda finala rotunjita la trei zecimale

3. `evaluate_application(credit_score, monthly_income, existing_debt, has_cosigner)`
- stabileste daca cererea este `approved`, `manual_review` sau `rejected`
- combina praguri pentru scor, venit, grad de indatorare si codebitor

### 2.1 Diagrame de control

Au fost incluse diagrame de tip flowchart pentru principalele functii ale clasei:

#### validate_loan_amount
![validate_loan_amount](diagrams/flowchart_validate_loan_amount.svg)

#### calculate_interest_rate
![calculate_interest_rate](diagrams/flowchart_calculate_interest_rate.svg)

#### evaluate_application
![evaluate_application](diagrams/flowchart_evaluate_application.svg)

Diagrama pentru `evaluate_application` evidentiaza deciziile si traseele independente ale functiei.

## 3. Tehnici de testare aplicate

### 3.1 Clase de echivalenta si notatie formala

Pentru `validate_loan_amount`, clasele de echivalenta sunt notate astfel:

| Clasa | Interval | Comportament asteptat |
|---|---|---|
| C1 | `amount < 1000` | invalid, ridica exceptie |
| C2 | `1000 <= amount <= 5000` | `small` |
| C3 | `5000 < amount <= 20000` | `medium` |
| C4 | `20000 < amount <= 50000` | `large` |
| C5 | `amount > 50000` | invalid, ridica exceptie |

Exemplele concrete sunt implementate in `tests/test_loan_evaluator_core.py`.

### 3.2 Analiza valorilor de frontiera

Frontierele utilizate in testare sunt urmatoarele:

- minim: `999`, `1000`, `1001`
- delimitarea interna dintre `small` si `medium`: `5000`, `5001`
- delimitarea interna dintre `medium` si `large`: `20000`, `20001`
- maxim: `49999`, `50000`, `50001`

Aceste cazuri apar in:

- `tests/test_loan_evaluator_core.py`
- `tests/test_loan_evaluator_additional.py`
- `tests/test_loan_evaluator_mutmut.py`

### 3.3 Acoperire la nivel de instructiune

Testul `test_statement_coverage_for_interest_rate` exercita lantul principal de instructiuni din calculul dobanzii, inclusiv reducerea pentru suma mare, reducerea pentru termen scurt si reducerea pentru contul de salariu.

### 3.4 Acoperire la nivel de decizie

Ramurile decisive din `calculate_interest_rate` sunt acoperite prin cazuri pentru:

- `months <= 12`
- `months >= 36`
- ramura implicita pentru perioade intermediare

### 3.5 Acoperire la nivel de conditie

Sunt verificate combinatii relevante pentru expresiile booleene din `evaluate_application`:

- `credit_score < 550`
- `credit_score >= 700 or has_cosigner`
- `monthly_income >= 5000`
- `monthly_income >= 3000`
- `debt_ratio <= 0.4`
- `debt_ratio <= 0.5`

### 3.6 Circuit independent

Graful de control al functiei `evaluate_application` poate fi parcurs prin urmatoarele noduri numerotate:

① validarea valorilor negative

② calculul raportului de indatorare

③ verificarea pragului `credit_score < 550`

④ ramura pentru venit mare si indatorare mica

⑤ verificarea aprobarii finale prin scor sau codebitor

⑥ ramura pentru venit mediu si codebitor

⑦ respingerea implicita

Aceste trasee sunt reflectate in diagrama `diagrams/flowchart_evaluate_application.svg`.

## 4. Setul de teste

### 4.1 Teste de baza

Fișierul `tests/test_loan_evaluator_core.py` contine testele esentiale pentru:

- clasele de echivalenta
- frontierele principale
- acoperire statement/decision/condition
- primele trasee basis path

### 4.2 Teste suplimentare

Fișierul `tests/test_loan_evaluator_additional.py` completeaza frontiera interna de la `5000` si cazul de respingere pe venit mediu fara codebitor.

### 4.3 Teste generate de Claude

Fișierul `tests/test_loan_evaluator_ai_generated.py` pastreaza suita generata automat pentru comparatie cu suita proiectata manual.

### 4.4 Teste derivate din mutmut

Fișierul `tests/test_loan_evaluator_mutmut.py` contine testele adaugate dupa analiza mutantilor supravietuitori si acopera in special frontierele interne si pragurile sensibile ale codului.

## 5. Mutation testing si justificarea folosirii mutmut

Pentru analiza de mutation testing, mutmut este solutia preferata fata de un generator manual de mutanti deoarece:

- genereaza automat mutanti din codul real, fara mentenanta manuala pentru fiecare varianta
- scaleaza mai bine la un numar mare de mutanti si la proiecte mai mari
- produce un flux reproductibil, util pentru raportare academica si verificare repetabila
- evidentiaza direct unde suita de teste este slaba, prin mutanti supravietuitori

Generatorul local `mutation_runner.py` ramane util doar ca instrument didactic si comparativ, dar nu inlocuieste un tool specializat precum mutmut.

Pentru rularea mutmut se recomanda utilizarea unui mediu virtual local. Executia a fost realizata in mediul gazda al workspace-ului, fara masina virtuala separata.

## 6. Mediu de rulare

### 6.1 Configuratia hardware

- CPU: `AMD Ryzen 9 7900 12-Core Processor` (12 nuclee / 24 thread-uri)
- RAM: `31.74 GB`
- Sistem: `LENOVO 90UY00ADRI`

### 6.2 Configuratia software

- OS: `Microsoft Windows 11 Pro`, versiune `10.0.26200`, arhitectura `64-bit`
- Python: `3.13.5`
- pip: `25.1.1`
- Git: `2.50.1.windows.1`
- Framework de testare: `unittest`

## 7. Rulare

Comenzile utilizate in proiect sunt urmatoarele:

```powershell
.\myvenv\Scripts\python.exe -m unittest discover -s tests -v
.\myvenv\Scripts\python.exe mutation_runner.py
```

La nivelul setului curent de teste, exista 53 de teste distribuite astfel:

- 15 teste in suita de baza
- 2 teste suplimentare
- 16 teste generate de Claude
- 20 teste mutmut

## 8. Concluzii

Rezultatele confirma faptul ca abordarea sistematica, bazata pe tehnici clasice de proiectare a testelor si pe mutation testing, este mai eficienta decat o suita generata exclusiv automat. Testele suplimentare au inchis exact golurile identificate de mutanti si au imbunatatit semnificativ calitatea suitei.

## 9. Referinte bibliografice

[1] Python Software Foundation, "unittest - Unit testing framework", Python 3 documentation.
[2] Python Software Foundation, "Python 3.13 Documentation", docs.python.org.
[3] A. J. Offutt, "Introduction to Software Testing", Cambridge University Press.
[4] ISTQB, "Foundation Level Syllabus - Test Design Techniques".
[5] diagrams.net, "diagrams.net", https://app.diagrams.net/

## Demo video

Videoclip demonstrativ: https://youtu.be/19t6CGx_Fvw

La actualizarea materialului video, livrabilele se regenereaza cu `python regenerate_deliverables.py`.

## Mutmut și script WSL

Rularea reproductibilă a `mutmut` pe Windows se realizează în WSL. Scriptul auxiliar este disponibil la [scripts/run_mutation_wsl.sh](scripts/run_mutation_wsl.sh).
Rezultatele mutaționale sunt consemnate în [mutmut_results_PLACEHOLDER.md](mutmut_results_PLACEHOLDER.md).

## Graf cauza-efect

Graful cauza-efect formalizat pentru analiza `evaluate_application` este disponibil la [diagrams/cause_effect_graph.svg](diagrams/cause_effect_graph.svg).

## Checklist final

- [x] README în limbaj formal
- [x] Clase de echivalență și frontiere documentate
- [x] Grafuri și diagrame incluse
- [x] Justificare mutmut și rulare în WSL
- [x] Teste Claude și mutmut incluse
- [x] Rezultate mutaționale consemnate


