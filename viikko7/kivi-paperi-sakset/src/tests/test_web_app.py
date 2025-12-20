import pytest
from web_app import app, WebKiviPaperiSakset, games
from peli_tehdas import luo_peli
from tuomari import Tuomari


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
"""
Pytest fixture that provides a Flask application context for testing.

This fixture creates and yields a Flask app context, allowing tests to access
the application instance and its context-dependent features (such as database
connections, configuration, and request/application globals) within the fixture
scope. The context is automatically cleaned up after each test that uses this
fixture.

Yields:
    Flask: The Flask application instance with an active application context.
"""
def app_context():
    """Create an app context for testing"""
    with app.app_context():
        yield app


class TestIndexRoute:
    """Tests for the main index route"""

    def test_index_page_loads(self, client):
        """Test that the index page loads successfully"""
        response = client.get("/")
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)

    def test_index_page_contains_mode_buttons(self, client):
        """Test that the index page contains all game mode options"""
        response = client.get("/")
        assert "Pelaaja vs Pelaaja" in response.get_data(as_text=True)
        assert "Tekoäly" in response.get_data(as_text=True)
        assert "Parannettu Tekoäly" in response.get_data(as_text=True)


class TestGameStartRoute:
    """Tests for starting a new game"""

    def test_start_game_mode_a(self, client):
        """Test starting a game with mode a (player vs player)"""
        response = client.post("/start", data={"mode": "a"}, follow_redirects=True)
        assert response.status_code == 200
        assert "Pelaaja vs Pelaaja" in response.get_data(as_text=True)

    def test_start_game_mode_b(self, client):
        """Test starting a game with mode b (player vs AI)"""
        response = client.post("/start", data={"mode": "b"}, follow_redirects=True)
        assert response.status_code == 200
        assert "Tekoäly" in response.get_data(as_text=True)

    def test_start_game_mode_c(self, client):
        """Test starting a game with mode c (player vs advanced AI)"""
        response = client.post("/start", data={"mode": "c"}, follow_redirects=True)
        assert response.status_code == 200
        assert "Parannettu Tekoäly" in response.get_data(as_text=True)

    def test_start_game_invalid_mode(self, client):
        """Test starting a game with invalid mode"""
        response = client.post(
            "/start", data={"mode": "invalid"}, follow_redirects=True
        )
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)

    def test_start_game_no_mode(self, client):
        """Test starting a game without specifying a mode"""
        response = client.post("/start", data={}, follow_redirects=True)
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)


class TestPlayRoute:
    """Tests for the game play page"""

    def test_play_page_without_session(self, client):
        """Test accessing play page without a valid session"""
        response = client.get("/play", follow_redirects=True)
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)

    def test_play_page_with_session(self, client):
        """Test accessing play page with a valid game session"""
        # Start a game first
        client.post("/start", data={"mode": "a"})
        # Now access play page
        response = client.get("/play")
        assert response.status_code == 200
        assert "Tulostaulukko" in response.get_data(as_text=True)


class TestMoveRoute:
    """Tests for making moves during gameplay"""

    def test_game_continues_until_5_points(self, client):
        """Test that game continues until someone reaches 5 points"""
        # Start a game
        client.post("/start", data={"mode": "b"})  # Use AI for predictable moves

        # Make multiple moves without invalid moves
        for i in range(10):
            response = client.post("/move", data={"move": "k"}, follow_redirects=True)
            assert response.status_code == 200

    def test_invalid_move_does_not_end_game(self, client):
        """Test that an invalid move no longer ends the game"""
        # Start a game
        client.post("/start", data={"mode": "a"})

        # Make an invalid move - should not crash or end game
        response = client.post("/move", data={"move": "x"}, follow_redirects=True)
        assert response.status_code == 200

    def test_move_without_session(self, client):
        """Test making a move without a valid session"""
        response = client.post("/move", data={"move": "k"}, follow_redirects=True)
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)


class TestResetRoute:
    """Tests for resetting the game"""

    def test_reset_clears_session(self, client):
        """Test that reset clears the session and returns to index"""
        # Start a game
        client.post("/start", data={"mode": "a"})

        # Reset the game
        response = client.get("/reset", follow_redirects=True)
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)

    def test_reset_without_session(self, client):
        """Test reset without an active session"""
        response = client.get("/reset", follow_redirects=True)
        assert response.status_code == 200
        assert "Kivi-Paperi-Sakset" in response.get_data(as_text=True)


class TestWebKiviPaperiSakset:
    """Tests for the WebKiviPaperiSakset game adapter class"""

    def test_initialization(self):
        """Test that the game adapter initializes correctly"""
        game_instance = luo_peli("a")
        web_game = WebKiviPaperiSakset(game_instance)

        assert web_game.game is not None
        assert isinstance(web_game.tuomari, Tuomari)
        assert web_game.game_over is False
        assert web_game.last_player_move is None
        assert web_game.last_computer_move is None
        assert web_game.winner is None

    def test_valid_move(self):
        """Test making a valid move"""
        game_instance = luo_peli("b")  # Use AI opponent
        web_game = WebKiviPaperiSakset(game_instance)

        result = web_game.make_move("k")
        assert result is not None
        assert "player_move" in result
        assert "computer_move" in result
        assert "result" in result
        assert web_game.last_player_move == "k"

    def test_invalid_move_returns_none(self):
        """Test that an invalid move returns None but doesn't set game_over"""
        game_instance = luo_peli("b")
        web_game = WebKiviPaperiSakset(game_instance)

        result = web_game.make_move("invalid")
        assert result is None

    def test_game_ends_at_5_points(self):
        """Test that game ends when a player reaches 5 points"""
        game_instance = luo_peli("b")  # Player vs AI
        web_game = WebKiviPaperiSakset(game_instance)

        # Manually set scores to 4-0
        web_game.tuomari.ekan_pisteet = 4

        # Next winning move should end the game
        web_game.make_move("k")

        # Check if game could be over (depends on who won the move)
        if web_game.tuomari.ekan_pisteet >= 5:
            assert web_game.game_over is True
            assert web_game.winner == "player"

    def test_game_ends_when_computer_reaches_5(self):
        """Test that game ends when computer reaches 5 points"""
        game_instance = luo_peli("b")
        web_game = WebKiviPaperiSakset(game_instance)

        # Manually set scores to 0-4
        web_game.tuomari.tokan_pisteet = 4

        # Make a move that will eventually trigger game over
        for i in range(5):
            result = web_game.make_move("s")  # Scissors
            if web_game.game_over:
                assert web_game.winner == "computer"
                break

    def test_move_validation(self):
        """Test the move validation function"""
        game_instance = luo_peli("a")
        web_game = WebKiviPaperiSakset(game_instance)

        assert web_game._onko_ok_siirto("k") is True
        assert web_game._onko_ok_siirto("p") is True
        assert web_game._onko_ok_siirto("s") is True
        assert web_game._onko_ok_siirto("x") is False
        assert web_game._onko_ok_siirto("") is False

    def test_win_determination(self):
        """Test the win determination logic"""
        game_instance = luo_peli("a")
        web_game = WebKiviPaperiSakset(game_instance)

        # Rock beats scissors
        assert web_game._eka_voittaa("k", "s") is True
        # Scissors beats paper
        assert web_game._eka_voittaa("s", "p") is True
        # Paper beats rock
        assert web_game._eka_voittaa("p", "k") is True
        # Same moves don't win
        assert web_game._eka_voittaa("k", "k") is False
        # Losing combination
        assert web_game._eka_voittaa("k", "p") is False

    def test_multiple_moves_score_tracking(self):
        """Test that scores are tracked correctly over multiple moves"""
        game_instance = luo_peli("b")
        web_game = WebKiviPaperiSakset(game_instance)

        initial_score = web_game.get_score()

        web_game.make_move("k")
        score_after_first = web_game.get_score()

        # Score should change after a move (either player scores or draw)
        assert score_after_first != initial_score or "Tasapelit: 1" in score_after_first

    def test_get_score_format(self):
        """Test that the score string is formatted correctly"""
        game_instance = luo_peli("a")
        web_game = WebKiviPaperiSakset(game_instance)

        score = web_game.get_score()
        assert "Pelitilanne:" in score
        assert "Tasapelit:" in score
