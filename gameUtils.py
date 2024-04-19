import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

class GameAssistant:

    def getGameDetails(self):
        name_inputs = input(f"\n\t Enter the player names (separated by space) ['default'/<ENTER> for default]: ")
        isDefault = (name_inputs[0] == 'd' if not(name_inputs == '') else True)
        self.player_names = ['Joe','Albert'] if isDefault else name_inputs.split(' ')
        self.bots = 1 if isDefault else self.getNumericInput('robot players',max_value=len(self.player_names))
        self.buyin = 300 if isDefault else self.getNumericInput('buyin',min_value=300,max_value=1000)
        if isDefault:
            print(f"\n\t\t\t **Defaults used: names={self.player_names}, bots={self.bots}, buyin={self.buyin}**")

    def printWinners(self,game):
        print("\n\t\t\t\t\t ***** RESULTS ***** ")
        winners_count = len(game.winners[game.roundNumber])
        per_winner_winnings = round(game.pot / winners_count) if winners_count > 0 else 0
        print(f"\n Total winnings: {game.pot}\n Total winners: {winners_count}\n Winners share: {per_winner_winnings}\n")
        winners_string = ','.join(i for i in game.winners[game.roundNumber])
        print("Winners: "+winners_string+"\n\n")
        for player in game.players:
            print(player)


    def getNumericInput(self, variable_name, min_value=None, max_value=None):
        
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

    
    def monotonousPrint(self, player, house):
        os.system('cls')
        dp.display(house)
        print('\t'*10 + '='*40)
        dp.display(player)