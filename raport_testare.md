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

Fișierul [tests/test_loan_evaluator_ai_generated.py](tests/test_loan_evaluator_ai_generated.py) contine o suita generata automat de Claude. Aceasta este utila ca punct de comparatie, dar nu acopera sistematic tehnicile cerute la curs.

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
