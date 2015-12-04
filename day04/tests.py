'''
Created on Dec 4, 2015

@author: jose.fernandez
'''
import unittest
from day04.main import find_minimum_number_for_md5


class Test(unittest.TestCase):

    def test_avent_coins_default(self):
        self.assertEqual(609043, find_minimum_number_for_md5("abcdef"))

    def test_avent_coins_final(self):
        self.assertEqual(1048970, find_minimum_number_for_md5("pqrstuv"))

    def test_avent_coins_answer(self):
        self.assertEqual(254575, find_minimum_number_for_md5("bgvyzdsv"))

if __name__ == "__main__":
    unittest.main()
