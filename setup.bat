@echo off
REM Quick setup script for Windows

echo 🚀 Setting up Re-pixel development environment

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.7+ is required
    exit /b 1
)

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo ⚡ Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install package in development mode
echo 📥 Installing re-pixel in development mode...
pip install -e ".[dev]"

echo ✅ Setup complete!
echo.
echo To activate the environment in the future, run:
echo   venv\Scripts\activate.bat
echo.
echo To run tests:
echo   python -m pytest tests/ -v
echo.
echo To run the demo:
echo   python demo.py

pause
