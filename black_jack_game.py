import os, sys, keyboard
import sqlite3

sys.path.append('./game_display')
from core.Game import Game
from core.GameAssistant import GameAssistant

# Establish a connection to the database
CONN = sqlite3.connect('data/game_state.db')
C = CONN.cursor()

def __createTables():
    C.execute('''
            CREATE TABLE IF NOT EXISTS players_bet (
                game_ID TEXT,
                roundNumber INTEGER,
                player_name TEXT,
                player_is_pc INTEGER,
                player_cards TEXT,
                player_hand INTEGER,
                player_bet INTEGER,
                house_name TEXT,
                house_visible_card TEXT,
                house_visible_hand INTEGER,
                game_pot INTEGER,
                round_initial_bet INTEGER
            )
        ''')
    CONN.commit()
    C.execute('''
            CREATE TABLE IF NOT EXISTS players_hitStay (
                game_ID TEXT,
                roundNumber INTEGER,
                player_name TEXT,
                player_is_pc INTEGER,
                round_initial_bet INTEGER,
                player_bet INTEGER,
                game_pot INTEGER,
                player_cards TEXT,
                player_hand INTEGER,
                player_bust INTEGER,
                house_name TEXT,
                house_visible_card TEXT,
                house_visible_hand INTEGER,
                player_choice TEXT
            )
        ''')
    CONN.commit()
    



def exit_gracefully():
    os.system('cls')
    print("\n\n\t\t\t\t  <<< EXITING GRACEFULLY >>> \n\n")
    C.close()
    assistant.printWinners(game)
    sys.exit()

def exit_on_key(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            exit_gracefully()
    return wrapper


@exit_on_key
def main():
    """
    DOCSTRING: this is the main program for the game
    """

    os.system('cls')
    global game
    global assistant
    game = Game()
    assistant = GameAssistant()
    print('\n')
    game.newRound(isFirstRound=True)

    while not game.exitGame:
        for player in game.players:
            player.playersTurn(game)
            if game.exitGame:
                break
        else:
            game.house.houseHitStay(game)
        
            os.system('cls')
            game.dealer.payWinners_new(game)
            assistant.printWinners(game)
            stopGame = input("\n\t Do you want to stop? [ Y / (N) ] ")
            game.exitGame = (stopGame[0].lower() in game.affirm_list if not(stopGame == '') else False)
            game.balanceCheck()
            if len(game.players) <= 1:
                game.exitGame = True
            if not game.exitGame:
                game.newRound()
        if game.exitGame:
            break

    os.system('cls')
    
    if (game.roundNumber == 0) and (any(game.players[i].bet == 0 for i in range(len(game.players)))):
        print('\n\t\t\t\t  Sorry to see you go so soon. See you next time \n\n')
    else:
        print('\n\tThank you for playing. The final standing was:')
    
    assistant.printWinners(game)


if __name__=="__main__":
    __createTables()
    main()