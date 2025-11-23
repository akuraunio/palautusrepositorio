class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def get_score(self):
        score_strings = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        score_difference = self.player1_score - self.player2_score

        def tie_score():
            if self.player1_score > 2:
                return "Deuce"
            else:
                return score_strings[self.player1_score] + "-All"

        def regulation_score():
            return (
                score_strings[self.player1_score]
                + "-"
                + score_strings[self.player2_score]
            )

        def overtime_score():
            if score_difference == -1:
                return "Advantage " + self.player2_name
            elif score_difference <= -2:
                return "Win for " + self.player2_name
            elif score_difference == 1:
                return "Advantage " + self.player1_name
            elif score_difference >= 2:
                return "Win for " + self.player1_name

        if score_difference == 0:
            return tie_score()
        elif self.player1_score > 3 or self.player2_score > 3:
            return overtime_score()
        else:
            return regulation_score()
