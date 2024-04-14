import os,sys
sys.path.append('./game_display')
import game_display.Display as dp

class GameAssistant:

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

    
    def monotonousPrint(player,house):
        os.system('cls')
        dp.display(house)
        print('\t'*10 + '='*40)
        dp.display(player)