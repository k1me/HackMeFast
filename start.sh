#!/bin/bash

#leginkabb friss inditasra szolgal, de ha az azadbazist szeretnenk resetelni alap allapotba, annak is megfelel

set -e

if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Nincs virtuális környezet! Futtasd: python -m venv venv"
    exit 1
fi

pip install -r requirements.txt

python backend/app/database.py

fastapi dev backend/app/main.py
#uvicorn backend.app.main:app --port 8000 --reload