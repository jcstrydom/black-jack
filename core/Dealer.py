import random
import os
from core.Deck import Deck


class Dealer():
    def __init__(self):
        """
        Initializes the Dealer object.
        
        Returns:
            None
        """
        print('\n\tNew dealer in the game...')
        self.pot = 0
        self.deck = Deck()
        self.shuffleCards()


    def newRound(self):
        """
        Initializes a new round of the game by calling the __init__ method of the Dealer class.

        This method is responsible for resetting the state of the Dealer object for a new round of the game.
        It does so by calling the __init__ method of the Dealer class.

        Parameters:
            self (Dealer): The Dealer object.

        Returns:
            None
        """
        self.__init__()


    def shuffleCards(self):
        """
        Shuffles the cards in the deck.

        This function shuffles the cards in the deck by using the `random.shuffle()` function. 
        It takes no parameters and does not return anything.

        Parameters:
            None

        Returns:
            None
        """
        print('\tDealer shuffled the cards...')
        random.shuffle(self.deck.pack)


    def dealCards(self,players):
        """
        A function to deal cards to players.

        Parameters:
            self: the object itself
            players (list): A list of Player objects to deal cards to.

        Returns:
            None
        """
        
        ## Just dealing the initial two cards per person
        for j in range(0,2):
            for player in players:
                print(f"\t\t{player.name}'s {j+1} card is dealt...")
                player.cards.append(self.deck.pack.pop(0))
                self.calculatePlayerHand(player)

    def calculatePlayerHand(self,player):
        """
        Calculate the score of a player's hand of cards.

        Parameters:
            player (Player): The player whose score is being calculated.

        Returns:
            None

        This function calculates the score of a player's hand of cards by iterating over each card in the player's hand.
        It checks the value of each card and updates the player's hand and aces accordingly.
        
        If the player's hand exceeds 21, and the player has an ace in their hand, it adjusts the player's hand by subtracting 10 from it for each ace,
        until the player's hand is less than or equal to 21, or the number of tries exceeds the number of aces.

        Finally, If the player's hand is still greater than 21 after adjusting for all aces, the player's bust attribute is set to True.

        """
        player.hand = 0
        player.aces = 0
        player.bust = False
        for c in player.cards:
            card_value = c.split(' ')[1]
            if card_value.lower() == 'a':
                player.aces += 1
            # os.system('clear')
            player.hand += self.deck.cardPoints[card_value]
        
        # input('-'*40 + f"\n{player.name.upper()} ACES = {player.aces}\n" + '-'*40)
        reset_tries = 0
        while player.hand > 21:
            if reset_tries < player.aces and player.aces > 0:
                reset_tries += 1
                player.hand -= 10
            else:
                player.bust = True
                break


    def addCard(self,player):
        """
        Add a card to the player's hand and calculate the player's score.

        Parameters:
            self: the object itself
            player (Player): The player to add the card to.

        Returns:
            None
        """
        player.cards.append(self.deck.pack.pop(0))
        self.calculatePlayerHand(player)


    def payWinners(self,game):
        """
        Determines the winners of the game and distributes the pot among them.

        Parameters:
            self: The object itself.
            game: An instance of the Game class representing the current game state.

        Returns:
            None
        """
        winners = []
        number_of_winners = 0
        # print(f"{game.dealer.pot=}")
        if game.house.bust:
            # print("House busts...")
            for i in game.players:
                if not i.bust:
                    i.won = True
                    number_of_winners += 1
                    winners.append(i.name)
        else:
            for i in game.players:
                if (not i.bust) and (i.hand > game.house.hand):
                    i.won = True
                    winners.append(i.name)
                    number_of_winners += 1

        if number_of_winners > 0:
            # print(f"{number_of_winners} winners: {winners}")
            per_winner_winnings = int(game.dealer.pot / float(number_of_winners))
            # print(f"{per_winner_winnings=}")
            for i in game.players:
                if i.won:
                    i.winnings[game.roundNumber] = per_winner_winnings
                    i.balance += i.winnings[game.roundNumber]
                    # print(f"{i.name} won {i.winnings[game.roundNumber]}")

        if number_of_winners == 0:
            # print(f"{number_of_winners} winners: {winners}")
            game.house.won = True
            game.house.winnings[game.roundNumber] = game.dealer.pot
            winners = [game.house.name]
            # print(f"{game.house.name} won {game.house.winnings[game.roundNumber]}")

        # if len(winners)>0:
        #     print(f"'winners' [{type(winners)}] of [{type(winners[0])}] = {winners}")

        game.winners[game.roundNumber] = winners
        # print(f"\n Winners = {game.winners[game.roundNumber]}")


    def payWinners_new(self,game):
        """
        Determines the winners of the game and distributes the pot among them.

        Parameters:
            self: The object itself.
            game: An instance of the Game class representing the current game state.

        Returns:
            None
        """
        winners = []
        number_of_winners = 0
        house_winnings = 0

        if game.house.bust:
            # print("House busts...")
            for i in game.players:
                if not i.bust:
                    i.won = True
                    multiplier = 2.5 if ((len(i.cards) == 2) and (i.hand == 21)) else 2
                    i.balance += i.bet*multiplier
                    i.winnings[game.roundNumber] = i.bet*multiplier
                    winners.append(i.name)
                    number_of_winners += 1
                else:
                    house_winnings += i.bet
        else:
            for i in game.players:
                if (not i.bust) and (i.hand >= game.house.hand):
                    i.won = True if (i.hand > game.house.hand) else False
                    multiplier = 2.5 if ((len(i.cards) == 2) and (i.hand == 21) and (i.hand > game.house.hand)) else 1 if (i.hand == game.house.hand) else 2
                    i.balance += i.bet*multiplier
                    i.winnings[game.roundNumber] = i.bet*multiplier
                    winners.append(i.name)
                    if i.hand > game.house.hand:
                        number_of_winners += 1
                else:
                    house_winnings += i.bet

        if number_of_winners == 0:
            # print(f"{number_of_winners} winners: {winners}")
            game.house.won = True
            game.house.winnings[game.roundNumber] = house_winnings
            winners = [game.house.name]
            # print(f"{game.house.name} won {game.house.winnings[game.roundNumber]}")

        # if len(winners)>0:
        #     print(f"'winners' [{type(winners)}] of [{type(winners[0])}] = {winners}")

        game.winners[game.roundNumber] = winners
        # print(f"\n Winners = {game.winners[game.roundNumber]}")


                
                    

        
