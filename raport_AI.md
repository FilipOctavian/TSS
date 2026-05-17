# Raport privind utilizarea unui tool de inteligenta artificiala in testarea software

## 1. Tool utilizat

Tool-ul folosit pentru generarea automata a testelor a fost Claude (claude.ai), model de limbaj dezvoltat de Anthropic. Referinta utilizata in raport este: Anthropic, Claude, https://claude.ai.

## 2. Promptul utilizat

Promptul transmis catre Claude a avut rolul de a genera o suita initiala de teste unitare pentru clasa `LoanEvaluator`.

```text
Am urmatoarea clasa Python care simuleaza un evaluator de credite bancare:

[codul clasei LoanEvaluator din main.py]

Genereaza o suita completa de teste unitare folosind unittest.
Acopera cat mai multe cazuri posibil.
```

## 3. Testele generate automat

Rezultatul generatiei automate a fost salvat in [tests/test_loan_evaluator_ai_generated.py](tests/test_loan_evaluator_ai_generated.py). Aceasta suita contine 16 teste si acopera cazuri uzuale pentru cele trei metode publice ale clasei.

Pe scurt, testele generate verifica:

- validarea sumelor prea mici si prea mari
- clasificarea valorilor uzuale in `small`, `medium` si `large`
- calculul dobanzii in scenarii simple
- aprobarea, respingerea si review-ul manual pentru cereri de credit
- tratarea valorilor negative

## 4. Comparatie cu suita proiectata manual

| Criteriu | Suita proiectata manual | Suita generata de Claude |
|---|---|---|
| Numar de teste | 37 | 16 |
| Clase de echivalenta | Da, explicit notate | Partial |
| Frontiere exacte | Da | Partial |
| Acoperire statement | Da | Partial |
| Acoperire decizie | Da | Partial |
| Acoperire conditie | Da | Nu este tratata sistematic |
| Basis path | Da | Nu |
| Rezistenta la mutanti | Ridicata dupa extindere | Redusa |

## 5. Observatii tehnice

Claude produce rapid o baza functionala de teste si este util pentru:

- identificarea metodelor publice
- formularea unui schelet de testare
- verificarea scenariilor evidente

Totusi, suita generata automat nu inlocuieste proiectarea formala, deoarece nu selecteaza in mod sistematic valorile de frontiera si nu urmareste traseele independente din graful de control. In acest proiect, exact aceste lipsuri au fost completate ulterior prin teste suplimentare si prin analiza mutantilor.

## 6. Rularea testelor generate de Claude

Testele pot fi rulate direct cu:

```powershell
python -m pytest tests/test_loan_evaluator_ai_generated.py -v
```

Suita a fost pastrata separat, tocmai pentru a permite comparatia cu testele proiectate manual si cu testele derivate din mutmut.

## 7. Concluzie

Claude este eficient pentru generarea rapida a unei baze de testare, dar acoperirea completa cere in continuare interventie umana, selectie explicita de frontiere si verificare prin mutation testing.

## 8. Referinte

[1] Anthropic, Claude, https://claude.ai.
[2] Aniche, Mauricio. *Effective Software Testing: A developer's guide*. Simon and Schuster, 2022.
[3] mutmut - mutation testing tool, https://mutmut.readthedocs.io/.