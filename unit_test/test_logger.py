import unittest
import sys
sys.path.append('../src')

from logger import LoggerManager
from constant import *

__author__ = 'carlos^gonzales'


class TestLogger(unittest.TestCase):

    def setUp(self):
        player_name = "Player 1"
        self.sudoku_game_log = LoggerManager(player_name)

    def test_logging_a_set_cell(self):
        set_cell = SET + " A 1 6"
        self.sudoku_game_log.info(set_cell)
        text = self.sudoku_game_log.get_log()
        self.assertTrue(set_cell in text)

    def test_logging_a_hide_cell(self):
        hint_cell = HIDE + " B 3"
        self.sudoku_game_log.info(hint_cell)
        text = self.sudoku_game_log.get_log()
        self.assertTrue(hint_cell in text)

    def test_logging_a_hint_cell(self):
        hint_cell = HINT + " A 9"
        self.sudoku_game_log.info(hint_cell)
        text = self.sudoku_game_log.get_log()
        self.assertTrue(hint_cell in text)

    def test_logging_a_set_invalid_cell(self):
        invalid_cell = MESSAGE_INVALID_POSITION + " H 10 6"
        self.sudoku_game_log.error(invalid_cell)
        text = self.sudoku_game_log.get_log()
        self.assertTrue(invalid_cell in text)

    def tearDown(self):
        print "first " + self.sudoku_game_log.get_log()
        self.sudoku_game_log.clear_log()
        print "finally " + self.sudoku_game_log.get_log()

if __name__ == '__main__':
    unittest.main()
