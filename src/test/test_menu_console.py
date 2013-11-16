import unittest
from src import constant
from src.menu_console import MenuConsole


class TestMenuConsole(unittest.TestCase):

    menu_console = MenuConsole("../../config.xml")

    def test_verify_that_the_menu_option_contains_default_options(self):
        menu_options = {'1': constant.CONFIGURATION, '2': constant.GENERATE_SUDOKU,
                        '3': constant.SOLVE_SUDOKU, '4': constant.EXIT}
        shared_items = set(menu_options.items()) & set(self.menu_console.menu_options.items())
        self.assertEqual(len(menu_options), len(shared_items))

    def test_verify_that_the_config_option_contains_default_options(self):
        config_options = {'1': constant.SET_OUTPUT, '2': constant.SET_DIFFICULTY,
                          '3': constant.SET_ALGORITHM, '4': constant.BACK}
        shared_items = set(config_options.items()) & set(self.menu_console.config_options.items())
        self.assertEqual(len(config_options), len(shared_items))

    def test_verify_that_the_difficulty_levels_contains_default_options(self):
        difficulty_levels = {'1': constant.EASY, '2': constant.MEDIUM, '3': constant.HARD,
                             '4': constant.CUSTOM, '5': constant.BACK}
        shared_items = set(difficulty_levels.items()) & set(self.menu_console.difficulty_levels.items())
        self.assertEqual(len(difficulty_levels), len(shared_items))

    def test_verify_that_the_algorithm_options_contains_default_options(self):
        algorithm_options = {'1': constant.ALGORITHM_BACKTRACKING, '2': constant.ALGORITHM_NORVING, '3': constant.BACK}
        shared_items = set(algorithm_options.items()) & set(self.menu_console.algorithm_options.items())
        self.assertEqual(len(algorithm_options), len(shared_items))

    def test_verify_if_a_path_is_valid(self):
        path = "c:\\test"
        self.assertTrue(self.menu_console.is_valid_path(path))

    def test_verify_if_a_path_is_not_valid(self):
        path = "testing?"
        self.assertFalse(self.menu_console.is_valid_path(path))


if __name__ == '__main__':
    unittest.main()