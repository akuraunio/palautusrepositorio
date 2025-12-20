@echo off
REM Quick test runner and coverage viewer
REM This script runs tests and automatically opens the coverage report

setlocal enabledelayedexpansion

cd /d "%~dp0"

echo.
echo ======================================
echo Kivi-Paperi-Sakset Test Suite
echo ======================================
echo.

REM Check if pytest is installed
python -m pytest --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pytest is not installed
    echo Please install it with: pip install pytest pytest-cov
    exit /b 1
)

echo Installing dependencies...
python -m pip install -q flask pytest pytest-cov

echo.
echo Running tests with coverage...
python -m pytest src/tests -v --cov=src --cov-report=html --cov-report=term-missing

if errorlevel 0 (
    echo.
    echo ======================================
    echo Tests completed successfully!
    echo ======================================
    echo.
    echo Opening coverage report in browser...
    
    if exist htmlcov\index.html (
        start htmlcov\index.html
    ) else (
        echo Coverage report not found at htmlcov\index.html
    )
) else (
    echo.
    echo ======================================
    echo Some tests failed!
    echo ======================================
)

pause
