import random
import os
from Deck import Deck


class Dealer():
	"""
	DOCSTRING: this is the object that facilitates playing the game. Most functionality sits here.
	"""
	def __init__(self,turn=0):
		"""
		DOCSTRING: This is when the dealer is instantiated
		"""
		print('\n\tNew dealer in the game...')
		self.pot_size = 0
		self.deck = Deck()
		self.shuffleCards()

	def newRound(self):
		self.__init__()


	def shuffleCards(self):
		"""
		DOCSTRING: here the new deck is shuffled
		"""
		print('\tDealer shuffled the cards...')
		random.shuffle(self.deck.pack)


	def dealCards(self,players):
		"""
		DOCSTRING: initial dealing of cards
		"""
		
		## Just dealing the initial two cards per person
		for j in range(0,2):
			for player in players:
				print(f"\t\t{player.name}'s {j+1} card is dealt...")
				player.cards.append(self.deck.pack.pop(0))
				self.calculatePlayerScore(player)

	def calculatePlayerScore(self,player):
		"""
		DOCSTRING: calculating the player's score from scratch each time
		"""
		player.hand = 0
		player.aces = 0
		for c in player.cards:
			card_value = c.split(' ')[1]
			if card_value.lower() == 'a':
				player.aces += 1
			# os.system('clear')
			player.hand += self.deck.cardPoints[card_value]
		
		# input('-'*40 + f"\n{player.name.upper()} ACES = {player.aces}\n" + '-'*40)
		reset_tries = 0
		while player.hand > 21:
			if reset_tries < player.aces and player.aces > 0:
				reset_tries += 1
				player.hand -= 10
			else:
				player.bust = True
				break


	def addCard(self,player):
		"""
		DOCSTRING: hit action is performed
		"""
		player.cards.append(self.deck.pack.pop(0))
		self.calculatePlayerScore(player)


	def payWinners(self,game):
		"""
		DOCSTRING: here the winners are paid
		"""
		winning_players = []


		if game.house.bust:
			for i in game.players:
				if not i.bust:
					i.won = True
					winning_players.append(i.name)
		else:
			for i in game.players:
				if not i.bust and i.hand > game.house.hand:
					i.won = True
					winning_players.append(i.name)
					
		winners = len(winning_players)

		if winners == 0:
			game.house.won = True
			game.house.winnings += game.pot
			winning_players.append('House')
		else:
			per_winner_winnings = round(game.pot / winners)
			for i in game.players:
				if i.won:
					i.winnings[game.roundNumber] = per_winner_winnings
					i.balance += i.winnings[game.roundNumber]
					winning_players.append(i.name)
	
		game.winners[game.roundNumber] = winning_players
				
					

		
