import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.team, "EDM")

    def test_nonfound_search(self):
        player = self.stats.search("Virtanen")

        self.assertEqual(player, None)

    def test_team(self):
        list_of_players = self.stats.team("EDM")

        self.assertEqual(list_of_players[0].name, "Semenko")

    def test_top(self):
        list_of_players = self.stats.top(3)

        self.assertEqual(list_of_players[0].name, "Gretzky")

    def test_top_goals(self):
        list_of_players_goals = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(list_of_players_goals[0].name, "Lemieux")
        

    def test_top_assists(self):
        list_of_players_assists = self.stats.top(3, SortBy.ASSISTS)
        
        self.assertEqual(list_of_players_assists[0].name, "Gretzky")