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

		## This is the logic for the PC player
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

		## This is the logic for the HOUSE player
		## THIS MAY BE NEEDED TO PUT IN SEPARATE METHOD
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

	def makeABet(self,game):
		while True:
			try:
				bet = int(input(f"\n\t {self.name}, what's your bet? (min: {0}, remaining balance: {1}) "
            		.format(game.initbet, self.balance)))
				if game.initbet <= bet <= self.balance:
					self.balance -= bet
					self.bet = bet
			except ValueError:
				print("Invalid input, please try again...")

	
	def playersBet(self, minimum_bet):
		"""Prompt player for bet, ensure it's a valid integer between minimum and balance"""
		while True:
			try:
				bet = int(input(f"\n\t {self.name}, what's your bet? (min: {minimum_bet}, balance: {self.balance}) "))
				if minimum_bet <= bet <= self.balance:
					self.balance -= bet
					return bet
				raise ValueError
			except ValueError:
				print("\n\t Please enter a valid integer between the minimum and your balance.")


	def playersAction(self,game):
		# correctInput = False
		# while not correctInput:
		instrct = input('\tWhat do you want to do?\n\t[H] Hit (draw another card)\n\t[S] Stand (no action)\n\t[E] Exit the game\n\t\t')[0].lower()
		if len(instrct) > 0:
			if instrct[0].lower() == 'h':
				game.dealer.addCard(self)
				return False
			elif instrct[0].lower() == 's':
				print(f"\n\t\t Your current score is {self.hand} with a bet of {self.bet}")
				input('\n\t Press enter to continue')
				return True
			elif instrct[0].lower() == 'e':
				game.exitGame = True
				return True
			else:
				print('You did not give a valid answer. Please try again...')
		else:
			pass


	def playersChoice(self,game):
		moveOn = False
		self.assistant.monotonousPrint(self,game.house)
		self.bet = self.playersBet(game.initialBet)
		while not moveOn and not game.exitGame and not self.bust:
			self.assistant.monotonousPrint(self,game.house)
			moveOn = self.playersAction(game)
		if self.bust:
			self.assistant.monotonousPrint(self,game.house)
			print(f"\n\n\t\t\t\t\t\t\t\t\t Sorry. You have lost your bet ({self.bet}) on this round.")
			input('\n\t Press enter to continue')
		




	def __str__(self):
		"""
		DOCSTRING: this returns the players name only
		"""
		return_str = f"{self.name} [PC = {self.is_pc}]:\n Cards: {','.join(x for x in self.cards)}\n Score: {self.score}\n Balance: {self.balance}\n Last Bet: {self.bet}"
		return_str = f"\n Number of Aces: {self.aces}"
		return_str += f"\n Player winnings: {str(self.winnings)}\n Player bust: {self.bust}'\n Player won: {self.won}\n----------------\n"
		return  return_str
    

		





