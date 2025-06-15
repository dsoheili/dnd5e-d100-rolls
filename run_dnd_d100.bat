:: run_dnd_d100.bat
:: Double-click this file to run the D&D D100 Roller

@echo off
cd /d "%~dp0"
python d100_roller_python.py
if errorlevel 1 (
    echo.
    echo Error running the application. Make sure Python is installed.
    echo.
    pause
)