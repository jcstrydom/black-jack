import unittest
from core.Game import Game
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
        self.game = Game(isTesting=True)


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
        self.game.players[0].cards = cards[:2]; self.game.players[1].cards = cards[2:]
        for hand,player in zip(hands,self.game.players):
            self.game.dealer.calculatePlayerScore(player)
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
        self.game.players[0].cards = cards[:2]; self.game.players[1].cards = cards[2:]
        for hand,player in zip(hands,self.game.players):
            self.game.dealer.calculatePlayerScore(player)
            self.assertEqual(player.hand, hand[0])
            self.assertEqual(player.aces, hand[1])
            self.assertFalse(player.bust)


    def test_calculatePlayerScore_multiple_aces(self):
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
        self.game.players[0].cards = cards[:3]; self.game.players[1].cards = cards[3:]
        for hand,player in zip(hands,self.game.players):
            self.game.dealer.calculatePlayerScore(player)
            self.assertEqual(player.hand, hand[0])
            self.assertEqual(player.aces, hand[1])
            self.assertFalse(player.bust)


    def test_calculatePlayerScore_hand_equal_to_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is equal to 21.

        This test sets up a player1 with two cards, "Spade A" and "Heart 10", and calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 21 and the `aces` attribute is equal to 1.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.game.players[0].cards = ["Spade A", "Heart 10"]
        self.game.dealer.calculatePlayerScore(self.game.players[0])
        self.assertEqual(self.game.players[0].hand, 21)
        self.assertEqual(self.game.players[0].aces, 1)
        self.assertFalse(self.game.players[1].bust)

    def test_calculatePlayerScore_hand_greater_than_21(self):
        """
        Test the behavior of the `calculatePlayerScore` method when the player's hand is greater than 21.

        This test sets up a player with three cards, "Club A", "Heart A", "Heart 10", "Diamond 6", "Spade A", and "Heart 4", then calls the `calculatePlayerScore` method of the `dealer` object.
        It then asserts that the `hand` attribute of the player is equal to 23, the `aces` attribute is equal to 3, and the `bust` attribute is True.

        Parameters:
            self (TestCalculatePlayerScore): The current instance of the test case.

        Returns:
            None
        """
        self.game.players[1].cards = ["Club A", "Heart A", "Heart 10", "Diamond 6", "Spade A", "Heart 4"]
        self.game.dealer.calculatePlayerScore(self.game.players[1])
        self.assertEqual(self.game.players[1].hand, 23)
        self.assertEqual(self.game.players[1].aces, 3)
        self.assertTrue(self.game.players[1].bust)

    def test_newRound(self):
        """
        Test the behavior of the `newRound` method.
        
        The default values of the `newRound` method are:
        - deck: shuffled
        - pot: 0
        
        Parameters:
            self (TestNewRound): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.newRound()
        self.assertNotEqual(self.game.dealer.deck.pack[0], "Cl A")
        self.assertEqual(self.game.dealer.pot, 0)

    def test_dealCards(self):
        """
        Test the behavior of the `dealCards` method.
        
        The default values of the `dealCards` method are:
        - all(len(player.cards) == 2 for player in self.players) shuffled
        
        Parameters:
            self (TestDealCards): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.dealCards(self.game.players)
        self.assertEqual(len(self.game.players[0].cards), 2)
        self.assertEqual(len(self.game.players[1].cards), 2)

    def test_addCards(self):
        """
        Test the behavior of the `addCards` method.

        Parameters:
            self (TestAddCards): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.calculatePlayerScore(self.game.players[0])
        init_deck_size = len(self.game.dealer.deck.pack)
        first_card = self.game.dealer.deck.pack[0]
        init_hand = self.game.players[0].hand

        self.game.dealer.addCard(self.game.players[0])

        self.assertEqual(len(self.game.dealer.deck.pack), init_deck_size - 1)
        self.assertEqual(self.game.players[0].cards[-1], first_card)
        self.assertGreater(self.game.players[0].hand, init_hand)

    def test_payWinners_house_bust(self):
        """
        Test the behavior of the `payWinners` method, when the house goes bust while the players don't.

        Parameters:
            self (TestPayWinners): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.pot = 200; self.game.roundNumber = 0
        cards = ["Spade 2", "Heart 3","Diamond K","Club J"]
        self.game.house.cards = ["Club A", "Heart A", "Heart 10", "Diamond 6", "Spade A", "Heart 4"]
        
        self.game.players[0].cards = cards[:2]; self.game.players[1].cards = cards[2:]
        for player in [*self.game.players, self.game.house]:
            self.game.dealer.calculatePlayerScore(player)

        self.game.dealer.payWinners(self.game)

        self.assertEqual(self.game.winners[0], ["TestPlayer1", "TestPlayer2"])
        share = [100,100,0]
        for win,player in zip(share,[*self.game.players, self.game.house]):
            # print(f"{self.game.winners[0]}")
            if player.name in self.game.winners[0]:
                self.assertTrue(player.won)
                # print(f"{player.name} --> {player.winnings}")
                self.assertEqual(player.winnings[0],win)

    def test_payWinners_house_21(self):
        """
        Test the behavior of the `payWinners` method, when the house has 21 while TestPlayer2 also has 21.

        Parameters:
            self (TestPayWinners): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.pot = 200; self.game.roundNumber = 0
        cards = ["Spade 2", "Heart 3","Diamond K","Club J"]
        self.game.house.cards = ["Club K", "Heart A"]
        
        self.game.players[0].cards = cards[:2]; self.game.players[1].cards = cards[2:]
        for player in [*self.game.players, self.game.house]:
            self.game.dealer.calculatePlayerScore(player)

        self.game.dealer.payWinners(self.game)
        self.assertEqual(self.game.winners[0], ["House"])
        share = [0,0,200]
        for win,player in zip(share,[*self.game.players, self.game.house]):
            if player.name in self.game.winners[0]:
                self.assertTrue(player.won)
                # print(f"{player.name} --> {player.winnings}")
                self.assertEqual(player.winnings[0],win)

    def test_payWinners_house_20(self):
        """
        Test the behavior of the `payWinners` method, when the house has 21 while TestPlayer2 also has 21.

        Parameters:
            self (TestPayWinners): The current instance of the test case.

        Returns:
            None
        """
        self.game.dealer.pot = 200; self.game.roundNumber = 0
        cards = ["Spade 2", "Heart 3","Diamond K","Club A"]
        self.game.house.cards = ["Club K", "Heart J"]
        
        self.game.players[0].cards = cards[:2]; self.game.players[1].cards = cards[2:]
        for player in [*self.game.players, self.game.house]:
            self.game.dealer.calculatePlayerScore(player)

        self.game.dealer.payWinners(self.game)
        self.assertEqual(self.game.winners[0], ["TestPlayer2"])
        share = [0,200,0]
        for win,player in zip(share,[*self.game.players, self.game.house]):
            if player.name in self.game.winners[0]:
                self.assertTrue(player.won)
                # print(f"{player.name} --> {player.winnings}")
                self.assertEqual(player.winnings[0],win)