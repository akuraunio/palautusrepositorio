class PlayerStats:
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        for player in self._players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        players_by_nationality.sort(key=lambda player: player.points, reverse=True)

        return players_by_nationality
    