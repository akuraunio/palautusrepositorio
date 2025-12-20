@echo off
REM Test runner script for Kivi-Paperi-Sakset
REM This script helps run the test suite with various options

setlocal enabledelayedexpansion

cd /d "%~dp0"

if "%1"=="" (
    echo Running all tests...
    python -m pytest src/tests -v
) else if "%1"=="coverage" (
    echo Running tests with coverage report...
    python -m pytest src/tests --cov=src --cov-report=html
    echo Coverage report generated in htmlcov/index.html
) else if "%1"=="fast" (
    echo Running tests without verbose output...
    python -m pytest src/tests
) else if "%1"=="help" (
    echo.
    echo Test runner script for Kivi-Paperi-Sakset
    echo.
    echo Usage: run_tests.bat [option]
    echo.
    echo Options:
    echo   (no option)  - Run all tests with verbose output
    echo   coverage     - Run tests with coverage report
    echo   fast         - Run tests without verbose output
    echo   help         - Show this help message
    echo.
) else (
    echo Unknown option: %1
    echo Use "run_tests.bat help" for usage information
    exit /b 1
)
