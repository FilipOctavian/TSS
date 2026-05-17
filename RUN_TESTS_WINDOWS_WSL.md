# Rulare teste: Windows si WSL

## Windows PowerShell

Daca vrei sa rulezi testele in Windows, recreeaza mediul virtual in Windows, nu folosi un `.venv` creat in WSL.

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

Daca vrei sa rulezi in WSL, foloseste mediul virtual creat in WSL.

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

Un mediu virtual creat in WSL nu poate fi folosit direct in PowerShell pe Windows. Daca vezi eroarea cu `/usr/bin/python.exe`, inseamna ca rulezi un venv Linux din Windows si trebuie recreat in mediul corect.
