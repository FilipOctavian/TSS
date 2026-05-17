# Instructiuni de rulare a testelor

Comenzile se ruleaza din radacina proiectului, adica din `C:\Users\Gabriela Matei\Desktop\tss` pe Windows sau din `/mnt/c/Users/Gabriela Matei/Desktop/tss` in WSL.

Atentie: un mediu virtual creat in WSL nu se utilizeaza din PowerShell pe Windows. In acest caz, mediul se recreeaza in Windows sau se ruleaza testele exclusiv din WSL.

## 1. Testele unitare principale

```powershell
python -m unittest discover -s tests -v
```

Acesta reprezinta pasul de baza si trebuie sa treaca inainte de celelalte verificari.

## 2. Runner-ul didactic de mutatii

```powershell
python mutation_runner.py
```

Acesta afiseaza mutanti de tip `KILLED` si `SURVIVED` si sprijina redactarea raportului.

## 3. Mutmut in WSL

In WSL, executarea se realizeaza astfel:

```bash
cd "/mnt/c/Users/Gabriela Matei/Desktop/tss"
source .venv/bin/activate
python -m unittest discover -s tests -v
./scripts/run_mutation_wsl.sh
mutmut results
```

Pentru generarea unui raport text:

```bash
mutmut results > mutmut_results.txt
```

## 4. Ordinea recomandata

1. Se ruleaza testele unitare.
2. Se ruleaza `mutation_runner.py`.
3. Se ruleaza `mutmut` in WSL.
4. Se completeaza raportul cu rezultatele obtinute.

## 5. Ce trebuie verificat

- toate testele din `tests/` trec
- mutmut raporteaza rezultatele asteptate
- in videoclip se vede rularea testelor si a mutation testing-ului

## 6. Video demo

Videoclip demonstrativ: https://youtu.be/19t6CGx_Fvw


