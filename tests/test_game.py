import unittest
from core.Game import Game

class TestGame(unittest.TestCase):

    def test_newRound_increases_initialBet_on_even_roundNumbers(self):
        game = Game(isTesting=True)
        game.players[0].balance = 100
        game.players[1].balance = 100
        game.roundNumber = 2
        game.house.balance = 100

        game.newRound(isFirstRound=False)

        self.assertEqual(game.initialBet, 75)
        self.assertEqual(game.roundNumber, 3)
        self.assertEqual(len(game.house.cards), 2)
        for player in game.players:
            self.assertEqual(len(player.cards), 2)
            self.assertEqual(player.bet, 0)
            self.assertEqual(player.bust, False)

    def test_newRound_resets_game_state(self):
        game = Game(isTesting=True)
        game.players[0].balance = 0
        game.players[1].balance = 100
        game.roundNumber = 0

        game.newRound(isFirstRound=True)

        self.assertEqual(game.initialBet, 50)
        self.assertEqual(game.roundNumber, 0)
        self.assertEqual(len(game.house.cards), 2)
        for player in game.players:
            self.assertEqual(len(player.cards), 2)
            self.assertEqual(player.bet, 0)
            self.assertEqual(player.bust, False)

    def test_balanceCheck_identifies_zero_balance(self):
        game = Game(isTesting=True)
        game.players[0].balance = 0
        game.players[1].balance = 100
        game.house.balance = -50

        result = game.balanceCheck(isTesting=True)

        self.assertTrue(result)

    def test_balanceCheck_does_not_identify_zero_balance(self):
        game = Game(isTesting=True)
        game.players[0].balance = 100
        game.players[1].balance = 50
        game.house.balance = 0

        result = game.balanceCheck()

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()