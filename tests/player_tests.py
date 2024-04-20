import unittest, sys
sys.path.append('./../')
from Dealer import Dealer
from Player import Player

class TestCalculatePlayerScore(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()
        self.player = Player("Test Player")

    def test_no_aces(self):
        self.player.cards = ["Spade 2", "Heart 3"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 5)
        self.assertEqual(self.player.aces, 0)

    def test_one_ace(self):
        self.player.cards = ["Spade A", "Heart 3"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 16)
        self.assertEqual(self.player.aces, 1)

    def test_multiple_aces(self):
        self.player.cards = ["Spade A", "Heart A", "Diamond A"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 30)
        self.assertEqual(self.player.aces, 3)

    def test_hand_less_than_21(self):
        self.player.cards = ["Spade 10", "Heart 5"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 15)
        self.assertEqual(self.player.aces, 0)

    def test_hand_equal_to_21(self):
        self.player.cards = ["Spade A", "Heart 10"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 21)
        self.assertEqual(self.player.aces, 1)

    def test_hand_greater_than_21(self):
        self.player.cards = ["Spade A", "Heart 10", "Diamond 6"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 27)
        self.assertEqual(self.player.aces, 1)
        self.assertFalse(self.player.bust)

if __name__ == '__main__':
    unittest.main()