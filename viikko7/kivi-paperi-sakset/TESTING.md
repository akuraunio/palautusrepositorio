# Automated Tests - Quick Start Guide

## What Was Created

A complete automated test suite for the Kivi-Paperi-Sakset web application with **70+ test cases** covering:

- ✅ Web application routes and requests
- ✅ Game logic and move validation
- ✅ Scoring system (Tuomari) with first-to-5 format
- ✅ AI systems (basic and advanced)
- ✅ Session management
- ✅ Game ending when a player reaches 5 points

## Test Files

```
src/tests/
├── __init__.py              # Makes tests a package
├── conftest.py             # Pytest configuration
├── test_web_app.py         # Flask routes & game adapter (45+ tests)
├── test_tuomari.py         # Scoring logic (10+ tests)
├── test_tekoaly.py         # AI implementations (20+ tests)
├── test_peli_tehdas.py     # Game factory (10+ tests)
└── README.md               # Detailed test documentation
```

## How to Run Tests

### Option 1: Using the test scripts

```bash
# Windows
run_tests.bat                    # Run all tests with verbose output
run_tests.bat coverage           # Run tests with coverage report
run_tests.bat fast               # Run tests (quiet mode)

# Linux/Mac
./run_tests.sh
./run_tests.sh coverage
./run_tests.sh fast
```

### Option 2: Direct pytest commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific file
pytest src/tests/test_web_app.py

# Run with coverage report
pytest --cov=src --cov-report=html

# Run with coverage and missing lines
pytest --cov=src --cov-report=term-missing
```

### Option 3: Using the comprehensive test runner (Windows)

```bash
run_tests_with_coverage.bat
# This automatically installs dependencies, runs tests, and opens coverage report in browser
```

## Test Examples

### Web Application Tests

- Index page loads correctly
- Game modes can be selected
- Moves are processed correctly
- Game ends on invalid move
- Score is tracked properly
- Session management works

### Game Logic Tests

- Valid moves: k (rock), p (paper), s (scissors)
- Invalid moves end the game
- Correct winners determined (rock > scissors > paper > rock)
- Draws detected (same moves)
- Scores accumulated correctly

### AI Tests

- Basic AI follows predictable sequence: k, p, s, k, p, s, ...
- Advanced AI remembers opponent moves
- Advanced AI develops counter-strategies
- Memory management when full

### Factory Tests

- All three game modes create correctly
- Invalid modes handled properly
- Game instances properly initialized

## Example Output

```
$ pytest src/tests -v
================================= test session starts ==================================
src/tests/test_web_app.py::TestIndexRoute::test_index_page_loads PASSED          [ 1%]
src/tests/test_web_app.py::TestIndexRoute::test_index_page_contains_mode_buttons PASSED [ 2%]
src/tests/test_web_app.py::TestGameStartRoute::test_start_game_mode_a PASSED     [ 3%]
src/tests/test_web_app.py::TestGameStartRoute::test_start_game_mode_b PASSED     [ 4%]
...
================================= 70 passed in 2.34s ==================================
```

## Coverage Report

After running tests with coverage, view the report:

- **HTML Report**: Open `htmlcov/index.html` in browser
- **Terminal Report**: Run `pytest --cov=src --cov-report=term-missing`

## Installation

If pytest is not installed:

```bash
pip install pytest pytest-cov
```

Or with poetry:

```bash
poetry install --with dev
```

## Test Structure

Each test file follows this pattern:

```python
import pytest
from module_to_test import ClassName

class TestClassName:
    """Tests for ClassName"""

    def test_specific_functionality(self):
        """Test description"""
        # Arrange
        instance = ClassName()

        # Act
        result = instance.method()

        # Assert
        assert result == expected_value
```

## CI/CD Integration

Tests automatically run on:

- `git push` to main or develop branches
- Pull requests to main or develop
- Supports Python 3.12 and 3.13

See `.github/workflows/tests.yml` for configuration.

## Files Added/Modified

### New Test Files

- `src/tests/test_web_app.py` - Web application tests
- `src/tests/test_tuomari.py` - Scoring tests
- `src/tests/test_tekoaly.py` - AI tests
- `src/tests/test_peli_tehdas.py` - Factory tests
- `src/tests/conftest.py` - Pytest configuration
- `src/tests/README.md` - Test documentation

### Configuration Files

- `pytest.ini` - Pytest configuration
- `.github/workflows/tests.yml` - CI/CD workflow

### Helper Scripts

- `run_tests.bat` - Test runner for Windows
- `run_tests.sh` - Test runner for Linux/Mac
- `run_tests_with_coverage.bat` - Comprehensive test runner with coverage

### Documentation

- `TEST_SUMMARY.md` - This file

## Testing Best Practices Implemented

✅ Comprehensive coverage - All major code paths tested
✅ Isolated tests - No dependencies between tests
✅ Clear naming - Test names describe what they test
✅ Arrange-Act-Assert pattern - Clear test structure
✅ Fixtures - Reusable test setup with pytest fixtures
✅ Parametrization ready - Easy to add parametrized tests
✅ Documentation - Each test is documented
✅ CI/CD integration - Automated test runs

## Common Issues & Solutions

### pytest: command not found

**Solution**: Install pytest with `pip install pytest`

### ImportError: No module named 'src'

**Solution**: Tests use conftest.py to set up the path. This is already configured.

### Tests fail with "No module named flask"

**Solution**: Install flask with `pip install flask`

## Next Steps

1. Run the tests: `pytest` or use one of the test scripts
2. Check coverage: `pytest --cov=src --cov-report=html`
3. View the HTML report in `htmlcov/index.html`
4. Integrate into your CI/CD pipeline
5. Add more tests as you add new features

## Support

For detailed test documentation, see `src/tests/README.md`
