import math
import random
import os
import time
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
            print('\t\t'+str(i.name)+"'s cards dealt...")
            i.cards = []
            time.sleep(0.5)
            for j in range(0,2):
                i.cards.append(deck.pack.pop(j))
            i.score,i.bust = dealer.playerScore(i)
            # print(str(i))

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
        if players[-1].bust:
            for i in players:
                if i.name != 'House':
                    i.won = True
                    i.balance += i.bet*2
                print(str(i))
        else:
            for i in players:
                if i.name != 'House' and not i.bust:
                    if i.score >= players[-1].score:
                        i.won = True
                        i.balance += i.bet*2
                else:
                    pass
                print(str(i))
        for i in players:
            i.bust = False
            i.won = False
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
                +'\nBot player: '+str(self.is_pc)+'\nPlayer bust: '+str(self.bust)+'\nPlayer won: '+str(self.won)+'\n----------------')


class Player_PC(Player):
    '''
    DOCSTRING: this class is specific to the COMPUTER players
    NOTE: the only attribute to overwrite is the is_pc one all others stay the same
    '''
    is_pc = True

    def drawCard(self,hse,pcBet):
        if self.name != 'House':
            monotonousPrint(self,hse)
            self.bet = pcBet
            self.balance -= pcBet
            print(str(self))
            input('\n\tPress enter to continue')
            while self.score <= 15:
                monotonousPrint(self,hse)
                print('\n\t\t'+self.name+' decides to hit\n')
                input('\n\tPress enter to continue')
                dealer.extraCard(self)
            if not self.bust:
                monotonousPrint(self,hse)
                print('\n\t\t'+self.name+' decides stay\n')
                input('\n\tPress enter to continue')
            else:
                monotonousPrint(self,hse)
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



def instructInput():
    """
    DOCSTRING: this verifies and establishes if instructions are needed
    """
    instrct = ''
    correctInput = False
    while not correctInput:
        instrct = input('\n\tDo you need any instructions on the game? [Y/N]')
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
        print("\n\tEach player has already been dealt their cards. \n\tWe will start from the first human player and give each player their turn, passing chronologically till it is the House's turn")
        print("\n\tYou can only bet on your own turn on your own hand. \n\tThe initial opening bet has a minimum of 50 and after every two rounds this increases by 25.\n\tEach player can choose to bet a higher amount, up to their current balance.")
        print("\n\tEach player has one of two decisions to make on their turn: \n\t\t[H] Hit, or\n\t\t[S] Stand\n\tOn Hit [H] they will be dealt an additional card, and on Stand [S] they will end their turn.\n\tBets will be locked in before the first decision is made.")
        print("\n\tLastly, the House will play. The House will Stand on a score of 17 or higher, and will Hit on anything less."
              "\n\tEach player's cards will be evaluated directly to the House's hand.\n\tIf your hand is the same or higher than the House, you will win your bet.")
        input("\n\n\tEnjoy the game!!!")
    else:
        pass




def playersBet(pl1,initbet):
    correctInput = False
    isnumber = False
    while not correctInput:
        if (pl1.balance - initbet) < initbet:
            print('\n\tUnfortunately your balance is too low to continue. Your remaining balance of '+str(pl1.balance)+' is being bet.')
            time.sleep(5)
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
                    time.sleep(1)
                    pl1.balance -= bet
                    return bet
                elif isnumber:
                    print('This number is out of bounds, please try again...')
                    isnumber = False
                else:
                    isnumber = False



def playersAction(pl1):
    correctInput = False
    instrct = ''
    while not correctInput:
        instrct = input('\tWhat do you want to do?\n\t[H] Hit (draw another card)\n\t[S] Stand (no action)\n\t[E] Exit the game\n\t\t')
        if len(instrct) > 0:
            if instrct[0].lower() == 'h':
                dealer.extraCard(pl1)
                return (False,False)
            elif instrct[0].lower() == 's':
                print('\n\tThank you.\t\tYour final score is '+str(pl1.score)+' with a bet of '+str(pl1.bet))
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
# for i in range(0, len(players)):
#    print(players[i].name + ' ' + str(players[i].balance))
dealer = Dealer()
deck = Deck()
# print(deck.pack)
#print('\n****************************\n\tShuffled pack\n')
dealer.shuffleCards()
dealer.dealCards()
# for x in players:
#     print(str(x))
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
            if gameExit:
                break
        else:
            a.drawCard(players[-1],initialBet)
    if not gameExit:
        betOpeningIncrease += 1
        os.system('cls')
        dealer.payWinners()
        corInp = False
        while not corInp:
            gameExt = input('\n\n\t\tDo you want to continue? [Y/N]')
            if gameExt[0].lower() == 'n':
                gameExit = gameExt
                break
            elif gameExt[0].lower() == 'y' and gameExt[0].lower() == 'j':
                break
            else:
                print('You did not give a valid answer. Please try again...')
        if not gameExit:
            deck = Deck()
            dealer.shuffleCards()
            dealer.dealCards()
os.system('cls')
print('\n\tThank you for playing. The final standing was:')
dealer.payWinners()






#print(d.pack)
