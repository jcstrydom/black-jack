import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

class GameAssistant:

    def getGameDetails(self):
        """
        Prompts the user to enter player names and other game details.

        Parameters:
            None

        Returns:
            None
        """
        name_inputs = input(f"\n\t Enter the player names (separated by space) [<ENTER> --> default]: ")
        isDefault = (name_inputs[0] == 'd' if not(name_inputs == '') else True)
        self.player_names = ['Joe','Albert'] if isDefault else name_inputs.split(' ')
        self.bots = 1 if isDefault else self.getNumericInput('robot players',max_value=len(self.player_names))
        self.buyin = 300 if isDefault else self.getNumericInput('buyin',min_value=300,max_value=1000)
        if isDefault:
            print(f"\n\n\n\t\t\t << !!! Defaults used: names={self.player_names}, bots={self.bots}, buyin={self.buyin}  !!! >> \n\n\n")


    def printWinners(self,game):
        """
        A function to print the winners of a game round along with their details and winnings.

        Parameters:
            self: the object itself
            game: an instance of the Game class representing the current game state

        Returns:
            None
        """
        print("\n\t\t\t\t\t" + "="*40 + f"\n\t\t\t\t\t\t  RESULTS FOR ROUND {game.roundNumber}\n\t\t\t\t\t" + "="*40 + "\n")
        max_round_of_winners = max(list(game.winners.keys())) if len(game.winners) > 0 else -1
        if max_round_of_winners != -1:
            winners_count = len(game.winners[max_round_of_winners])
            per_winner_winnings = round(game.dealer.pot / winners_count) if winners_count > 0 else 0
            print(f"\n ROUND = {max_round_of_winners:>3}; Total winnings: {game.dealer.pot:>6}; Total winners: {winners_count:>6}; Winners share: {per_winner_winnings:>6}; ")
            winners_string = ','.join(game.winners[max_round_of_winners])
            print("Winners: "+winners_string+"\n")
        else:
            print("\n No winners this round\n\n")
        
        print(game.house)
        for player in game.players:
            print(player)


    def getNumericInput(self, variable_name, min_value=None, max_value=None):
        """
        Get a numeric input from the user with optional minimum and maximum values.

        Args:
            variable_name (str): The name of the variable to prompt the user for.
            min_value (int, optional): The minimum allowed value for the input. Defaults to None.
            max_value (int, optional): The maximum allowed value for the input. Defaults to None.

        Returns:
            int: The valid numeric input entered by the user.

        Raises:
            ValueError: If the input is not a valid numeric value or falls outside the specified range.
        """
        
        __valid_input = False

        # print(f"min_value = {min_value}")
        # print(f"max_value = {max_value}")

        request_str = f"\n\t Please enter number for {variable_name} "
        conditions = []
        if min_value:
            conditions.append(f"min: {min_value}")
        if max_value:
            conditions.append(f"max: {max_value}")

        if len(conditions) > 0:
            request_str += f" [{', '.join(conditions)}]: "

        while not __valid_input:
            try:
                var_value = int(input(request_str))
                if min_value and var_value < min_value:
                    raise ValueError
                if max_value and var_value > max_value:
                    raise ValueError
                __valid_input = True
                return var_value
            except ValueError:
                print("Invalid input. Please try again...")

    
    def playerHouseHandDisplay(self, player, house):
        """
        A function that prints the hand of both the player and house

        Parameters:
            player (object): The player object to be displayed.
            house (object): The house object to be displayed.

        Returns:
            None
        """
        os.system('cls')
        dp.display(house)
        print('\t'*10 + '='*40)
        dp.display(player)