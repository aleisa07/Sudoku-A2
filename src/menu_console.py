from src.constant import *
import utils
from src.config_xml import ConfigXML

__author__ = 'Carlos Gonzales'


class MenuConsole():
    def __init__(self):
        """Constructor of MenuConsole class that initialize the ConfigXML class
        in order to read the config.xml"""
        self.config_xml = ConfigXML()

    @property
    def menu_options(self):
        return {'1': MENU_CONFIGURATION,
                '2': MENU_GENERATE_SUDOKU,
                '3': MENU_SOLVE_SUDOKU,
                '4': MENU_EXIT}

    @property
    def config_options(self):
        return {'1': MENU_SET_OUTPUT,
                '2': MENU_SET_DIFFICULTY,
                '3': MENU_SET_ALGORITHM,
                '4': MENU_BACK}

    @property
    def difficulty_levels(self):
        return {'1': LEVEL_EASY,
                '2': LEVEL_MEDIUM,
                '3': LEVEL_HARD,
                '4': LEVEL_CUSTOM,
                '5': MENU_BACK}

    @property
    def algorithm_options(self):
        return {'1': ALGORITHM_BACKTRACKING,
                '2': ALGORITHM_NORVIG,
                '3': MENU_BACK}

    def display_menu_options(self):
        """Method that display the menu options initial by console"""
        utils.print_key_and_values_from_a_dictionary(self.menu_options)
        option_number = int(raw_input(MESSAGE_SELECT_OPTION))
        menu_function = {'1': self.display_config_options,
                         '2': self.generate_sudoku,
                         '3': self.solve_sudoku,
                         '4': self.exit}
        if 1 <= option_number <= len(self.menu_options):
            function_to_call = menu_function[str(option_number)]
            function_to_call()
        else:
            print MESSAGE_SELECT_OPTION_TRY_AGAIN
            self.display_menu_options()

    def display_config_options(self):
        """Method that display the configuration options by console"""
        utils.print_key_and_values_from_a_dictionary(self.config_options)
        option_number = int(raw_input(MESSAGE_SELECT_OPTION))
        config_function = {'1': self.set_output,
                           '2': self.display_algorithm_options,
                           '3': self.display_difficulty_levels,
                           '4': self.display_menu_options}
        if 1 <= option_number <= len(self.config_options):
            function_to_call = config_function[str(option_number)]
            function_to_call()
        else:
            print MESSAGE_SELECT_OPTION_TRY_AGAIN
            self.display_config_options()

    def generate_sudoku(self):
        """Method that generate a sudoku
        Missing integration"""
        pass

    def solve_sudoku(self):
        """Method that solve a sudoku
        Missing integration"""
        pass

    def exit(self):
        print "Good Bye!"

    def set_output(self):
        """Method that set the output path according to new output path
        typed by console"""
        attribute = "value"
        print "Current Output path", self.config_xml.get_node(attribute,
                                                              XPATH_OUTPUT)
        new_output = raw_input("\nPlease enter a new path: ")
        if utils.is_valid_path(new_output):
            if utils.exist_path(new_output):
                self.config_xml.set_node(attribute, XPATH_OUTPUT, new_output)
            else:
                print "The path does not exist"
        else:
            print "Enter a valid path"
            self.set_output()
        self.display_config_options()

    def display_difficulty_levels(self):
        """Method that display the difficulty levels by console"""
        attribute = "value"
        print "Current Difficulty Level", self.config_xml.get_node(attribute,
                                                                   XPATH_LEVEL)
        utils.print_key_and_values_from_a_dictionary(self.difficulty_levels)
        option_number = int(raw_input(MESSAGE_SELECT_OPTION))
        if 1 <= option_number <= len(self.difficulty_levels):
            if option_number != len(self.difficulty_levels):
                self.config_xml.set_node(attribute, XPATH_LEVEL,
                                         self.difficulty_levels[
                                             str(option_number)])
            self.display_config_options()
        else:
            print MESSAGE_SELECT_OPTION_TRY_AGAIN
            self.display_difficulty_levels()

    def display_algorithm_options(self):
        """Method that display the algorithm options by console"""
        attribute = "value"
        print "Current Algorithm", self.config_xml.get_node(attribute,
                                                            XPATH_ALGORITHM)
        utils.print_key_and_values_from_a_dictionary(self.algorithm_options)
        option_number = int(raw_input(MESSAGE_SELECT_OPTION))
        if 1 <= option_number <= len(self.algorithm_options):
            if option_number != len(self.algorithm_options):
                self.config_xml.set_node(attribute, XPATH_ALGORITHM,
                                         self.algorithm_options[
                                             str(option_number)])
            self.display_config_options()
        else:
            print MESSAGE_SELECT_OPTION_TRY_AGAIN
            self.display_algorithm_options()


if __name__ == '__main__':
    menuConsole = MenuConsole()
    print "################ Sudoku ################"
    menuConsole.display_menu_options()
