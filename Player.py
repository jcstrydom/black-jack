import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

import math
from gameUtils import GameAssistant

class Player():
	'''
	DOCSTRING: this class can be used for both computer and human players
	NOTE: all classes will have a list, and there is a pc indicator to say if it is an Computer or not
	'''
	# is_pc = False


	def __init__(self,name,balance=100,is_pc=False):
		'''
		DOCSTRING: this instantiates a player object with the player name
		'''

		self.assistant = GameAssistant()

		self.name = name
		self.is_pc = is_pc
		self.bust = False
		self.aces = 0
		# self.score = 0
		self.balance = balance
		self.cards = []
		self.hand = 0
		self.bet = 0
		self.winnings = []
		self.won = False


	def addCard(self,select):
		'''
		DOCSTRING: this adds a card
		'''
		self.cards.append(select)


	def getCards(self):
		'''
		DOCSTRING: this returns the cards
		'''
		return self.cards

	def getName(self):
		'''
		DOCSTRING: this returns the name of the player
		'''
		return self.name
	def drawCard(self,game):
		"""This is a method specifically for the PC player to draw a card"""
		if self.is_pc:
            # monotonousPrint(self,hse)
			betRatio = (1.5 + (self.hand-15)/15) # I am checking howfar from 15 is the first 2 cards
			if betRatio <=1:
				betRatio = 1
			self.bet = min(math.floor(game.initialBet*betRatio),self.balance)
			self.balance -= self.bet
            # print(str(self))
            # input('\n\tPress enter to continue')
			while self.hand <= 15:
				self.assistant.monotonousPrint(self,game.house)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides to hit\n')
				input('\n\tPress enter to continue')
				game.dealer.addCard(self)

			if not self.bust:
				self.assistant.monotonousPrint(self,game.house)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides stay\n')
				input('\n\tPress enter to continue')
			else:
				self.assistant.monotonousPrint(self,game.house)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and went bust\n')
				input('\n\tPress enter to continue')
		else:
			while self.score <= 16:
				os.system('cls')
				dp.display(game.house,True)
				print('\n\t'+self.name+' decides to hit\n')
				input('\n\tPress enter to continue')
				game.dealer.extraCard(self)
			if self.bust:
				os.system('cls')
				dp.display(game.house,True)
				print('\n\n\tThe house has gone bust! All players in the game has won!!!'.upper())
				input('\n\tPress enter to continue')
			else:
				os.system('cls')
				dp.display(game.house,True)
				print('\n\t\tThe house has a final score of '+str(self.hand))
				input('\n\tPress enter to continue')
				

    
	def __str__(self):
		"""
		DOCSTRING: this returns the players name only
		"""
		return_str = f"{self.name} [PC = {self.is_pc}]:\n Cards: {','.join(x for x in self.cards)}\n Score: {self.score}\n Balance: {self.balance}\n Last Bet: {self.bet}"
		return_str += f"\n Player winnings: {str(self.winnings)}\n Player bust: {self.bust}'\n Player won: {self.won}\n----------------\n"
		return  return_str
    

		





