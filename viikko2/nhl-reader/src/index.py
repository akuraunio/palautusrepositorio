import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    
    country = "FIN"
    print_players_from_country_sorted_by_points(players, country)


def print_players_from_country_sorted_by_points(players, country):
    print(f"Players from {country}:\n")
    players.sort(key=lambda player: player.points, reverse=True)

    for player in players:
        if player.nationality == country:
            print(player)


if __name__ == "__main__":
    main()
