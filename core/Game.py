import os
import uuid

from core.Dealer import Dealer
from core.Player import Player
from core.GameAssistant import GameAssistant


class Game:

    def __init__(self,isTesting=False):
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
        if not isTesting:
            print('\n\t Welcome to naive Black-Jack [with ML].\n\n\tNOTE: Please make sure that your window is maximized for optimal viewings')
            self.instructions()

        # Generate a unique game ID
        self.game_ID = str(uuid.uuid4())

        assistant = GameAssistant()
        assistant.getGameDetails(isTesting=isTesting)

        self.affirm_list = ['y','j']
        self.valid_list = ['y','j','n']
        self.house = Player('House',999999)
        self.buyin = assistant.buyin
        self.__botplayers = assistant.bots
        self.__init_players(assistant.player_names)  # list of players
        self.dealer = Dealer()
        self.winners = {}
        self.exitGame = False
        self.initialBet = 50
        self.roundNumber = 0




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

    


    def balanceCheck(self,isTesting=False):
        """
        Checks if any player in the game has a balance of 0 or less. If so, displays a message with the names of the players who have a zero balance.

        Returns:
            bool: True if any player has a balance of 0 or less, False otherwise.
        """
        lowBalPlayers = [p.name for p in self.players if p.balance <= self.initialBet]
        if len(lowBalPlayers)>0:
            self.players = [p for p in self.players if p.name not in lowBalPlayers]
            if not isTesting:
                input('\n\n The following player(s) have a zero balance and will be exiting the game: '+','.join(lowBalPlayers)+'\n')
                


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
            print("\n\tAIM:")
            print("\tThe aim of the game is to get a higher hand than the House. There is a condition: you cannot have more than 21. If your hand goes over 21, you go bust.")
            print("\tIn essence each player, plays against the House. Each player will be able to see one of the House's cards, when placing their bets.")
            print("\n\tSCORING:")
            print("\tEach number card scores their number in the hand. All face cards count 10. Aces count either 11 or 1, which ever benefits the players hand.")
            print("\n\tSETUP:")
            print("\tThe game starts by asking who will be playing? Enter a list of player names separated by spaces. Additionally the number of bots can be specified as well.")
            print("\tOnce the players have been defined (human and robot) the cards are dealt to all players including the House.")
            print("\tPlay starts with the first human player and sequentially follows the list given, till the House has the final turn")
            print('\n\tBETTING:')
            print("\tWhen you place your first bet, you can only see the House's one card. You bet, and once you have placed the bet, you will see your cards." \
                  " When you see your cards for the first time,\n\tyou have three options: Double down [d], Hit [h], or Stay [s]. Double down [d], allows you to double your bet while getting another card." \
                    " Double down is only available once,\n\tand is not available in any following decisions of your turn. \n\tThe initial opening bet has a minimum of 50 and"
                " after every two rounds this increases by 25.\n\tEach player can choose to bet a higher amount than the minimum, up to their current balance.")
            print('\n\tHIT / STAND:')
            print("\tEach player has one of two decisions to make on their turn: \n\t\t[H] Hit - an additional card is dealt, or\n\t\t[S] Stand - their turn ends")
            print('\n\tTHE HOUSE:')
            print("\tThe House will play last of all in each round. The House will Stand on a hand of 17 or higher, and will Hit on anything less.")
            print('\n\tWINNING:')
            print("\tEach player's cards will be evaluated directly against the House's hand.\n\tIf your hand is higher than the House, you receive double your bet (i.e. replenishes your bet and gaining another bet in addition).")
            print("\tWhen you have a Black Jack (i.e. score 21 with only two cards, e.g. A and K) you receive 2.5 times your bet, if the house does not also get 21.")
            print("\tIf your hand is equal with the House, you will receive back your bet, and if you are below the House, you loose your bet.")
            print('\n\tEND GAME:')
            print("\tLastly, the game will end when any human player decides to exit the game, or when there is only one human player left.")
            print("\tAdditionally, the game will exit at any time if <CTRL + C> is pressed.")
            input("\n\n\tEnjoy the game!!!")
            os.system('cls')
            print("\n\n")


	