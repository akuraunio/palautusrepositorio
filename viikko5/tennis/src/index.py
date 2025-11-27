from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_score())

    def play_round(winner):
        game.won_point(winner)
        print(game.get_score())

    round_winners = ["player1", "player1", "player1", "player1"]
    for winner in round_winners:
        play_round(winner)


if __name__ == "__main__":
    main()
