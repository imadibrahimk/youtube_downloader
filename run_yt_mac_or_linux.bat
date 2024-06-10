#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi

source env/bin/activate

pip install -r requirements.txt

python3 python.py
