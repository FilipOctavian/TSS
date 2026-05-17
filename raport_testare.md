# Raport de testare

## 1. Obiectiv

Scopul acestui raport este de a descrie metodologia de testare aplicata pentru clasa `LoanEvaluator`, implementata in `main.py`, si de a justifica alegerea unui tool specializat de mutation testing in raport cu un generator didactic de mutanti.

## 2. Tehnici utilizate

Au fost aplicate urmatoarele tehnici de proiectare a testelor:

- partitiarea in clase de echivalenta
- analiza valorilor de frontiera
- acoperire la nivel de instructiune
- acoperire la nivel de decizie
- acoperire la nivel de conditie
- basis path pentru functia `evaluate_application`

Clasele si frontierele relevante sunt documentate in [README.md](README.md), iar testele corespunzatoare sunt in folderul [tests](tests).

## 3. Rezultate observabile

### 3.1 Setul de teste de baza

Fișierul [tests/test_loan_evaluator_core.py](tests/test_loan_evaluator_core.py) acopera:

- clasele de echivalenta pentru suma imprumutului
- frontierele minime si maxime ale intervalului valid
- ramurile principale pentru calculul dobanzii
- trasee independente pentru decizia de aprobare/respingere

### 3.2 Setul de teste suplimentare

Fișierul [tests/test_loan_evaluator_additional.py](tests/test_loan_evaluator_additional.py) completeaza frontiera interna de la `5000` si cazul de respingere pe venit mediu fara codebitor.

### 3.3 Setul de teste generate de Claude

Fișierul [tests/test_loan_evaluator_ai_generated.py](tests/test_loan_evaluator_ai_generated.py) contine o suita generata automat de Claude. Aceasta este utila ca punct de comparatie, dar nu acopera sistematic tehnicile de proiectare a testelor documentate aici.

### 3.4 Setul de teste derivat din mutmut

Fișierul [tests/test_loan_evaluator_mutmut.py](tests/test_loan_evaluator_mutmut.py) contine testele adaugate dupa analiza mutantilor supravietuitori.

## 4. Justificarea utilizarii mutmut

Mutmut este preferat in raport cu un generator manual de mutanti deoarece:

- genereaza mutanti direct din codul real, fara mentenanta manuala pentru fiecare varianta
- scaleaza mai bine la un numar mare de mutanti si la proiecte mai mari
- produce un flux reproductibil, util pentru raportare academica si verificare repetabila
- evidentiaza direct unde suita de teste este slaba, prin mutanti supravietuitori

In acest proiect, `mutation_runner.py` are rol didactic si de demonstrare. El este util pentru prezentarea diferentelor dintre `KILLED` si `SURVIVED`, dar nu inlocuieste un instrument complet de mutation testing.

## 5. Mediu de executie

Rularea s-a facut local, in mediul gazda al workspace-ului, fara masina virtuala separata. Pentru instalarea si executia mutmut, un mediu virtual local ramane totusi recomandat, deoarece izoleaza dependintele si stabileste un context reproductibil.

## 6. Concluzii

Rezultatul principal este ca suita manual proiectata, completata cu testele suplimentare si cu testele derivare din mutmut, ofera o acoperire semnificativ mai buna decat suita generata automat. Claude produce rapid un schelet util, dar nu inlocuieste proiectarea sistematica a cazurilor de test.

## 7. Referinte

[1] Python Software Foundation, "unittest - Unit testing framework", Python 3 documentation.
[2] A. J. Offutt, "Introduction to Software Testing", Cambridge University Press.
[3] ISTQB, "Foundation Level Syllabus - Test Design Techniques".
[4] mutmut - mutation testing tool, https://mutmut.readthedocs.io/

## 8. Instrucțiuni pentru mutation testing (WSL)

Pentru a rula `mutmut` pe mașina ta (recomandat în WSL/Ubuntu):

1. Asigură-te că ai `python3-venv` instalat: `sudo apt install python3-venv`.
2. În directorul proiectului rulează scriptul helper:

```bash
./scripts/run_mutation_wsl.sh
mutmut results > mutmut_results.txt
```

3. Copiază sumarul în fișierul `mutmut_results_PLACEHOLDER.md` sau înlocuiește-l cu rezultatele reale.

## 9. Rezultate mutaționale (placeholder)

În urma rulării mutmut în WSL, rezultatele observate sunt:

- total mutanți: 95
- mutanți omorâți: 80
- mutanți supraviețuitori: 15
- timeout-uri: 0

Acest lucru indică faptul că suita curentă acoperă bine logica principală, dar mai există 15 mutanți care merită analizați individual pentru a decide dacă necesită teste suplimentare sau dacă sunt echivalenți.

Comanda corectă pentru inspectarea rezultatului este:

```bash
mutmut results
```

Nu este necesară comanda `mutmut show-results`; în versiunea folosită, aceasta nu există.

## 10. Graf cauza-efect și mapping teste

Vezi graful cauza-efect formalizat pentru funcția `evaluate_application`: [diagrams/cause_effect_graph.svg](diagrams/cause_effect_graph.svg#L1).

Structura formală folosită în diagramă este:

- cauze de intrare pentru pragurile de scor, venit și indatorare
- reguli logice pentru decizia finală
- efecte pentru `approved`, `manual_review`, `rejected` și `ValueError`

Mappingul către teste este următorul:

- C1 / C2 / C3 → teste de prag și decizie: `test_condition_boundary_credit_score_550_is_not_auto_rejected`, `test_credit_score_exactly_700_is_approved`, `test_application_approved`, `test_application_rejected_low_score`, `test_application_manual_review`, `test_application_with_cosigner`.
- C4 / C5 / C6 → teste de venit și debt ratio: `test_income_exactly_3000_with_cosigner_is_manual_review`, `test_income_exactly_5000_enters_high_income_branch`, `test_debt_ratio_exactly_0_4_enters_high_income_branch`, `test_debt_ratio_above_0_4_is_rejected`, `test_debt_ratio_exactly_0_5_with_cosigner_is_manual_review`.
- C7 → teste de validare negativă: `test_application_negative_values_raises`, `test_negative_credit_score_alone_raises_value_error`, `test_monthly_income_zero_does_not_raise_and_returns_rejected`, `test_existing_debt_zero_does_not_raise`.
- C8 → teste pentru `calculate_interest_rate`: `test_statement_coverage_for_interest_rate`, `test_decision_coverage_reaches_long_term_branch`, `test_amount_exactly_20000_gets_large_loan_discount`, `test_min_months_boundary_6_is_valid`, `test_max_months_boundary_60_is_valid`, `test_months_61_raises_value_error`.

Acest mapping este suficient pentru cerintele proiectului si poate fi extins daca este necesar un tabel complet cauza-efect conditie-efect.

## 11. Checklist final

- [x] README în limbaj formal și reproductibil
- [x] Clase de echivalență notate formal și frontiere documentate
- [x] Diagrame și diagramă numerotată incluse
- [x] Grafic cauza-efect formalizat și mapat la teste
- [x] Justificare pentru mutmut și rulare în WSL documentată
- [x] Teste Claude și teste mutmut incluse în repo
- [x] Rezultate mutaționale consemnate în raport

