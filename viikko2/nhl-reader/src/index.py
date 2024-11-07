import requests
from player import Player
from player_reader import PlayerReader, PlayerStats
from rich import print
from rich.text import Text
from rich.console import Console
from rich.table import Table

def get_season():
   console = Console()
   season = console.input("Select season [bold red][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/]: ")
   return str(season)

def get_nationality():
    console = Console()
    nationality = console.input("\nSelect nationality\n[bold red][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/]: ")
    return str(nationality)

def create_table(nationality, season, players):
    table_text = str("\nTop scorers of " + nationality + " season " + season)
    table = Table(title=table_text)

    table.add_column("name", style="cyan", no_wrap=True)
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console = Console()
    console.print(table)

def main():
        print("[italic]NHL statistics by nationality[/italic]\n")
        season = get_season()
        
        url = "https://studies.cs.helsinki.fi/nhlstats/" + season + "/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        while True:
            nationality = get_nationality()
            
            if nationality == "":
                break

            players = stats.top_scorers_by_nationality(nationality)
            create_table(nationality, season, players)


if __name__ == "__main__":
    main()
