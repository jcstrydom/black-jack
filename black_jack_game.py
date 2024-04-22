
import os, sys
sys.path.append('./game_display')
from Game import Game
from GameAssistant import GameAssistant

def exit_gracefully():
    print("\n\n\t\t\t\t  <<< EXITING GRACEFULLY >>> \n\n")
    sys.exit()


def exit_on_key(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt or EOFError:
            exit_gracefully()
    return wrapper


@exit_on_key
def main():
    """
    DOCSTRING: this is the main program for the game
    """

    os.system('cls')
    print('\n')
    game = Game()
    assistant = GameAssistant()
    game.newRound(isFirstRound=True)

    while not game.exitGame:
        if game.roundNumber != 0 and game.roundNumber % 2 == 0:
            game.initialBet += 25
        for player in game.players:
            player.playersChoice(game)
            if game.exitGame:
                break
        game.house.houseHitStay(game)
        
        os.system('cls')
        game.dealer.payWinners(game)
        assistant.printWinners(game)
        stopGame = input("\n\t Do you want to stop? [ Y / (N) ] ")
        game.exitGame = (stopGame[0].lower() in game.affirm_list if not(stopGame == '') else False)
        if not game.exitGame:
            game.newRound()
        if game.balanceCheck():
            break


    os.system('cls')
    
    print('\n\tThank you for playing. The final standing was:')
    assistant.printWinners(game)


if __name__=="__main__":
    main()