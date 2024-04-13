import math
import random
import os
import time
import sys
sys.path.append('./game_display')
import Display as dp


def monotonousPrint(p1,h1):
	os.system('cls')
	dp.display(h1)
	print('\t\t\t\t\t\t\t\t\t\t========================================')
	dp.display(p1)


class Deck():
	"""
	DOCSTRING: this is only the Deck object
	"""

	cardPoint = {' A':11,' 2':2,' 3':3,' 4':4,' 5':5,' 6':6,' 7':7,' 8':8,' 9':9,'10':10,' J':10,' Q':10,' K':10}


	def __init__(self):
		print('\tNew deck chosen...')
		time.sleep(0.5)
		self.pack = []
		royals = ['10',' J',' Q',' K']
		for suit in ('Di','Cl','Hr','Sp'):
			for number in range(1,14):
				if (number == 1):
					self.pack.append(suit + ' A')
				elif (number in range(10,14)):
					self.pack.append(suit + royals[number-10])
				else:
					self.pack.append(suit +' '+ str(number))


class Dealer():
	"""
	DOCSTRING: this is the object that facilitates playing the game. Most functionality sits here.
	"""
	def __init__(self):
		"""
		DOCSTRING: This is when the dealer is instantiated
		"""
		print('\n\tNew dealer in the game...')
		time.sleep(0.5)
		self.turn =  []
		self.pot_size = 0


	def shuffleCards(self):
		"""
		DOCSTRING: here the new deck is shuffled
		"""
		print('\tDealer shuffled the cards...')
		random.shuffle(deck.pack)
		time.sleep(0.5)

	def dealCards(self):
		"""
		DOCSTRING: initial dealing of cards
		"""
		for i in players:
			i.cards = []
		for j in range(0,2):
			for i in players:
				print('\t\t'+str(i.name)+"'s "+str(j+1)+" card is dealt...")            
				i.cards.append(deck.pack.pop(0))
		for i in players:
			i.score,i.bust = dealer.playerScore(i)

	def playerScore(self,plr):
		"""
		DOCSTRING: calculating the player's score from scratch each time
		"""
		numberOfAces = 0
		handValue = 0
		bust = False
		for c in plr.cards:
			handValue += deck.cardPoint[c[2::]]
			if c[2::] == ' A':
				numberOfAces += 1
		while handValue > 21:
			if numberOfAces > 1:
				handValue -= 11*numberOfAces
				handValue += 11+(numberOfAces-1)
				numberOfAces = 1
			elif numberOfAces == 1:
				handValue -= 10
				numberOfAces = 0
			else:
				bust = True
				break
		return (handValue,bust)

	def extraCard(self,plr):
		"""
		DOCSTRING: hit action is performed
		"""
		plr.addCard(deck.pack.pop(0))
		plr.score,plr.bust = self.playerScore(plr)

	def payWinners(self):
		"""
		DOCSTRING: here the winners are paid
		"""
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


class Player():
	'''
	DOCSTRING: this class can be used for both computer and human players
	NOTE: all classes will have a list, and there is a pc indicator to say if it is an Computer or not
	'''
	is_pc = False


	def __init__(self,name,balance=100):
		'''
		DOCSTRING: this instantiates a player object with the player name
		'''
		self.name = name
		self.bust = False
		self.score = 0
		self.balance = balance
		self.cards = []
		self.bet = 0
		self.winnings = 0
		self.won = False


	def addCard(self,select):
		'''
		DOCSTRING: this adds a card
		'''
		self.cards.append(select)


	def getCard(self):
		'''
		DOCSTRING: this returns the cards
		'''
		return self.cards

	def getName(self):
		'''
		DOCSTRING: this returns the name of the player
		'''
		return self.name

	def __str__(self):
		"""
		DOCSTRING: this returns the players name only
		"""
		return (self.name + ': \nCards: ' + ','.join(x for x in self.cards) + '\nScore: '+str(self.score)+ '\nBalance: '+str(self.balance)+ '\nLast Bet: '+str(self.bet)
				+'\nPlayer winnings: '+str(self.winnings)+'\nPlayer bust: '+str(self.bust)+'\nPlayer won: '+str(self.won)+'\n----------------\n')
		# Removed ->  +'\nBot player: '+str(self.is_pc)  


class Player_PC(Player):
	'''
	DOCSTRING: this class is specific to the COMPUTER players
	NOTE: the only attribute to overwrite is the is_pc one all others stay the same
	'''
	is_pc = True

	def drawCard(self,hse,pcBet):
		if self.name != 'House':
			# monotonousPrint(self,hse)
			betRatio = (1.5 + (self.score-15)/15) # I am checking howfar from 15 is the first 2 cards
			if betRatio <=1:
				betRatio = 1
			self.bet = min(math.floor(pcBet*betRatio),self.balance)
			self.balance -= self.bet
			# print(str(self))
			# input('\n\tPress enter to continue')
			while self.score <= 15:
				monotonousPrint(self,hse)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides to hit\n')
				input('\n\tPress enter to continue')
				dealer.extraCard(self)
			if not self.bust:
				monotonousPrint(self,hse)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides stay\n')
				input('\n\tPress enter to continue')
			else:
				monotonousPrint(self,hse)
				print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and went bust\n')
				input('\n\tPress enter to continue')
		else:
			while self.score <= 16:
				os.system('cls')
				dp.display(hse,True)
				print('\n\t'+self.name+' decides to hit\n')
				input('\n\tPress enter to continue')
				dealer.extraCard(self)
			if self.bust:
				os.system('cls')
				dp.display(hse,True)
				print('\n\n\tThe house has gone bust! All players in the game has won!!!'.upper())
				input('\n\tPress enter to continue')
			else:
				os.system('cls')
				dp.display(hse,True)
				print('\n\t\tThe house has a final score of '+str(self.score))
				input('\n\tPress enter to continue')

class Player_H(Player):
	'''
	DOCSTRING: this class is specific to the HUMAN players
	'''


def balanceCheck():
	for x in players:
		if x.balance == 0:
			os.system('cls')
			return True



def gameSize():
	"""
	DOCSTRING: this verifies and establishes how many players are in the game
	"""
	correctInput = False
	isnumber = False
	playersTotal = 0
	bots = 0
	buy = 0
	while not correctInput:
		try:
			playersTotal = int(input('\n\tHow many players are in the game (max 6): '))
			isnumber = True
		except ValueError:
			print('The input was not a number, please try again...')
		finally:
			if isnumber and playersTotal <= 6 and playersTotal > 0:
				correctInput = True
				print('\tThank you')
			elif isnumber:
				print('This number is out of bounds, please try again...')
				isnumber = False
			else:
				isnumber = False
	correctInput = False
	isnumber = False
	while not correctInput:
		try:
			bots = int(input('\n\tHow many ROBOT players do you want (0 - '+str(round(playersTotal/2))+'): '))
			isnumber = True
		except ValueError:
			print('The input was not a number, please try again...')
		finally:
			if isnumber and bots <= round(playersTotal/2) and bots >= 0:
				correctInput = True
				print('\tThank you')
			elif isnumber:
				print('This number is out of bounds, please try again...')
				isnumber = False
			else:
				isnumber = False
	correctInput = False
	isnumber = False
	while not correctInput:
		try:
			buy = int(input('\n\tBeginning balance for all players in this game (max 1000): '))
			isnumber = True
		except ValueError:
			print('The input was not a number, please try again...')
		finally:
			if isnumber and buy <= 1000 and buy > 0:
				correctInput = True
				print('\tThank you')
			elif isnumber:
				print('This number is out of bounds, please try again...')
				isnumber = False
			else:
				isnumber = False
	return (playersTotal,bots,buy)



def playerStart():
	"""
	DOCSTRING: this initialises the players in the game and the players list
	"""
	player_names = []
	print('\n\tWelcome to Black-Jack.\n\n\tNOTE: Please make sure that your window is maximized for optimal viewings')
	tot,bot,buyin = gameSize()
	print('\n')
	for i in range(0,tot-bot):
		player_names.append(input("\tPlease enter player "+str(i+1)+"'s name: ").capitalize())
	for i in range(0,bot):
		player_names.append("PC"+str(i+1))
	players = []
	for i in range(0,tot-bot):
		players.append(Player_H(player_names[i],buyin))
	for i in range(tot-bot,tot+1):
		if i < tot:
			players.append(Player_PC(player_names[i],buyin))
		else:
			players.append(Player_PC('House',9999999))
	return players



def instructInput():
	"""
	DOCSTRING: this verifies and establishes if instructions are needed
	"""
	instrct = ''
	correctInput = False
	while not correctInput:
		instrct = input('\n\tDo you need any instructions on the game? [Y/N]')
		if len(instrct) > 0:
			if instrct[0].lower() == 'y' or instrct[0].lower() == 'j':
				correctInput = True
				return True
			elif instrct[0].lower() == 'n':
				correctInput = True
				return False
		else:
			print('You did not give a valid answer. Please try again...')


def instructions():
	"""
	DOCSTRING: This is the instructions on how to play the game.
	"""
	instruct = instructInput()
	if instruct:
		os.system('cls')
		print('\n\tOnce more,\n\n\tWelcome to BlackJack!')
		print("\n\tEach player has already been dealt their cards. \n\tWe will start from the first human player and give each player their turn,"
			  " passing chronologically till it is the House's turn")
		print('\n\tBETTING:')
		print("\tYou can only bet on your own turn, on your own hand. \n\tThe initial opening bet has a minimum of 50 and"
			  " after every two rounds this increases by 25.\n\tEach player can choose to bet a higher amount, up to their current balance.")
		print('\tBets are finalized when a player sees their hand and no player will be able to change thereafter')
		print('\n\tHIT / STAND:')
		print("\tEach player has one of two decisions to make on their turn: \n\t\t[H] Hit, or\n\t\t[S] Stand\n\tOn Hit [H] they will be dealt an additional card"
			  ", and on Stand [S] they will end their turn.")
		print('\n\tTHE HOUSE:')
		print("\tThe House will play last of all in each round. The House will Stand on a score of 17 or higher, and will Hit on anything less.")
		print('\n\tWINNING:')
		print("\tEach player's cards will be evaluated directly to the House's hand.\n\tIf your hand is higher than the House, you will win your share of the kittie.")
		print("\tThe kittie is the sum of all the bets. Your share will be the kittie devided by the number of winners.")
		print('\n\tEND GAME:')
		print("\tLastly, the game will end when any human player decides to exit the game, or when any player has a balance of 0")
		input("\n\n\tEnjoy the game!!!")
	else:
		pass




def playersBet(pl1,initbet):
	correctInput = False
	isnumber = False
	while not correctInput:
		if (pl1.balance - initbet) < initbet:
			print('\n\tYour balance is too low for the next round. Your remaining balance of '+str(pl1.balance)+' is being bet.')
			input('\n\tPress enter to continue') #time.sleep(7.5)
			bet = pl1.balance
			pl1.balance = 0
			return bet
		else:
			try:
				bet = int(input('\n\tWhat are you betting on your hand? (min: '+str(initbet)+', remaining balance:'+str(pl1.balance)+')\n\t'))
				isnumber = True
			except ValueError:
				print('The input was not a number, please try again...')
			finally:
				if isnumber and bet >= initbet and bet <= pl1.balance:
					correctInput = True
					print('\tThank you')
					input('\n\tPress enter to continue') #time.sleep(1)
					pl1.balance -= bet
					return bet
				elif isnumber:
					print('This number is out of bounds, please try again...')
					isnumber = False
				else:
					isnumber = False



def playersAction(pl1):
	# correctInput = False
	instrct = ''
	# while not correctInput:
	instrct = input('\tWhat do you want to do?\n\t[H] Hit (draw another card)\n\t[S] Stand (no action)\n\t[E] Exit the game\n\t\t')
	if len(instrct) > 0:
		if instrct[0].lower() == 'h':
			dealer.extraCard(pl1)
			return (False,False)
		elif instrct[0].lower() == 's':
			print('\n\t\tYour final score is '+str(pl1.score)+' with a bet of '+str(pl1.bet))
			input('\n\tPress enter to continue')
			return (True,False)
		elif instrct[0].lower() == 'e':
			return (True,True)
		else:
			print('You did not give a valid answer. Please try again...')
	else:
		pass


def playersChoice(pl1,hse,initialBet,gameExit):
	madeChoice = False
	monotonousPrint(pl1,hse)
	pl1.bet = playersBet(pl1,initialBet)
	while not madeChoice and not gameExit and not pl1.bust:
		monotonousPrint(pl1,hse)
		madeChoice,gameExit = playersAction(pl1)
	if pl1.bust:
		monotonousPrint(pl1,hse)
		print('\n\n\t\t\t\t\t\t\t\t\tSorry. You have lost your bet ('+str(pl1.bet)+') on this round.')
		input('\n\tPress enter to continue')
	return gameExit




"""
DOCSTRING: this is the main program for the game
"""
os.system('cls')
print('\n')
players = playerStart()
os.system('cls')
dealer = Dealer()
deck = Deck()
dealer.shuffleCards()
dealer.dealCards()
instructions()
finalRound = False
gameExit = False
betOpeningIncrease = 0
initialBet = 50
while not gameExit:
	if betOpeningIncrease != 0 and betOpeningIncrease % 2 == 0:
		initialBet += 25
	for a in players:
		if not a.is_pc:
			gameExit = playersChoice(a,players[-1],initialBet,gameExit)
			# gameExit = balanceCheck() if gameExit == False else True
			if gameExit:
				break
		else:
			a.drawCard(players[-1],initialBet)
	if not gameExit:
		betOpeningIncrease += 1
		os.system('cls')
		dealer.payWinners()
		gameExit = balanceCheck()
		if gameExit:
			break
		corInp = False
		while not corInp:
			gameExt = input('\n\n\t\tDo you want to continue? [Y/N]')
			if len(gameExt) > 0:
				if gameExt[0].lower() == 'n':
					gameExit = True
					break
				elif gameExt[0].lower() == 'y' or gameExt[0].lower() == 'j':
					break
				else:
					print('You did not give a valid answer. Please try again...')
			else:
				pass
		if not gameExit:
			os.system('cls')
			deck = Deck()
			dealer.shuffleCards()
			dealer.dealCards()
os.system('cls')
if balanceCheck():
	lowBalPlayers = []
	for i in players:
		if i.balance == 0:
			lowBalPlayers.append(i.name)
	print('The following player(s) have zero balances that caused the game to exit: '+','.join(x for x in lowBalPlayers)+'\n')
	print('\n\tThe final standing was:')
else:
	print('\n\tThank you for playing. The final standing was:')
dealer.payWinners()
