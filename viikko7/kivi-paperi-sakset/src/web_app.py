from flask import Flask, render_template, request, session, redirect, url_for
from peli_tehdas import luo_peli
from tuomari import Tuomari
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Global game instances per session
games = {}


class WebKiviPaperiSakset:
    """Web adapter for the existing game logic"""

    WIN_SCORE = 5  # Game ends when a player reaches 5 points

    def __init__(self, game_instance):
        self.game = game_instance
        self.tuomari = Tuomari()
        self.game_over = False
        self.winner = None
        self.last_player_move = None
        self.last_computer_move = None
        self.last_result = None

    def make_move(self, player_move):
        """Process a single move and return the result"""
        if not self._onko_ok_siirto(player_move):
            return None

        self.last_player_move = player_move
        self.last_computer_move = self.game._tokan_siirto(player_move)

        if not self._onko_ok_siirto(self.last_computer_move):
            return None

        self.tuomari.kirjaa_siirto(self.last_player_move, self.last_computer_move)

        # Determine the result of this round
        if self.last_player_move == self.last_computer_move:
            self.last_result = "Tasapeli!"
        elif self._eka_voittaa(self.last_player_move, self.last_computer_move):
            self.last_result = "Voitit kierroksen!"
        else:
            self.last_result = "Hävisit kierroksen!"

        # Check if game is over (someone reached 5 points)
        if self.tuomari.ekan_pisteet >= self.WIN_SCORE:
            self.game_over = True
            self.winner = "player"
        elif self.tuomari.tokan_pisteet >= self.WIN_SCORE:
            self.game_over = True
            self.winner = "computer"

        return {
            "player_move": self.last_player_move,
            "computer_move": self.last_computer_move,
            "result": self.last_result,
            "score": str(self.tuomari),
        }

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _eka_voittaa(self, eka, toka):
        if eka == "k" and toka == "s":
            return True
        elif eka == "s" and toka == "p":
            return True
        elif eka == "p" and toka == "k":
            return True
        return False

    def get_score(self):
        return str(self.tuomari)


@app.route("/")
def index():
    """Main page with game mode selection"""
    session.clear()
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_game():
    """Start a new game with selected mode"""
    mode = request.form.get("mode")

    if mode not in ["a", "b", "c"]:
        return redirect(url_for("index"))

    # Create a new game instance
    game_instance = luo_peli(mode)

    if not game_instance:
        return redirect(url_for("index"))

    # Create session ID and store game
    session_id = secrets.token_hex(16)
    session["game_id"] = session_id
    session["mode"] = mode

    games[session_id] = WebKiviPaperiSakset(game_instance)

    return redirect(url_for("play"))


@app.route("/play")
def play():
    """Game play page"""
    game_id = session.get("game_id")

    if not game_id or game_id not in games:
        return redirect(url_for("index"))

    game = games[game_id]
    mode = session.get("mode", "a")

    mode_names = {
        "a": "Pelaaja vs Pelaaja",
        "b": "Pelaaja vs Tekoäly",
        "c": "Pelaaja vs Parannettu Tekoäly",
    }

    return render_template(
        "play.html",
        game=game,
        mode_name=mode_names.get(mode, "Tuntematon"),
        game_over=game.game_over,
    )


@app.route("/move", methods=["POST"])
def make_move():
    """Handle a player move"""
    game_id = session.get("game_id")

    if not game_id or game_id not in games:
        return redirect(url_for("index"))

    game = games[game_id]
    move = request.form.get("move")

    if move:
        game.make_move(move)

    return redirect(url_for("play"))


@app.route("/reset")
def reset():
    """Reset the game"""
    game_id = session.get("game_id")
    if game_id and game_id in games:
        del games[game_id]
    session.clear()
    return redirect(url_for("index"))


def run():
    """Start the Flask development server"""
    app.run(debug=True, port=5000)
