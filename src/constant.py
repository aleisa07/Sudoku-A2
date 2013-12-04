# Menus to display for console
MENU_CONFIGURATION = 'Configuration'
MENU_GENERATE_SUDOKU = 'Generate Sudoku'
MENU_SOLVE_SUDOKU = 'Solve Sudoku'
MENU_EXIT = 'Exit'
MENU_SET_OUTPUT = 'Set output'
MENU_SET_DIFFICULTY = 'Set difficulty'
MENU_SET_ALGORITHM = 'Set Algorithm to solve'
MENU_BACK = 'Back'

# Messages to display for console
MESSAGE_SELECT_OPTION = "\nPlease select an option: "
MESSAGE_SELECT_OPTION_TRY_AGAIN = "Choose only the options displayed in the menu. Try again."
MESSAGE_INVALID_POSITION = "Invalid position in Sudoku. "

# Range of hint cells by level
TOP = "TOP"
BOTTOM = "BOTTOM"
EASY_VALUES = {BOTTOM: 30, TOP: 40}
MEDIUM_VALUES = {BOTTOM: 40, TOP: 60}
HARD_VALUES = {BOTTOM: 60, TOP: 70}

LEVEL_EASY = 	'Easy'
LEVEL_MEDIUM = 	'Medium'
LEVEL_HARD = 	'Hard'
# Levels
LEVEL = {LEVEL_EASY: 	EASY_VALUES,
		 LEVEL_MEDIUM : MEDIUM_VALUES,
		 LEVEL_HARD :	HARD_VALUES}

# Levels
LEVEL_EASY = 'Easy'
LEVEL_MEDIUM = 'Medium'
LEVEL_HARD = 'Hard'
LEVEL_CUSTOM = 'Custom'

LEVEL = {LEVEL_EASY:    EASY_VALUES,
         LEVEL_MEDIUM:  MEDIUM_VALUES,
         LEVEL_HARD:    HARD_VALUES}

# Algorithm to solve a Sudoku
ALGORITHM_BACKTRACKING = 'BackTracking'
ALGORITHM_NORVIG = 'Norvig'

MAP_ROW = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F",
           6: "G", 7: "H", 8: "I"}
# Xpath locator to get values of the config.xml

# Dictionary of rows
MAP_ROW = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I"}

# Xpath locator to get values of the config.xml
XPATH_OUTPUT = ".//path_output"
XPATH_ALGORITHM = ".//algorithm"
XPATH_LEVEL = ".//difficulty/level"
XPATH_HOLES_NUMBER = ".//difficulty/level/limits_holes"

# Operations
SET = "Set"
HIDE = "Hide"
HINT = "Hint"

