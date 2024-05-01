import unittest, sys
sys.path.append('./../')
from core.Dealer import Dealer
from core.Player import Player

class TestCalculatePlayerScore(unittest.TestCase):

    def setUp(self):
        """
        Set up the initial state for the test case.

        This function initializes the `dealer` and `player` objects for the test case.
        The `dealer` object is an instance of the `Dealer` class, and the `player` object is an instance of the `Player` class with the name "Test Player".

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.dealer = Dealer()
        self.player = Player("Test Player")

    def test_no_aces(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has no aces in their hand.

        This test sets up a player with two cards, "Spade 2" and "Heart 3", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 5 and the `aces` attribute is equal to 0.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade 2", "Heart 3"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 5)
        self.assertEqual(self.player.aces, 0)

    def test_one_ace(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has one aces in their hand.

        This test sets up a player with three ace cards, "Spade A", "Heart 3", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 16 and the `aces` attribute is equal to 1.

        Parameters:
            self: The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade A", "Heart 3"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 16)
        self.assertEqual(self.player.aces, 1)

    def test_multiple_aces(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player has multiple aces in their hand.

        This test sets up a player with three ace cards, "Spade A", "Heart A", and "Diamond A", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 30 and the `aces` attribute is equal to 3.

        Parameters:
            self: The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade A", "Heart A", "Diamond A"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 30)
        self.assertEqual(self.player.aces, 3)

    def test_hand_less_than_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is less than 21.

        This test sets up a player with two cards, "Spade 10" and "Heart 5", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 15 and the `aces` attribute is equal to 0.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade 10", "Heart 5"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 15)
        self.assertEqual(self.player.aces, 0)

    def test_hand_equal_to_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is equal to 21.

        This test sets up a player with two cards, "Spade A" and "Heart 10", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 21 and the `aces` attribute is equal to 1.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade A", "Heart 10"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 21)
        self.assertEqual(self.player.aces, 1)

    def test_hand_greater_than_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is greater than 21.

        This test sets up a player with three cards, "Spade A", "Heart 10", and "Diamond 6", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 27, the `aces` attribute is equal to 1, and the `bust` attribute is False.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.player.cards = ["Spade A", "Heart 10", "Diamond 6"]
        self.dealer.calculatePlayerScore(self.player)
        self.assertEqual(self.player.hand, 27)
        self.assertEqual(self.player.aces, 1)
        self.assertFalse(self.player.bust)

if __name__ == '__main__':
    unittest.main()