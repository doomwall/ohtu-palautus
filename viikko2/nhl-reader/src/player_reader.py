import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)


class PlayerStats:
    def __init__(self, players) -> None:
        self.players = sorted(players.players, key=lambda player: player.points, reverse=True)

    def top_scorers_by_nationality(self, nationality):
        sortednationality = [player for player in self.players if player.nationality == nationality]
        return sortednationality