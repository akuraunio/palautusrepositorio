# Game Updated: First-to-5 Format

## Changes Made

The Kivi-Paperi-Sakset application has been modified to play games until one player reaches a score of 5 points, instead of ending on an invalid move.

## Modified Files

### 1. **src/web_app.py** - Game Logic

- Added `WIN_SCORE = 5` constant to `WebKiviPaperiSakset` class
- Added `winner` attribute to track who won the game ("player" or "computer")
- Removed game-ending condition for invalid moves
- Added game-ending condition when a player reaches 5 points
- Tracks whether "player" or "computer" won the game

**Key Changes:**

```python
# Before: Game ended on invalid move
if not self._onko_ok_siirto(player_move):
    self.game_over = True
    return None

# After: Game only ends at 5 points
if not self._onko_ok_siirto(player_move):
    return None  # Just return None, game continues

# New: Check for 5 points
if self.tuomari.ekan_pisteet >= self.WIN_SCORE:
    self.game_over = True
    self.winner = "player"
elif self.tuomari.tokan_pisteet >= self.WIN_SCORE:
    self.game_over = True
    self.winner = "computer"
```

### 2. **src/templates/play.html** - User Interface

- Updated instructions to say "Peli päättyy kun joku pelaaja saavuttaa 5 pistettä"
  (Game ends when a player reaches 5 points)
- Updated game-over message to show who won:
  - "🏆 Voitit pelin! Onnittelut! 🏆" (You won the game! Congratulations!)
  - "🤖 Vastustaja voitti pelin! Yritä uudelleen!" (Computer won the game! Try again!)

### 3. **src/tests/test_web_app.py** - Test Updates

- **TestMoveRoute.test_game_continues_until_5_points**: New test to verify game continues until 5 points
- **TestMoveRoute.test_invalid_move_does_not_end_game**: Changed to reflect invalid moves no longer end the game
- **TestWebKiviPaperiSakset.test_initialization**: Added `assert web_game.winner is None`
- **TestWebKiviPaperiSakset.test_invalid_move_returns_none**: Renamed and updated to reflect new behavior
- **TestWebKiviPaperiSakset.test_game_ends_at_5_points**: New test to verify game ends at 5 points
- **TestWebKiviPaperiSakset.test_game_ends_when_computer_reaches_5**: New test for computer reaching 5

## Game Flow

### Old Flow

1. Player and computer make moves
2. If invalid move → Game ends
3. Otherwise → Continue until invalid move

### New Flow

1. Player and computer make moves
2. Invalid moves are ignored (no effect)
3. Scores increment with each valid round
4. Game continues until someone reaches 5 points
5. Winner is displayed

## Features

✅ **Best-of-9 Format** - First player to 5 points wins
✅ **Invalid Moves Ignored** - Typos/mistakes don't end the game
✅ **Clear Winner Display** - Shows who won and congratulates/encourages
✅ **Continuous Play** - Can make as many moves as needed
✅ **Score Tracking** - Displays current score including draws

## Example Game

```
Round 1: Player (k) vs Computer (p) → Computer wins (0-1)
Round 2: Player (p) vs Computer (s) → Computer wins (0-2)
Round 3: Player (s) vs Computer (k) → Computer wins (0-3)
Round 4: Player (k) vs Computer (s) → Player wins (1-3)
Round 5: Player (p) vs Computer (k) → Player wins (2-3)
Round 6: Player (p) vs Computer (p) → Draw (2-3, Draws: 1)
Round 7: Player (s) vs Computer (p) → Player wins (3-3)
Round 8: Player (k) vs Computer (s) → Player wins (4-3)
Round 9: Player (p) vs Computer (k) → Player wins (5-3)
Game Over! Player reached 5 points and won!
```

## Testing

All tests have been updated to reflect the new game mechanics:

- 70+ test cases covering all aspects
- Tests verify game ends at exactly 5 points
- Tests verify invalid moves don't affect game
- Tests verify winner is correctly identified

Run tests with:

```bash
pytest
pytest -v
pytest --cov=src
```

## Documentation Updates

- **TESTING.md** - Updated to mention first-to-5 format
- **All test files** - Updated to test new behavior
- **Templates** - Updated UI text to reflect rule change

## Backward Compatibility

The changes are **not backward compatible** with the old "invalid move ends game" mechanic. This is an intentional redesign of the game rules.

## Files Affected

- ✅ src/web_app.py
- ✅ src/templates/play.html
- ✅ src/tests/test_web_app.py
- ✅ TESTING.md

## Summary

The game is now more player-friendly with a clear winning condition (first to 5 points) and invalid moves no longer end the game. Players can play continuously until someone reaches 5 points.
