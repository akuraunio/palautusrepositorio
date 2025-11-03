import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaajan_etsiminen_nimella(self):
        self.assertAlmostEqual(self.stats.search("Kurri"), self.stats._players[2])
    
    def test_pelaajien_etsiminen_joukkueella(self):
        self.assertAlmostEqual(self.stats.team("EDM"), [self.stats._players[0], self.stats._players[2], self.stats._players[4]])
    
    def test_top_pelaajien_etsiminen(self):
        self.assertAlmostEqual(self.stats.top(1), [self.stats._players[4], self.stats._players[1]])

    def test_vaara_nimi_haku_palauttaa_None(self):
        self.assertAlmostEqual(self.stats.search("Stubb"), None)


    
