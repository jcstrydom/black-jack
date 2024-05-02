import unittest, sys
sys.path.append('./../')
from core.Dealer import Dealer
from core.Player import Player

class TestCalculatePlayerScore(unittest.TestCase):

    def setUp(self):
        """
        Set up the initial state for the test case.

        This function initializes the `dealer` and `player` objects for the test case.
        The `dealer` object is an instance of the `Dealer` class, and the `player` object is an instance of the `Player` class with the name "Test Player".

        Parameters:
        - self: The instance of the test case.

        Returns:
        - None
        """
        self.dealer = Dealer()
        self.player = Player("Test Player")

    

if __name__ == '__main__':
    unittest.main()