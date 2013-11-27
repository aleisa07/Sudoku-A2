import unittest
from src.constant import *
from src.menu_console import MenuConsole


class TestMenuConsole(unittest.TestCase):

    def setUp(self):
        self.menu_console = MenuConsole()

    def test_verify_that_the_menu_option_contains_default_options(self):
        menu_options = {'1': MENU_CONFIGURATION, '2': MENU_GENERATE_SUDOKU,
                        '3': MENU_SOLVE_SUDOKU, '4': MENU_EXIT}
        shared_items = set(menu_options.items()) & set(
            self.menu_console.menu_options.items())
        self.assertEqual(len(menu_options), len(shared_items))

    def test_verify_that_the_config_option_contains_default_options(self):
        config_options = {'1': MENU_SET_OUTPUT, '2': MENU_SET_DIFFICULTY,
                          '3': MENU_SET_ALGORITHM, '4': MENU_BACK}
        shared_items = set(config_options.items()) & set(
            self.menu_console.config_options.items())
        self.assertEqual(len(config_options), len(shared_items))

    def test_verify_that_the_difficulty_levels_contains_default_options(self):
        difficulty_levels = {'1': LEVEL_EASY, '2': LEVEL_MEDIUM,
                             '3': LEVEL_HARD,
                             '4': LEVEL_CUSTOM, '5': MENU_BACK}
        shared_items = set(difficulty_levels.items()) & set(
            self.menu_console.difficulty_levels.items())
        self.assertEqual(len(difficulty_levels), len(shared_items))

    def test_verify_that_the_algorithm_options_contains_default_options(self):
        algorithm_options = {'1': ALGORITHM_BACKTRACKING,
                             '2': ALGORITHM_NORVIG, '3': MENU_BACK}
        shared_items = set(algorithm_options.items()) & set(
            self.menu_console.algorithm_options.items())
        self.assertEqual(len(algorithm_options), len(shared_items))

if __name__ == '__main__':
    unittest.main()