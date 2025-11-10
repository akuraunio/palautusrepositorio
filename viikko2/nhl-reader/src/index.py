from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
import requests
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    season = console.input("Season [magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/] ")
    nationality = console.input("Nationality [magenta][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/]")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", style="blue")
    table.add_column("teams", style="purple")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")

    for player in players:
        table.add_row(str(player.name), str(player.team), str(player.goals), str(player.assists), str(player.points))

    console.print(table)


if __name__ == "__main__":
    main()
