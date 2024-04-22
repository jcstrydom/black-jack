import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

import math
from GameAssistant import GameAssistant

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
        self.balance = balance
        self.is_pc = is_pc
        self.bust = False
        self.cards = []
        self.aces = 0
        self.hand = 0
        self.bet = 0
        self.winnings = {}
        self.won = False

    def newRound(self):
        self.bust = False
        self.cards = []
        self.aces = 0
        self.hand = 0
        self.bet = 0
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
    
    def determineBet(self,game):
        if self.is_pc:
            betRatio = (1.5 + (self.hand-15)/15) # I am checking howfar from 15 is the first 2 cards
            if betRatio <=1:
                betRatio = 1
            self.bet = min(math.floor(game.initialBet*betRatio),self.balance)
            self.balance -= self.bet
            game.dealer.pot += self.bet
        else:
            while True:
                try:
                    bet = input(f"\n\t {self.name}, what's your bet? [min: ({game.initialBet}), balance: {self.balance}] ")
                    bet = int(bet) if not(bet == '') else game.initialBet
                    if self.balance < game.initialBet:
                        bet = self.balance
                        print(f"\n\t {self.name} is ALL-IN. Your final bet is: {self.balance}")
                        self.bet = bet
                        self.balance -= bet
                        game.dealer.pot += bet
                        break
                    elif game.initialBet <= bet <= self.balance:
                        self.bet = bet
                        self.balance -= bet
                        game.dealer.pot += bet
                        break
                    else:
                        print(f"\n\t Please enter a valid integer less than or equal to your balance ({self.balance}).")
                    raise ValueError
                except ValueError:
                    print(f"\n\t Please enter a valid integer between the minimum and your balance ({self.balance}).")

    

    def houseHitStay(self,game):
        """This is a method specifically for the PC player to draw a card"""
        while self.hand <= 16:
            os.system('cls')
            dp.display(game.house,True)
            print(f"\n\t {self.name} decides to hit. Currently on {self.hand}.\n")
            input('\n\tPress enter to continue')
            game.dealer.addCard(self)
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

    

    def hitStayExit(self,game):
        if self.is_pc:
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
            while True:
                self.assistant.monotonousPrint(self,game.house)
                action = input('\t What do you want to do?\n\t [(H)] Hit (draw another card)\n\t [ S ] Stand (no action)\n\t [ E ] Exit the game\n\t\t')
                action = (action[0].lower() if not(action == '') else 'h')
                match (action):
                    case 'h':
                        game.dealer.addCard(self)
                    case 's':
                        input(f"\n\t\t Your current score is {self.hand} with a bet of {self.bet}")
                        break
                    case 'e':
                        game.exitGame = True
                        break
                    case _:
                        print('You did not give a valid answer. Please try again...')



    def playersChoice(self,game):
        moveOn = False
        self.assistant.monotonousPrint(self,game.house)
        self.determineBet(game)
        self.hitStayExit(game)
        # while not moveOn and not game.exitGame and not self.bust:
        #     self.assistant.monotonousPrint(self,game.house)
        #     moveOn = self.hitStayExit(game)
        if self.bust:
            self.assistant.monotonousPrint(self,game.house)
            print(f"\n\n\t\t\t\t\t\t\t\t\t Sorry. You have lost your bet ({self.bet}) on this round.")
            input('\n\t Press enter to continue')



    def __str__(self):
        """
        DOCSTRING: this returns the players name only
        """
        return_str = f"{self.name:<18} [PC = {self.is_pc}]:\n Cards:            {'; '.join(x for x in self.cards)}\n Hand:             {self.hand}"
        return_str += f"\n Balance:          {self.balance}\n Last Bet:         {self.bet}"
        return_str += f"\n Number of Aces:   {self.aces}"
        return_str += f"\n Player winnings:  {str(self.winnings)}\n Player bust:      {self.bust}\n Player won:       {self.won}\n --------------------------------\n"
        return  return_str
    
    def __repr__(self):
        return f"Player({self.name})"

        





