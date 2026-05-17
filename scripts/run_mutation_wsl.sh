#!/usr/bin/env bash
set -euo pipefail

echo "Ensure python3-venv is installed: sudo apt install python3-venv"
echo "Creating venv..."
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Running mutmut (this may take a while)"
mutmut run
echo "Done. Use 'mutmut results' and 'mutmut show-results' to inspect details"
