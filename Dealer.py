import random
import os
from Deck import Deck


class Dealer():
	"""
	DOCSTRING: this is the object that facilitates playing the game. Most functionality sits here.
	"""
	def __init__(self):
		"""
		DOCSTRING: This is when the dealer is instantiated
		"""
		print('\n\tNew dealer in the game...')
		self.turn =  []
		self.pot_size = 0
		self.deck = Deck()
		self.shuffleCards()


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
		for c in player.cards:
			card_value = c.split(' ')[1]
			player.hand += self.deck.cardPoints[card_value]
		
		reset_tries = 0
		while player.hand > 21:
			if player.aces > 0:
				if reset_tries < player.aces:
					reset_tries += 1
					player.hand -= 10
				else:
					pass
			else:
				player.bust = True
				break


	def addCard(self,player):
		"""
		DOCSTRING: hit action is performed
		"""
		card_to_add = self.deck.pack.pop(0)
		player.addCard(card_to_add)
		if card_to_add.split(' ')[1].lower() == 'a':
			player.aces += 1
		# os.system('clear')
		input('-'*40 + f"\n{player.name.upper()} ACES = {player.aces}\n" + '-'*40)
		self.calculatePlayerScore(player)


	def payWinners(self,players):
		"""
		DOCSTRING: here the winners are paid
		"""
		house = players[-1]
		players = players[:-1]


		kittie = 0
		winners = 0
		winning_players = []
		
		
		for i in players:
			kittie += i.bet


		if players[-1].bust:
			for i in players:
				if i.name != 'House' and not i.bust:
					i.won = True
					winners += 1
					winning_players.append(i.name)
		else:
			for i in players:
				if i.name != 'House' and not i.bust:
					if i.score > players[-1].score:
						i.won = True
						winners += 1
						winning_players.append(i.name)
				else:
					pass
		if winners == 0:
			players[-1].balance = kittie
			players[-1].won = True
			players[-1].winnings = kittie
			winners = 1
			winning_players.append(players[-1].name)
		else:
			for i in players:
				if i.won:
					i.winnings = round(kittie / winners)
				else:
					i.winnings = 0
				i.balance += i.winnings
					

		print('\nTotal winnings: '+str(kittie)+'\nTotal winners: '+str(winners)+'\nWinners share: '+str(round(kittie / winners)))
		winners_string = ','.join(i for i in winning_players)
		print("Winners: "+winners_string+"\n\n")

		for i in players:
			print(str(i))
			i.bust = False
			i.won = False
			i.winnings = 0
			i.bet = 0
			i.score = 0
