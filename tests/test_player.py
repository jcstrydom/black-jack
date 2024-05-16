import unittest, sys
sys.path.append('./../')
from core.Game import Game

import unittest
from unittest.mock import patch, Mock
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
        self.game = Game(isTesting=True)


    def test_newRound(self):
        """
        Test the `newRound` method of the `Player` class.

        This test checks if the `newRound` method correctly resets the player's attributes to their initial state.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        cards = ["Diamond 10","Spade 2","Spade A","Club 10","Heart K","Club Q"]
        bets = [100,50]
        self.game.players[0].cards = cards[:3]; self.game.players[1].cards = cards[3:]
        for i,p in enumerate(self.game.players):
            self.game.dealer.calculatePlayerHand(p)
            p.bet = bets[i]
            p.won = bool(0 ** i)
            # print(p)
        
        for p in self.game.players:
            p.newRound()
            self.assertEqual(p.bet,0)
            self.assertEqual(p.bust,False)
            self.assertEqual(p.cards,[])
            self.assertEqual(p.hand,0)
            self.assertEqual(p.aces,0)

    def test_addCard_and_getCards(self):
        """
        Test the `addCard` method of the `Player` class.

        This test checks if the `addCard` method correctly adds a card to the player's hand.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        init_cards = self.game.players[0].getCards()
        add_card = "Diamond 10"
        result = [*init_cards,add_card]
        self.game.players[0].addCard(add_card)
        self.assertEqual(self.game.players[0].cards,result)


    def test_determineBet_isPC(self):
        """
        Test the `determineBet` method of the `Player` class.

        This test checks if the `determineBet` method correctly sets the player's bet to the appropriate amount if the player is a PC.

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        ## player below 8 (i.e. betRatio < 1.0)
        self.game.dealer.pot = 100
        self.game.initialBet = 50
        self.game.players[1].hand = 5
        self.game.players[1].is_pc = True
        self.game.players[1].balance = 100

        self.game.players[1].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[1].bet,50)
        self.assertEqual(self.game.players[1].balance,50)
        self.assertEqual(self.game.dealer.pot,150)

        ## player between 8 and 15 (i.e. 1.0 < betRatio < 1.5)
        self.game.dealer.pot = 100
        self.game.initialBet = 50
        self.game.players[0].hand = 12
        self.game.players[0].is_pc = True
        self.game.players[0].balance = 100

        self.game.players[0].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[0].bet,65)
        self.assertEqual(self.game.players[0].balance,35)
        self.assertEqual(self.game.dealer.pot,165)

        ## player greater than 15 (i.e. betRatio > 1.5)
        self.game.dealer.pot = 100
        self.game.initialBet = 50
        self.game.players[0].hand = 18
        self.game.players[0].is_pc = True
        self.game.players[0].balance = 100

        self.game.players[0].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[0].bet,85)
        self.assertEqual(self.game.players[0].balance,15)
        self.assertEqual(self.game.dealer.pot,185)

        
    
    @patch('builtins.input', side_effect=['0', '50', '50', '75', '10'])
    def test_determineBet_not_isPC(self, mock_input):
        """
        Test the `determineBet` method of the `Player` class.

        This test checks if the `determineBet` method correctly sets the player's bet to the appropriate amount if the player is not a PC.

        Parameters:
        - self: The instance of the test case.
        - mock_input: A mock input object that will be used to simulate user inputs.

        Returns:
        - None
        """
        ## player below 8 (i.e. betRatio < 1.0)
        self.game.dealer.pot = 100
        self.game.initialBet = 50
        self.game.players[1].hand = 5
        self.game.players[1].is_pc = False
        self.game.players[1].balance = 100

        self.game.players[1].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[1].bet, 50)
        self.assertEqual(self.game.players[1].balance, 50)
        self.assertEqual(self.game.dealer.pot, 150)

        ## player between 8 and 15 (i.e. 1.0 < betRatio < 1.5)
        self.game.dealer.pot = 100
        self.game.initialBet = 75
        self.game.players[0].hand = 12
        self.game.players[0].is_pc = False
        self.game.players[0].balance = 100

        self.game.players[0].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[0].bet, 75)
        self.assertEqual(self.game.players[0].balance, 25)
        self.assertEqual(self.game.dealer.pot, 175)

        ## player greater than 15 (i.e. betRatio > 1.5)
        self.game.dealer.pot = 100
        self.game.initialBet = 75
        self.game.players[0].hand = 18
        self.game.players[0].is_pc = False
        self.game.players[0].balance = 10

        self.game.players[0].determineBet(self.game,isTesting=True)
        self.assertEqual(self.game.players[0].bet,10)
        self.assertEqual(self.game.players[0].balance, 0)
        self.assertEqual(self.game.dealer.pot, 110)

    
    def test_houseHitStay(self):
        """
        Test the `houseHitStay` method of the `House` class.
        
        This test checks the behavior of the `houseHitStay` method in various scenarios.
        
        Parameters:
        - self: The instance of the test case.
        
        Returns:
        - None
        """

        cards = ["Di 10","Sp 2","Sp A","Cl 10","Hr K","Cl Q"]
        # Test case where player's hand is less than or equal to 16
        self.game.house.cards = cards[:2]
        self.game.dealer.calculatePlayerHand(self.game.house)
        # print(f"{self.game.house.cards=} [{self.game.house.hand=}]")
        
        self.game.house.houseHitStay(self.game,isTesting=True)
        self.assertGreater(self.game.house.hand,16)
        

        # Test case where player's hand is greater than 16 and the house has bust
        self.game.house.cards = cards[2:4]
        self.game.dealer.calculatePlayerHand(self.game.house)
        print(f"{self.game.house.cards=} [{self.game.house.hand=}]")
        
        self.game.house.houseHitStay(self.game,isTesting=True)
        self.assertGreater(self.game.house.hand,16)
        self.assertEqual(self.game.house.bust,False)

        self.game.house.cards = cards[3:]
        self.game.dealer.calculatePlayerHand(self.game.house)
        # print(f"{self.game.house.cards=} [{self.game.house.hand=}]")
        
        self.game.house.houseHitStay(self.game,isTesting=True)
        self.assertGreater(self.game.house.hand,16)
        self.assertEqual(self.game.house.bust,True)


    def test_hitStayExit_isPC(self):
        """
        Test the `hitStayExit_isPC` method for specific player hand scenarios.
        
        This test method sets up player's hand scenarios using predetermined cards and checks the behavior 
        when the hand value is less than or equal to 16, greater than 16, and when the house has bust.
        
        Parameters:
        - self: The instance of the test case.
        
        Returns:
        - None
        """
        cards = ["Di 10","Sp 2","Sp A","Cl 10","Hr K","Cl Q"]
        self.game.players[0].is_pc = True
        player = self.game.players[0]
        # Test case where player's hand is less than or equal to 15
        player.cards = cards[:2]
        self.game.dealer.calculatePlayerHand(player)
        print(f"{player.name=}: {player.cards=} [{player.hand=}]")
        
        player.hitStayExit(self.game,isTesting=True)
        self.assertGreater(player.hand,15)
        

        # Test case where player's hand is greater than 15 and the house has bust
        player.cards = cards[2:4]
        self.game.dealer.calculatePlayerHand(player)
        print(f"{player.name=}: {player.cards=} [{player.hand=}]")
        
        player.hitStayExit(self.game,isTesting=True)
        self.assertGreater(player.hand,16)
        self.assertEqual(player.bust,False)

        player.cards = cards[3:]
        self.game.dealer.calculatePlayerHand(player)
        print(f"{player.name=}: {player.cards=} [{player.hand=}]")
        
        player.hitStayExit(self.game,isTesting=True)
        self.assertGreater(player.hand,16)
        self.assertEqual(player.bust,True)
        


if __name__ == '__main__':
    unittest.main()
