import os

from Dealer import Dealer
from Player import Player
from gameUtils import GameAssistant


class Game:

    def __init__(self):

        print('\n\tWelcome to naive Black-Jack [with ML].\n\n\tNOTE: Please make sure that your window is maximized for optimal viewings')
        print(f"\n\t A new game is being initialised ...")

        assitant = GameAssistant()
    
        player_names = input(f"\n\t Enter the player names (separated by space): ").split(' ')
        # print(f"player_names type = {type(player_names)}")
        # self.__botplayers = assitant.getNumericInput(variable_name='robot players',max_value=len(player_names))
        self.__botplayers = assitant.getNumericInput('robot players',max_value=len(player_names))
        self.buyin = assitant.getNumericInput('buyin',min_value=300,max_value=1000)
        self.players = []
        self.__init_players(player_names)  # list of players
        self.dealer = Dealer()
        self.house = Player('House',999999)
        self.isFinalRound = False
        self.exitGame = False
        self.initBetsize = 50
        self.openingBetIncrease = 0

        self.instructions()

    def __init_players(self,player_names):
        for name in player_names:
            self.players.append(Player(name,self.buyin))
        for i in range(self.__botplayers):
            self.players.append(Player(f"PC-{i+1}",self.buyin,is_pc=True))

    def instructInput(self):
        """
        DOCSTRING: this verifies and establishes if instructions are needed
        """
        valid_input = ['y','j','n']
        affirm_list = valid_input[:-1]

        instrct = ''
        correctInput = False
        while not correctInput:
            instrct = input('\n\tDo you need any instructions on the game? [Y/N] - ')[0].lower()
            correctInput = instrct in valid_input
            if not correctInput:
                print('You did not give a valid answer. Please try again...')
        return instrct in affirm_list
                


    def instructions(self):
        """
        DOCSTRING: This is the instructions on how to play the game.
        """
        instruct = self.instructInput()
        if instruct:
            os.system('cls')
            print('\n\n\tWelcome to BlackJack!')
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
            os.system('cls')
            print("\n\n")
        else:
            pass


    def playersBet(self,player):
        correctInput = False
        isnumber = False
        while not correctInput:
            if (player.balance - self.initbet) < self.initbet:
                print(f"\n\t Your balance is too low for the next round. Your remaining balance of {player.balance} is being bet.")
                input('\n\t Press enter to continue') #time.sleep(7.5)
                bet = player.balance
                player.balance = 0
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
						

    def balanceCheck(self):
        return self.balance == 0

    
    def playersAction(pl1,dealer):
        # correctInput = False
        instrct = ''
        # while not correctInput:
        instrct = input('\tWhat do you want to do?\n\t[H] Hit (draw another card)\n\t[S] Stand (no action)\n\t[E] Exit the game\n\t\t')[0].lower()
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

	