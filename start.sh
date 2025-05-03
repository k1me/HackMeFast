#!/bin/bash

set -e

if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Nincs virtuális környezet! Futtasd: python -m venv venv"
    exit 1
fi

echo "Szükséges csomagok telepítése..."
pip install -r requirements.txt

cd backend

echo "Adatbázis seedelése..."
python3 -m app.database.seeder

echo "Backend indítása..."
fastapi dev app/main.py &
#alternativ inditas
#uvicorn backend.app.main:app --port 8000 --reload

echo "Frontend indítása..."
cd ../frontend/hackmefast-ui
if command -v ng &>/dev/null; then
    ng serve --open
else
    echo "Nincs Angulár telepítve! Futtasd: npm install -g @angular/cli"
    exit 1
fi
