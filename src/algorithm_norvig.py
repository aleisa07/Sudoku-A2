from collections import OrderedDict
from src.algorithm_base import AlgorithmBase
from src.sudoku_matrix import SudokuMatrix
import utils


class AlgorithmNorvig(AlgorithmBase):
    def __init__(self):
        """Constructor of the Algorithm Norvig that initialize the variables
        used in the resolution of a Sudoku
        """
        self.digit_list = '123456789'
        self.row_list = 'ABCDEFGHI'
        self.column_list = self.digit_list
        self.list_squares = utils.cross(self.row_list, self.column_list)
        self.unit_list = (
            [utils.cross(self.row_list, column) for column in
             self.column_list] +
            [utils.cross(row, self.column_list) for row in self.row_list] +
            [utils.cross(rows, columns) for rows in ('ABC', 'DEF', 'GHI')
             for columns in ('123', '456', '789')])
        self.unit_dict_squares = dict(
            (square, [unit for unit in self.unit_list if square in unit]) for
            square in self.list_squares)
        self.peers_set_squares = dict((square, set(
            sum(self.unit_dict_squares[square], [])) - set([square])) for
            square in self.list_squares)

    def solve(self, sudoku_matrix):
        """
        Return a solved Sudoku Matrix object using the algorithm Norvig

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object withou solution

        """
        dictionary_sudoku = self.convert_matrix_to_dict(sudoku_matrix)
        dict_sudoku_solved = self.search(
            self.get_dict_values_possible(dictionary_sudoku))
        return self.convert_dict_to_matrix(dict_sudoku_solved)

    def convert_matrix_to_dict(self, sudoku_matrix):
        """
        Method that convert a Sudoku Matrix object to a dictionary

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        sudoku_dictionary = dict()
        for row in range(9):
            for column in range(9):
                key = self.row_list[row] + self.digit_list[column]
                value = sudoku_matrix.get_cell(row, column).get_cell_value()
                sudoku_dictionary[key] = str(value)
        order_map = OrderedDict(
            sorted(sudoku_dictionary.items(), key=lambda t: t[0]))
        return order_map

    def convert_dict_to_matrix(self, sudoku_dict):
        """
        Method that convert a dictionary to a Sudoku Matrix object

        Keyword arguments:
        sudoku_dict -- dictionary of square of a sudoku

        """
        sudoku_matrix = SudokuMatrix()
        row_i = 0
        for row in self.row_list:
            column_j = 0
            for col in self.column_list:
                sudoku_matrix.set_cell_value(row_i, column_j,
                                             sudoku_dict[row + col])
                column_j += 1
            row_i += 1
        return sudoku_matrix

    def get_dict_values_possible(self, dict_values):
        """Convert a sudoku dict values to a dict of possible values,
        {square: digits}, or return False if a contradiction is detected.

        Keyword arguments:
        dict_values -- dictionary of square of a sudoku

        """
        # To start, every square can be any digit;
        # then assign values from the sudoku dict values.
        dict_values_possible = dict(
            (key, self.digit_list) for key in self.list_squares)
        for key, value in dict_values.items():
            if value in self.digit_list and not self.assign(
                    dict_values_possible,
                    key, value):
                return False  # (Fail if we can't assign value to square.)
        return dict_values_possible

    def search(self, dict_values):
        """Using depth-first search and propagation, try all possible values

        Keyword arguments:
        dict_values -- dictionary of square of a sudoku

        """
        if dict_values is False:
            return False  # Failed earlier
        if all(len(dict_values[key]) == 1 for key in self.list_squares):
            return dict_values  # Solved!

        # Choose the unfilled square key with the fewest possibilities
        number, key = min(
            (len(dict_values[key]), key) for key in self.list_squares if
            len(dict_values[key]) > 1)

        return utils.get_element_exists_in_sequence(
            self.search(self.assign(dict_values.copy(), key, value)) for value
            in dict_values[key])

    def assign(self, dict_values, key, value):
        """Eliminate all the other values (except value) from values[key]
        and propagate.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        dict_values -- copy of the dictionary of square of a sudoku
        key -- key of a unfilled square with the fewest possibilities
        value -- a value of dict_values

        """
        other_values = dict_values[key].replace(value, '')
        if all(self.eliminate(dict_values, key, other_value) for other_value in
               other_values):
            return dict_values
        else:
            return False

    def eliminate(self, dict_values, key, value):
        """Eliminate value from values[key];
        propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected.

        Keyword arguments:
        dict_values -- dictionary of square of a sudoku
        key -- key chose of the unfilled square with the fewest possibilities
        value -- a value

        """
        if value not in dict_values[key]:
            return dict_values  # Already eliminated
        dict_values[key] = dict_values[key].replace(value, '')
        # (1) If a square key is reduced to one other_value,
        # then eliminate other_value from the peers.
        if len(dict_values[key]) == 0:
            return False  # Contradiction: removed last value
        elif len(dict_values[key]) == 1:
            other_value = dict_values[key]
            if not all(self.eliminate(dict_values, other_key, other_value) for
                       other_key in self.peers_set_squares[key]):
                return False
        return self.get_dict_values_reduced_to_only_one_place(dict_values, key,
                                                              value)

    def get_dict_values_reduced_to_only_one_place(self, dict_values, key,
                                                  value):
        """Get the dictionary of values reduced to only one place

        Keyword arguments:
        dict_values -- dictionary of square of a sudoku
        key -- key chose of the unfilled square with the fewest possibilities
        value -- a value

        """
        # (2) If a unit u is reduced to only one place for a value,
        # then put it there.
        for unit in self.unit_dict_squares[key]:
            value_places = [key for key in unit if value in dict_values[key]]
            if len(value_places) == 0:
                return False  # Contradiction: no place for this value
            elif len(value_places) == 1:
                # value can only be in one place in unit; assign it there
                if not self.assign(dict_values, value_places[0], value):
                    return False
        return dict_values


