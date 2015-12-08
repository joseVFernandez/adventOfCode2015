'''
Created on Dec 4, 2015

@author: jose.fernandez
'''
import unittest
from day07.main import Logic_board


class Test(unittest.TestCase):

    def setUp(self):
        self.logic_board = Logic_board()

    def tearDown(self):
        self.logic_board = None

    def test_default_decoration(self):
        self.assertEquals(0,
                          self.logic_board.method())


if __name__ == "__main__":
    unittest.main()
