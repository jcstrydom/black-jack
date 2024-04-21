import math
import random
import os
import time
import sys
sys.path.append('./game_display')
import game_display.Display as dp
from Game import Game
from GameAssistant import GameAssistant



def main():
	"""
	DOCSTRING: this is the main program for the game
	"""

	os.system('cls')
	print('\n')
	game = Game()
	assistant = GameAssistant()
	game.newRound(isFirstRound=True)

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
		game.house.drawCard(game)
		
		os.system('cls')
		game.dealer.payWinners(game)
		assistant.printWinners(game)
		stopGame = input("\n\t Do you want to stop? [ Y / (N) ] ")
		game.exitGame = (stopGame[0].lower() in game.affirm_list if not(stopGame == '') else False)
		if not game.exitGame:
			game.newRound()
		if game.balanceCheck():
			break


	os.system('cls')
	
	print('\n\tThank you for playing. The final standing was:')
	assistant.printWinners(game)


if __name__=="__main__":
	main()