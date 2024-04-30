import os

from core.Dealer import Dealer
from core.Player import Player
from core.GameAssistant import GameAssistant


class Game:

    def __init__(self):
        """
        Initializes a new instance of the Game class.

        This method is called when a new instance of the Game class is created. It sets up the initial state of the game,
        including printing a welcome message, getting game details from the GameAssistant class, initializing game variables,
        creating a Player object for the house, setting the buy-in amount, creating bot players, initializing players,
        creating a Dealer object, initializing the winners dictionary, setting the exit game flag to False,
        and setting the initial bet to 50, and setting the round number to 0.
        
        Finally, it calls the instructions method to display game instructions to the user.

        Parameters:
            None

        Returns:
            None
        """

        print('\n\t Welcome to naive Black-Jack [with ML].\n\n\tNOTE: Please make sure that your window is maximized for optimal viewings')
        print(f"\n\t A new game is being initialised ...")

        assistant = GameAssistant()
        assistant.getGameDetails()

        self.affirm_list = ['y','j']
        self.valid_list = ['y','j','n']
        self.house = Player('House',999999)
        self.buyin = assistant.buyin
        self.__botplayers = assistant.bots
        self.__init_players(assistant.player_names)  # list of players
        self.dealer = Dealer()
        self.winners = {}
        # self.isFinalRound = False
        self.exitGame = False
        self.initialBet = 50
        self.roundNumber = 0

        self.instructions()



    def __init_players(self,player_names):
        """
        Initializes the players for the game.

        Args:
            player_names (list): A list of player names.

        Returns:
            None

        This function creates a list of Player objects based on the given player names.
        It appends each Player object to the `self.players` list.
        Additionally, it creates bot players and appends them to the `self.players` list.
        The bot players are created using the `Player` class with the name "PC-{i+1}" and the `self.buyin` value.
        The number of bot players is determined by the value of `self.__botplayers`.
        
        """
        self.players = []
        for name in player_names:
            self.players.append(Player(name,self.buyin))
        for i in range(self.__botplayers):
            self.players.append(Player(f"PC-{i+1}",self.buyin,is_pc=True))


    def newRound(self,isFirstRound=False):
        """
        A function to start a new round in the game.

        Args:
            self: the object itself
            isFirstRound (bool): A flag indicating if it's the first round of the game. Default is False.

        Returns:
            None
        """
        if self.roundNumber != 0 and self.roundNumber % 2 == 0:
            self.initialBet += 25
        if not isFirstRound:
            self.roundNumber += 1
        self.house.newRound()
        self.dealer.newRound()
        for player in self.players:
            player.newRound()
        self.dealer.dealCards(self.players + [self.house])

    


    def balanceCheck(self):
        """
        Checks if any player in the game has a balance of 0 or less. If so, displays a message with the names of the players who have a zero balance.

        Returns:
            bool: True if any player has a balance of 0 or less, False otherwise.
        """
        balanceBroke = any(x.balance <= 0 for x in self.players)
        if balanceBroke:
            lowBalPlayers = [p.name for p in self.players if p.balance <= 0]
            input('The following player(s) have zero balances that caused the game to exit: '+','.join(lowBalPlayers)+'\n')
        return balanceBroke


    def instructions(self):
        """
        DOCSTRING: This is the instructions on how to play the game.
        """
        valid_input = ['y','j','n']
        affirm_list = valid_input[:-1]
        instrct = input("\n\t Do you need any instructions on the game? [ Y / (N) ] ")
        instruct = (instrct[0].lower() in affirm_list if not(instrct == '') else False)

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


	