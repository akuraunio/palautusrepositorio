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
    print_players_from_country(players, country)


def print_players_from_country(players, country):
    print(f"Players from {country}:")

    for player in players:
        if player.nationality == country:
            print(player)


if __name__ == "__main__":
    main()
