# Black-Jack

The game follows the standard rules of Black Jack. Players compete against the dealer to get a hand value closest to 21 without going over. Each player starts with two cards, and the dealer reveals one card. Players can choose to hit (draw another card), stand (keep their current hand), or double down (double their bet and receive one more card). The dealer follows a set of rules to determine their final hand.

Please refer to the code and comments in the respective files for more details on the implementation.

Have fun playing Black Jack!

# Core Directory

This directory contains the core functionality of your Black Jack game. It includes the following files:

- `Game.py`: This file contains the `Game` class, which is responsible for managing the game state and flow.
- `Dealer.py`: This file contains the `Dealer` class, which represents the dealer in the game.
- `Player.py`: This file contains the `Player` class, which represents the players in the game.
- `GameAssistant.py`: This file contains the `GameAssistant` class, which assists in managing the game flow and providing prompts to the user.
- `Deck.py`: This file contains the `Deck` class, which represents a deck of cards used in the game.
- `Card.py`: This file contains the `Card` class, which represents a single card in the game.

## Running the Game

To run the game, you have two options:

### Option 1: Using Conda Environment

1. Install Conda by following the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
2. Create a new Conda environment using the `environment.yml` file in the root directory of your project:
   ```shell
   conda env create -f environment.yml
   ```
3. Activate the environment:
   ```shell
   conda activate black-jack
   ```
4. Run the game using the `Game.py` file:
   ```shell
   python core/Game.py
   ```

### Option 2: Using Pip Requirements

1. Install Python and pip if you haven't already.
2. Create a new virtual environment:
   ```shell
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```shell
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```shell
     source venv/bin/activate
     ```
4. Install the required packages using the `requirements.txt` file in the root directory of your project:
   ```shell
   pip install -r requirements.txt
   ```
5. Run the game using the `Game.py` file:
   ```shell
   python core/Game.py
   ```


Thank you for your interest in Black-Jack and I trust that this game will be a fun experience for you!

