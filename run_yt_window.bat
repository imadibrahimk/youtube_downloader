@echo off
cd /d "%~dp0" 

IF NOT EXIST env (
    echo Creating virtual environment...
    python -m venv env
)

call env\Scripts\activate.bat

pip install -r requirements.txt

python python.py

pause
