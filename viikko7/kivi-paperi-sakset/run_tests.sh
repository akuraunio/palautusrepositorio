#!/bin/bash
# Test runner script for Kivi-Paperi-Sakset
# This script helps run the test suite with various options

cd "$(dirname "$0")"

if [ -z "$1" ]; then
    echo "Running all tests..."
    python -m pytest src/tests -v
elif [ "$1" = "coverage" ]; then
    echo "Running tests with coverage report..."
    python -m pytest src/tests --cov=src --cov-report=html
    echo "Coverage report generated in htmlcov/index.html"
elif [ "$1" = "fast" ]; then
    echo "Running tests without verbose output..."
    python -m pytest src/tests
elif [ "$1" = "help" ]; then
    echo ""
    echo "Test runner script for Kivi-Paperi-Sakset"
    echo ""
    echo "Usage: ./run_tests.sh [option]"
    echo ""
    echo "Options:"
    echo "  (no option)  - Run all tests with verbose output"
    echo "  coverage     - Run tests with coverage report"
    echo "  fast         - Run tests without verbose output"
    echo "  help         - Show this help message"
    echo ""
else
    echo "Unknown option: $1"
    echo "Use './run_tests.sh help' for usage information"
    exit 1
fi
