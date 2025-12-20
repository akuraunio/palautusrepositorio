# Test Suite for Kivi-Paperi-Sakset Web Application

This directory contains comprehensive automated tests for the Kivi-Paperi-Sakset (Rock-Paper-Scissors) game application.

## Test Files

### `test_web_app.py`
Tests for the Flask web application and the `WebKiviPaperiSakset` game adapter:
- **TestIndexRoute**: Tests for the main index page
- **TestGameStartRoute**: Tests for starting games with different modes
- **TestPlayRoute**: Tests for the game play page
- **TestMoveRoute**: Tests for making valid and invalid moves
- **TestResetRoute**: Tests for resetting games
- **TestWebKiviPaperiSakset**: Tests for the game adapter logic

### `test_tuomari.py`
Tests for the Tuomari (judge/referee) class:
- Game point tracking
- Win/loss/draw determination
- Score formatting
- Multiple game tracking

### `test_tekoaly.py`
Tests for both AI implementations:
- **TestTekoaly**: Tests for basic AI with fixed pattern
- **TestTekoalyParannettu**: Tests for advanced AI with memory and strategy
- **TestTekoalyIntegration**: Integration tests between different AI types

### `test_peli_tehdas.py`
Tests for the game factory:
- Creating different game types (Player vs Player, vs AI, vs Advanced AI)
- Invalid mode handling
- Game instance validation

### `conftest.py`
Pytest configuration and shared fixtures:
- Python path setup for importing modules

## Running Tests

### Install test dependencies
```bash
pip install pytest pytest-cov
```

Or using poetry:
```bash
poetry install --with dev
```

### Run all tests
```bash
pytest
```

### Run tests with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest src/tests/test_web_app.py
```

### Run specific test class
```bash
pytest src/tests/test_web_app.py::TestIndexRoute
```

### Run specific test
```bash
pytest src/tests/test_web_app.py::TestIndexRoute::test_index_page_loads
```

### Run tests with coverage report
```bash
pytest --cov=src --cov-report=html
```

This generates an HTML coverage report in `htmlcov/index.html`

### Run tests with coverage in terminal
```bash
pytest --cov=src --cov-report=term-missing
```

### Run tests in watch mode (requires pytest-watch)
```bash
# Install: pip install pytest-watch
ptw
```

## Test Coverage

The test suite covers:
- **Web Interface**: All Flask routes and HTTP methods
- **Game Logic**: Move validation, win determination, scoring
- **AI Behavior**: Basic and advanced AI move patterns
- **Game State Management**: Session handling, game reset, move history
- **Error Handling**: Invalid moves, missing sessions, invalid game modes
- **Score Tracking**: Point accumulation, draw tracking, score formatting

## Key Test Scenarios

### Web Application Tests
- Starting games with all three modes (player vs player, vs AI, vs advanced AI)
- Making valid moves (rock, paper, scissors)
- Handling invalid moves (ending the game)
- Resetting games and returning to main menu
- Session management

### Game Logic Tests
- All winning combinations (rock beats scissors, scissors beats paper, paper beats rock)
- Draw conditions (same moves)
- Score accumulation over multiple rounds
- Score string formatting

### AI Tests
- Basic AI follows predictable sequence (k, p, s, k, p, s, ...)
- Advanced AI records opponent moves
- Advanced AI develops counter-strategies
- Memory management when memory is full

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: pytest --cov=src --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v3
```

## Notes

- Tests use pytest fixtures for Flask test client setup
- Session-based tests ensure proper isolation
- Move validation is tested extensively to catch edge cases
- AI behavior is tested deterministically despite randomness
