import math
import random
import os
import time
import Display

class Deck():
    """
    DOCSTRING: this is only the Deck object
    """

    cardPoint = {' A':11,' 2':2,' 3':3,' 4':4,' 5':5,' 6':6,' 7':7,' 8':8,' 9':9,'10':10,' J':10,' Q':10,' K':10}
    cardToken = {'Di':'\u2666','Cl':'\u2663','Hr':'\u2665','Sp':'\u2660'}

    def __init__(self):
        print('\tNew deck chosen...')
        time.sleep(1)
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
        time.sleep(1)
        self.turn =  []
        self.pot_size = 0


    def shuffleCards(self):
        """
        DOCSTRING: here the new deck is shuffled
        """
        print('\tDealer shuffled the cards...')
        random.shuffle(deck.pack)
        time.sleep(1)

    def dealCards(self):
        """
        DOCSTRING: initial dealing of cards
        """
        for i in players:
            print('\t\t'+str(i.name)+"'s cards dealt...")
            time.sleep(1)
            for j in range(0,2):
                i.cards.append(deck.pack.pop(j))
            i.score = playerScore(i)

    def playerScore(self,plr):
        """
        DOCSTRING: calculating the player's score from scratch each time
        """
        numberOfAces = 0
        handValue = 0
        for c in plr.cards:
            handValue += cardPoint[c[2::]]
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
                plr.bust == True
                break
        plr.score = handValue

    def extraCard(self,plr):
        """
        DOCSTRING: hit action is performed
        """
        plr.addCard(deck.pack.pop(0))
        playerScore(plr)


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
        return self.name


class Player_PC(Player):
    '''
    DOCSTRING: this class is specific to the COMPUTER players
    NOTE: the only attribute to overwrite is the is_pc one all others stay the same
    '''
    is_pc = True

    def drawCard(self):
        if self.score <= 15 and self.name != "House":
            dealer.extraCard(self)
        elif self.score <= 16 and self.name == 'House':
            dealer.extraCard(self)
        else:
            pass

class Player_H(Player):
    '''
    DOCSTRING: this class is specific to the HUMAN players
    '''
    def drawCard(self):
        dealer.extraCard(self)


def drawCard(crd):
    #print('\u0201===============\u187')
    pass




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
    playrs = []
    print('\n\tWelcome to Black-Jack.')
    tot,bot,buyin = gameSize()
    # print('Total players:'+str(tot))
    # print('Total Robots:'+str(bot))
    print('\n')
    for i in range(1,tot-bot+1):
        playrs.append(input("\tPlease enter player "+str(i)+"'s name: ").capitalize())
    for i in range(1,bot+1):
        playrs.append("PC"+str(i))
    # print(playrs)
    players = []
    for i in range(0,tot-bot):
        players.append(Player_H(playrs[i],buyin))
    for i in range(tot-bot,tot+1):
        if i < tot:
            players.append(Player_PC(playrs[i],buyin))
        else:
            players.append(Player_PC('House',99999999))
    return players

# This is the testing program for now


os.system('cls')
print('\n')
players = playerStart()
os.system('cls')
# for i in range(0, len(players)):
#    print(players[i].name + ' ' + str(players[i].balance))
dealer = Dealer()
deck = Deck()
# print(deck.pack)
#print('\n****************************\n\tShuffled pack\n')
dealer.shuffleCards()
dealer.dealCards()
for a in players[len(players)]:
    print('Player name: ' + a.name)
    print('Cards dealt: \n')
    for b in a.cards:
        print(b)
    print('==================\n')

#print(d.pack)
