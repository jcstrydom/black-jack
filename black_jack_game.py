import math
import random
import os
import time
import sys
sys.path.append('./game_display')
import game_display.Display as dp
from Game import Game



def main():
	"""
	DOCSTRING: this is the main program for the game
	"""
	os.system('cls')
	print('\n')
	game = Game()
	game.dealer.dealCards(game.players + [game.house])


	while not game.exitGame:
		if game.roundNumber != 0 and game.roundNumber % 2 == 0:
			game.initialBet += 25
		for player in game.players:
			if not player.is_pc:
				player.playersChoice(game)
				if game.exitGame:
					break
			else:
				player.drawCard(game)
		if not game.exitGame:
			game.roundNumber += 1
			os.system('cls')
			game.dealer.payWinners(game.players + [game.house])
			game.exitGame = game.balanceCheck()
			if game.exitGame:
				break
			corInp = False
			while not corInp:
				continueGame = input('\n\n\t\tDo you want to continue? [Y/N]')
				if continueGame[0].lower() in ('y','j'):
					break
				elif continueGame[0].lower() == 'n':
					game.exitGame = True
					break
				else:
					print('You did not give a valid answer. Please try again...')
					
			if not game.exitGame:
				os.system('cls')
				game.dealer.dealCards(game.players + [game.house])
	os.system('cls')
	if game.balanceCheck():
		lowBalPlayers = [p for p in game.players if p.balance == 0]
		print('The following player(s) have zero balances that caused the game to exit: '+','.join(x for x in lowBalPlayers)+'\n')
		print('\n\tThe final standing was:')
	else:
		print('\n\tThank you for playing. The final standing was:')
	game.dealer.payWinners(game.players + [game.house])


if __name__=="__main__":
	main()