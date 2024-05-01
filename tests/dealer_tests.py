import unittest
from unittest.mock import Mock
from core.Dealer import Dealer
from core.Player import Player

class TestDealer(unittest.TestCase):

    def setUp(self):
        """
        Set up the initial state for the test case.

        This function initializes the `dealer` and a list of two `player` objects for the test case.
        The `dealer` object is an instance of the `Dealer` class, and the two `player` objects are of instance `Player` with names "TestPlayer1" and "TestPlayer2".


        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.dealer = Dealer()
        player1 = Player('TestPlayer1'); player2 = Player('TestPlayer2')
        self.players = [player1,player2]


    def test_calculatePlayerScore_no_aces(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has no aces in their hand.

        This test sets up a player1 with two cards, "Spade 2", "Heart 3", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 5 and the `aces` attribute is equal to 0.

        This test sets up a player2 with two cards, "Diamond K", "Club J", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 20 and the `aces` attribute is equal to 0.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        cards = ["Spade 2", "Heart 3","Diamond K","Club J"]
        hands = [(5,0),(20,0)]
        self.players[0].cards = cards[:2]; self.players[1].cards = cards[2:]
        for hand,player in zip(hands,self.players):
            self.dealer.calculatePlayerScore(player)
            self.assertEqual(player.hand, hand[0])
            self.assertEqual(player.aces, hand[1])
            self.assertFalse(player.bust)

    def test_calculatePlayerScore_one_ace(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has one aces in their hand.

        This test sets up a player with three ace cards, "Spade A", "Heart 3", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 16 and the `aces` attribute is equal to 1.

        This test sets up a player with three ace cards, "Diamond K", "Club A", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 21 and the `aces` attribute is equal to 1.

        Parameters:
            self: The current instance of the test case.

        Returns:
            None
        """
        cards = ["Spade A", "Heart 3","Diamond K","Club A"]
        hands = [(14,1),(21,1)]
        self.players[0].cards = cards[:2]; self.players[1].cards = cards[2:]
        for hand,player in zip(hands,self.players):
            self.dealer.calculatePlayerScore(player)
            self.assertEqual(player.hand, hand[0])
            self.assertEqual(player.aces, hand[1])
            self.assertFalse(player.bust)


    def test_multiple_aces(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has multiple aces in their hand.

        This test sets up a player1 with three ace cards, "Spade A", "Heart A", and "Diamond A", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 13 and the `aces` attribute is equal to 3.

        This test sets up a player2 with three ace cards, "Spade A", "Heart K", and "Diamond A", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 12 and the `aces` attribute is equal to 2.

        Parameters:
            self: The current instance of the test case.

        Returns:
            None
        """
        cards = ["Spade A", "Heart A", "Diamond A", "Spade A", "Heart K", "Diamond A"]
        hands = [(13,3),(12,2)]
        self.players[0].cards = cards[:3]; self.players[1].cards = cards[3:]
        for hand,player in zip(hands,self.players):
            self.dealer.calculatePlayerScore(player)
            self.assertEqual(player.hand, hand[0])
            self.assertEqual(player.aces, hand[1])
            self.assertFalse(player.bust)


    def test_hand_equal_to_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is equal to 21.

        This test sets up a player1 with two cards, "Spade A" and "Heart 10", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 21 and the `aces` attribute is equal to 1.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.players[0].cards = ["Spade A", "Heart 10"]
        self.dealer.calculatePlayerScore(self.players[0])
        self.assertEqual(self.players[0].hand, 21)
        self.assertEqual(self.players[0].aces, 1)
        self.assertFalse(self.players[1].bust)

    def test_hand_greater_than_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is greater than 21.

        This test sets up a player with three cards, "Club A", "Heart A", "Heart 10", "Diamond 6", "Spade A", and "Heart 4", then calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 23, the `aces` attribute is equal to 3, and the `bust` attribute is True.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.players[1].cards = ["Club A", "Heart A", "Heart 10", "Diamond 6", "Spade A", "Heart 4"]
        self.dealer.calculatePlayerScore(self.players[1])
        self.assertEqual(self.players[1].hand, 23)
        self.assertEqual(self.players[1].aces, 3)
        self.assertTrue(self.players[1].bust)
