@echo off
echo.
echo ================================================
echo    Rice Type Detection - Windows Startup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found. Starting application...
echo.

REM Run the startup script
python run.py

echo.
echo Application stopped.
pause 