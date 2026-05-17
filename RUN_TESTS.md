# Cum rulezi testele

Ruleaza comenzile din radacina proiectului, adica din `C:\Users\Gabriela Matei\Desktop\tss` pe Windows sau din `/mnt/c/Users/Gabriela Matei/Desktop/tss` in WSL.

Important: nu folosi acelasi folder `.venv` creat in WSL din PowerShell pe Windows. Daca ai creat mediul in WSL, recreeaza-l separat in Windows sau ruleaza testele doar din WSL.

## 1. Testele unitare principale

```powershell
python -m unittest discover -s tests -v
```

Acesta este pasul de baza si trebuie sa treaca inainte de orice altceva.

## 2. Runner-ul didactic de mutatii

```powershell
python mutation_runner.py
```

Acesta arata mutanti de tip `KILLED` si `SURVIVED` si ajuta la raport.

## 3. Mutmut in WSL

In WSL:

```bash
cd "/mnt/c/Users/Gabriela Matei/Desktop/tss"
source .venv/bin/activate
python -m unittest discover -s tests -v
./scripts/run_mutation_wsl.sh
mutmut results
```

Daca vrei raport text:

```bash
mutmut results > mutmut_results.txt
```

## 4. Ordinea recomandata

1. Rulezi testele unitare.
2. Rulezi `mutation_runner.py`.
3. Rulezi `mutmut` in WSL.
4. Completezi raportul cu rezultatele obtinute.

## 5. Ce trebuie verificat

- toate testele din `tests/` trec
- mutmut raporteaza rezultatele asteptate
- poti arata in video ca ai rulat testele si mutation testing-ul

## 6. Video demo

Videoclip demo: https://youtu.be/19t6CGx_Fvw


