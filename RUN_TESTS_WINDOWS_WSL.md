# Instructiuni de rulare: Windows si WSL

## Windows PowerShell

Daca testele se ruleaza in Windows, mediul virtual se recreeaza in Windows; nu se foloseste un `.venv` creat in WSL.

```powershell
deactivate
Remove-Item -Recurse -Force .venv
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
python mutation_runner.py
```

## WSL

Daca testele se ruleaza in WSL, se foloseste mediul virtual creat in WSL.

```bash
cd "/mnt/c/Users/Gabriela Matei/Desktop/tss"
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
./scripts/run_mutation_wsl.sh
mutmut results
```

## Observatie importanta

Un mediu virtual creat in WSL nu poate fi utilizat direct in PowerShell pe Windows. Daca apare eroarea cu `/usr/bin/python.exe`, inseamna ca este rulat un venv Linux din Windows si mediul trebuie recreat in platforma corespunzatoare.
