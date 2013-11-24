from collections import OrderedDict
from src.algorithm_base import AlgorithmBase
from src.sudoku_matrix import SudokuMatrix
import utils


class AlgorithmNorvig(AlgorithmBase):

    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.list_squares = utils.cross(self.rows, self.cols)
        self.unit_list = ([utils.cross(self.rows, c) for c in self.cols] +
                          [utils.cross(r, self.cols) for r in self.rows] +
                          [utils.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
                           for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unit_list if s in u]) for s in
                          self.list_squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in
                          self.list_squares)

    def solve(self, sudoku_matrix):
        dictionary_sudoku = self.convert_matrix_to_dict(sudoku_matrix)
        dict_sudoku_solved = self.search(self.parse_grid(dictionary_sudoku))
        return self.convert_dict_to_matrix(dict_sudoku_solved)

    def convert_matrix_to_dict(self, sudoku_matrix):
        sudoku_dictionary = dict()
        for row in range(9):
            for column in range(9):
                key = self.rows[row] + self.digits[column]
                value = sudoku_matrix.get_cell(row, column).get_cell_value()
                sudoku_dictionary[key] = str(value)
        order_map = OrderedDict(
            sorted(sudoku_dictionary.items(), key=lambda t: t[0]))
        return order_map

    def convert_dict_to_matrix(self, sudoku_dict):
        sudoku_matrix = SudokuMatrix()
        i = 0
        for row in self.rows:
            j = 0
            for col in self.cols:
                sudoku_matrix.set_cell_value(i, j, sudoku_dict[row + col])
                j += 1
            i += 1
        return sudoku_matrix

    def parse_grid(self, grid):
        """Convert grid to a dict of possible values, {square: digits}, or
        return False if a contradiction is detected."""
        # To start, every square can be any digit;
        # then assign values from the grid.
        dict_values_possible = dict(
            (key, self.digits) for key in self.list_squares)
        for key, value in grid.items():
            if value in self.digits and not self.assign(dict_values_possible,
                                                        key, value):
                return False # (Fail if we can't assign d to square s.)
        return dict_values_possible

    ######## Search ########

    def search(self, dict_values):
        """Using depth-first search and propagation, try all possible values"""
        if dict_values is False:
            return False  # Failed earlier
        if all(len(dict_values[key]) == 1 for key in self.list_squares):
            return dict_values  # Solved!
            # Chose the unfilled square s with the fewest possibilities
        n, s = min((len(dict_values[key]), key) for key in self.list_squares if
                   len(dict_values[key]) > 1)
        return utils.some(
            self.search(self.assign(dict_values.copy(), s, d)) for d in
            dict_values[s])

    ######## Constraint Propagation ########

    def assign(self, dict_values, s, d):
        """Eliminate all the other values (except d) from values[s] and propagate.
        Return values, except return False if a contradiction is detected."""
        other_values = dict_values[s].replace(d, '')
        if all(self.eliminate(dict_values, s, d2) for d2 in other_values):
            return dict_values
        else:
            return False

    def eliminate(self, dict_values, s, d):
        """Eliminate d from values[s]; propagate when values or places <= 2.
        Return values, except return False if a contradiction is detected."""
        if d not in dict_values[s]:
            return dict_values  # Already eliminated
        dict_values[s] = dict_values[s].replace(d, '')
        # (1) If a square s is reduced to one value d2, then eliminate d2
        # from the peers.
        if len(dict_values[s]) == 0:
            return False  # Contradiction: removed last value
        elif len(dict_values[s]) == 1:
            d2 = dict_values[s]
            if not all(self.eliminate(dict_values, s2, d2) for s2 in
                       self.peers[s]):
                return False
                # (2) If a unit u is reduced to only one place for a value d,
                # then put it there.
        for u in self.units[s]:
            dplaces = [s for s in u if d in dict_values[s]]
            if len(dplaces) == 0:
                return False  # Contradiction: no place for this value
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.assign(dict_values, dplaces[0], d):
                    return False
        return dict_values

    ######## Display as 2-D grid ########

    def display(self, sudoku_matrix):
        """Display these values as a 2-D grid."""
        dict_values = self.convert_matrix_to_dict(sudoku_matrix)
        width = 1 + max(len(dict_values[s]) for s in self.list_squares)
        line = '+'.join(['-' * (width * 3)] * 3)
        for r in self.rows:
            print ''.join(
                dict_values[r + c].center(width) + ('|' if c in '36' else '')
                for c in self.cols)
            if r in 'CF':
                print line
        print