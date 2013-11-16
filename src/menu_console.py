import os
from src import constant
from src.config_xml import ConfigXML


class MenuConsole():

    def __init__(self, file_path):
        self.config_xml = ConfigXML(file_path)

    @property
    def menu_options(self):
        return {'1': constant.CONFIGURATION,
                '2': constant.GENERATE_SUDOKU,
                '3': constant.SOLVE_SUDOKU,
                '4': constant.EXIT}

    @property
    def config_options(self):
        return {'1': constant.SET_OUTPUT,
                '2': constant.SET_DIFFICULTY,
                '3': constant.SET_ALGORITHM,
                '4': constant.BACK}

    @property
    def difficulty_levels(self):
        return {'1': constant.EASY,
                '2': constant.MEDIUM,
                '3': constant.HARD,
                '4': constant.CUSTOM,
                '5': constant.BACK}

    @property
    def algorithm_options(self):
        return {'1': constant.ALGORITHM_BACKTRACKING,
                '2': constant.ALGORITHM_NORVING,
                '3': constant.BACK}

    def display_menu_options(self):
        self.print_options_map(self.menu_options)
        option_number = int(raw_input("\nPlease select an option: "))
        menu_function = {'1': self.display_config_options,
                         '2': self.generate_sudoku,
                         '3': self.solve_sudoku,
                         '4': self.exit}
        if 1 <= option_number <= len(self.menu_options):
            function_to_call = menu_function[str(option_number)]
            function_to_call()
        else:
            print "Choose only the options displayed in the menu. Try again"
            self.display_menu_options()

    def display_config_options(self):
        self.print_options_map(self.config_options)
        option_number = int(raw_input("\nPlease select an option: "))
        config_function = {'1': self.set_output,
                           '2': self.display_algorithm_options,
                           '3': self.display_difficulty_levels,
                           '4': self.display_menu_options}
        if 1 <= option_number <= len(self.config_options):
            function_to_call = config_function[str(option_number)]
            function_to_call()
        else:
            print "Choose only the options displayed in the menu. Try again"
            self.display_config_options()

    def generate_sudoku(self):
        pass

    def solve_sudoku(self):
        pass

    def exit(self):
        print "Good Bye!"

    def set_output(self):
        print "Current Output path", self.config_xml.get_node("value", ".//path_output")
        new_output = raw_input("\nPlease enter a new path: ")
        if self.is_valid_path(new_output):
            self.config_xml.set_node("value", ".//path_output", new_output)
        else:
            print "Enter a valid path"
            self.set_output()
        self.display_config_options()

    def is_valid_path(self, path):
        return os.path.isabs(path)

    def display_difficulty_levels(self):
        print "Current Difficulty Level", self.config_xml.get_node("value", ".//difficulty/level")
        self.print_options_map(self.difficulty_levels)
        option_number = int(raw_input("\nPlease select an option: "))
        if 1 <= option_number <= len(self.difficulty_levels):
            if option_number != len(self.difficulty_levels):
                self.config_xml.set_node("value", ".//difficulty/level", self.difficulty_levels[str(option_number)])
            self.display_config_options()
        else:
            print "Choose only the options displayed in the menu. Try again"
            self.display_difficulty_levels()

    def display_algorithm_options(self):
        print "Current Algorithm", self.config_xml.get_node("value", ".//algorithm")
        self.print_options_map(self.algorithm_options)
        option_number = int(raw_input("\nPlease select an option: "))
        if 1 <= option_number <= len(self.algorithm_options):
            if option_number != len(self.algorithm_options):
                self.config_xml.set_node("value", ".//algorithm", self.algorithm_options[str(option_number)])
            self.display_config_options()
        else:
            print "Choose only the options displayed in the menu. Try again"
            self.display_algorithm_options()

    def print_options_map(self, map):
        for key, value in map.iteritems():
            print key, value

    def main_console(self):
        print "################ Sudoku ################"
        self.display_menu_options()

if __name__ == '__main__':
    menuConsole = MenuConsole("../config.xml")
    menuConsole.main_console()
