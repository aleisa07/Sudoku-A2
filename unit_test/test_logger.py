import unittest
import sys
sys.path.append('../src')

from logger import LoggerManager
from constant import *

__author__ = 'carlos^gonzales'


class TestLogger(unittest.TestCase):

    def setUp(self):
        log_id_name = "Player 1"
        self.sudoku_log = LoggerManager(log_id_name)

    def test_verify_that_is_possible_to_log_an_info_message(self):
        set_cell = SET + " A 1 6"
        self.sudoku_log.info(set_cell)
        text = self.sudoku_log.get_log()
        self.assertTrue(set_cell in text)

    def test_verify_that_is_possible_to_log_an_error_message(self):
        invalid_cell = MESSAGE_INVALID_POSITION + " H 10 6"
        self.sudoku_log.error(invalid_cell)
        text = self.sudoku_log.get_log()
        self.assertTrue(invalid_cell in text)

    def test_verify_that_is_possible_to_clear_a_log(self):
        self.sudoku_log.clear_log()
        text = self.sudoku_log.get_log()
        self.assertTrue(not text)

    def tearDown(self):
        self.sudoku_log.clear_log()

if __name__ == '__main__':
    unittest.main()
