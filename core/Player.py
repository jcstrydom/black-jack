import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

import math
from core.GameAssistant import GameAssistant

class Player():
    '''
    DOCSTRING: this class can be used for both computer and human players
    NOTE: all classes will have a list, and there is a pc indicator to say if it is an Computer or not
    '''
    # is_pc = False


    def __init__(self,name,balance=100,is_pc=False):
        """
        DOCSTRING: This function initializes a Player object with the provided name, balance, and PC indicator. 
        """
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
        """
        Resets the player's attributes at the start of a new round: bust to False, clears the cards list,
        sets the number of aces to zero, resets the hand value to zero, sets the bet amount to zero, and marks 
        the player as not having won.
        """
        self.bust = False
        self.cards = []
        self.aces = 0
        self.hand = 0
        self.bet = 0
        self.won = False


    def addCard(self,select):
        """
        Adds a card to the player's hand.

        Parameters:
            select (Card): The card to be added to the player's hand.

        Returns:
            None
        """
        self.cards.append(select)


    def getCards(self):
        """
        Get the list of cards held by the player.

        Returns:
            list: The list of cards held by the player.
        """
        return self.cards

    def getName(self):
        """
        Get the name of the player.
        Returns:
            str: The name of the player.
        """
        return self.name
    
    def determineBet(self,game):
        """
        Determines the bet for the player based on the current game state.

        Parameters:
            game (Game): The current game object.

        Returns:
            None

        This function calculates the bet for the player based on the current game state.
        If the player is a computer player, the bet is calculated based on the player's hand value.
        The bet is then deducted from the player's balance and added to the game's pot.
        If the player is a human player, they are prompted to enter their bet.
        The function validates the input and ensures it is within the valid range.
        If the player chooses to go all-in, their bet is set to their entire balance and their balance is updated accordingly.

        Note:
            - This function assumes that the game object has an `initialBet` attribute representing the minimum bet allowed in the game.
            - This function assumes that the game object's `dealer` attribute is an instance of the `Dealer` class and has a `pot` attribute to store the bets.
        """
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
        """
        This is a method specifically for the PC player to draw a card
        """
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
        """
        This function handles the decision to hit or stay for the player in a game of blackjack.
        It takes in the game object as a parameter and uses it to make decisions based on the player's hand value and whether the player is a human or a computer.
        
        If the player is a human, it enters a loop where the player input is requested on their decision to hit, stay or exit.

        In the player is a a bot, and the player's hand value exceeds 15, it displays the player's hand and waits for user to acknowledge the decision from the bot.
        The heuristic used for the bot player is to add a card if the hand is less than or equal to 15, otherwise it will stay.
        """
        if self.is_pc:
            while self.hand <= 15:
                self.assistant.playerHouseHandDisplay(self,game.house)
                print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides to hit\n')
                input('\n\tPress enter to continue')
                game.dealer.addCard(self)
            if not self.bust:
                self.assistant.playerHouseHandDisplay(self,game.house)
                print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and decides stay\n')
                input('\n\tPress enter to continue')
            else:
                self.assistant.playerHouseHandDisplay(self,game.house)
                print('\n\t\t'+self.name+' has bet '+str(self.bet)+' and went bust\n')
                input('\n\tPress enter to continue')
        else:
            keepOn = True
            while (not self.bust) and (keepOn):
                self.assistant.playerHouseHandDisplay(self,game.house)
                action = input('\t What do you want to do?\n\t [(H)] Hit (draw another card)\n\t [ S ] Stand (no action)\n\t [ E ] Exit the game\n\t\t')
                action = (action[0].lower() if not(action == '') else 'h')
                match (action):
                    case 'h':
                        game.dealer.addCard(self)
                    case 's':
                        input(f"\n\t\t Your current score is {self.hand} with a bet of {self.bet}")
                        keepOn = False
                    case 'e':
                        game.exitGame = True
                        keepOn = False
                    case _:
                        print('You did not give a valid answer. Please try again...')



    def playersChoice(self,game):
        """
        This function allows the player to make a choice during the game.
        
        Parameters:
            game (Game): The game object representing the current game state.
        
        Returns:
            None
        """
        moveOn = False
        self.assistant.playerHouseHandDisplay(self,game.house)
        self.determineBet(game)
        self.hitStayExit(game)
        # while not moveOn and not game.exitGame and not self.bust:
        #     self.assistant.monotonousPrint(self,game.house)
        #     moveOn = self.hitStayExit(game)
        if self.bust:
            self.assistant.playerHouseHandDisplay(self,game.house)
            print(f"\n\n\t\t\t\t\t\t\t\t\t Sorry. You have lost your bet ({self.bet}) on this round.")
            input('\n\t Press enter to continue')



    def __str__(self):
        """
        Returns a string representation of the Player object. The string includes the player's name, whether the player is a computer or not,
        the player's cards, their hand value, their balance, their last bet, the number of aces they have, their winnings, whether they have busted,
        and whether they have won.
        
        The string is formatted with the player's name left justified to 18 characters, and the player's cards are joined with semicolons. The string ends with a horizontal line.

        :return: A string representation of the Player object.
        :rtype: str
        """
        return_str = f"{self.name:<18} [PC = {self.is_pc}]:\n Cards:            {'; '.join(x for x in self.cards)}\n Hand:             {self.hand}"
        return_str += f"\n Balance:          {self.balance}\n Last Bet:         {self.bet}"
        return_str += f"\n Number of Aces:   {self.aces}"
        return_str += f"\n Player winnings:  {str(self.winnings)}\n Player bust:      {self.bust}\n Player won:       {self.won}\n --------------------------------\n"
        return  return_str
    
    def __repr__(self):
        """
        A description of the entire function, its parameters, and its return types.
        """
        return f"Player({self.name})"

        





