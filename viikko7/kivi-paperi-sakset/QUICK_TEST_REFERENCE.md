# Quick Reference - Test Commands

## Running Tests

### All Tests (Recommended)

```bash
pytest                          # Run everything
pytest -v                       # Verbose output
pytest -v --tb=short            # Short error messages
```

### With Coverage

```bash
pytest --cov=src                                    # Terminal report
pytest --cov=src --cov-report=html                 # HTML report
pytest --cov=src --cov-report=term-missing         # Show missing lines
```

### Specific Tests

```bash
pytest src/tests/test_web_app.py                   # One file
pytest src/tests/test_web_app.py::TestIndexRoute   # One class
pytest src/tests/test_web_app.py::TestIndexRoute::test_index_page_loads  # One test
```

### Watch Mode (continuous testing)

```bash
pip install pytest-watch
ptw                             # Auto-run on file changes
```

## Using Test Scripts

### Windows

```bash
run_tests.bat                   # All tests, verbose
run_tests.bat coverage          # Tests + coverage HTML report
run_tests.bat fast              # All tests, quiet
run_tests_with_coverage.bat     # Full setup + coverage in browser
```

### Linux/Mac

```bash
chmod +x run_tests.sh           # Make executable (first time only)
./run_tests.sh                  # All tests, verbose
./run_tests.sh coverage         # Tests + coverage HTML report
./run_tests.sh fast             # All tests, quiet
```

## Installation (First Time)

```bash
# Install test dependencies
pip install pytest pytest-cov

# Or using poetry
poetry install --with dev
```

## View Coverage Report

After running tests with coverage:

```bash
# Open in browser (Windows)
start htmlcov\index.html

# Open in browser (Linux)
xdg-open htmlcov/index.html

# Open in browser (Mac)
open htmlcov/index.html
```

## Common Issues

| Issue                                        | Solution                                         |
| -------------------------------------------- | ------------------------------------------------ |
| pytest not found                             | `pip install pytest pytest-cov`                  |
| ImportError: No module named 'src'           | Run from project root, conftest.py handles paths |
| ModuleNotFoundError: No module named 'flask' | `pip install flask`                              |
| No tests collected                           | Tests are in `src/tests/test_*.py`               |

## Test Count by File

| File                | Tests   |
| ------------------- | ------- |
| test_web_app.py     | 25+     |
| test_tekoaly.py     | 20+     |
| test_tuomari.py     | 10+     |
| test_peli_tehdas.py | 10+     |
| **Total**           | **70+** |

## Test Categories

| Category   | Tests |
| ---------- | ----- |
| Web Routes | 20+   |
| Game Logic | 15+   |
| Scoring    | 10+   |
| AI         | 20+   |
| Factory    | 10+   |

## Documentation Files

| File                | Purpose                               |
| ------------------- | ------------------------------------- |
| TESTING.md          | 👈 Start here! Quick start guide      |
| TEST_SUMMARY.md     | Detailed test documentation           |
| CREATED_TESTS.md    | Complete overview of what was created |
| src/tests/README.md | In-depth test file descriptions       |

## Quick Test Run Example

```bash
$ cd viikko7/kivi-paperi-sakset
$ pip install pytest
$ pytest -v

================================ test session starts ==================================
platform win32 -- Python 3.13.2, pytest-7.4.0
rootdir: C:\...\kivi-paperi-sakset, configfile: pytest.ini
collected 70 items

src/tests/test_web_app.py::TestIndexRoute::test_index_page_loads PASSED            [  1%]
src/tests/test_web_app.py::TestIndexRoute::test_index_page_contains_mode_buttons P [  2%]
...
================================== 70 passed in 2.45s ===================================
```

## Pro Tips

1. **Run tests before committing**

   ```bash
   pytest && git commit
   ```

2. **Run specific test while developing**

   ```bash
   pytest src/tests/test_web_app.py::TestIndexRoute::test_index_page_loads -v
   ```

3. **Generate coverage and view in one command**

   ```bash
   pytest --cov=src --cov-report=html && start htmlcov\index.html
   ```

4. **Run tests with different verbosity levels**

   ```bash
   pytest           # Quiet
   pytest -v        # Verbose
   pytest -vv       # Very verbose
   ```

5. **Save test results to file**
   ```bash
   pytest --tb=short > test_results.txt
   pytest --cov=src > coverage_report.txt
   ```

## GitHub Actions

Tests automatically run on:

- Push to main or develop branches
- Pull requests to main or develop
- Configured in `.github/workflows/tests.yml`

## Need Help?

1. Read TESTING.md for quick start
2. Check TEST_SUMMARY.md for detailed info
3. See src/tests/README.md for specific test details
4. Run `pytest --help` for pytest options
