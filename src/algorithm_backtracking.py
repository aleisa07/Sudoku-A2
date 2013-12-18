from algorithm_base import AlgorithmBase
from sudoku_matrix import SudokuMatrix
from algorithm_solver import time_decorator


class Backtracking(AlgorithmBase):
    def __init__(self):
        """
        Constructor of Algorithm Backtracking that initializes the matrix used to resolve Sudoku
        """
        self.matrix = None

    @time_decorator
    def solve(self, sudoku_matrix):
        """
        Return a solved Sudoku Matrix object using the algorithm Backtracking

        keyword arguments 
        sudoku_matrix -- Sudoku Matrix object without solution
        """
        self.matrix = sudoku_matrix.sudoku_matrix
        self.solve_in_line(0, 0)
        sudoku_matrix = SudokuMatrix()
        sudoku_matrix.set_sudoku_matrix(self.matrix)
        return sudoku_matrix   

    def solve_in_line(self, row, col):
        """
        Recursive method in order to go over the matrix

        keyword arguments 
        row -- Number of row of the matrix
        col -- Number of column of the matrix
        """
        if col >= 9:
            col = 0
            row += 1
            if row >= 9:
                return True

        if int(self.matrix[row][col].get_cell_value()) != 0:
            return self.solve_in_line(row, (col + 1))

        for cell_value in range(1, 10):
            if self.is_valid_value(row, col, cell_value):
                self.matrix[row][col].set_cell_value(cell_value)
                if self.solve_in_line(row, (col + 1)):
                    return True
        (self.matrix[row][col]).set_cell_value(0)
        return False

    def is_valid_value(self, row, col, cell_value):
        """
        Validate if the value to use is valid, validating the column, the row and the square

        keyword arguments 
        row -- Number of row of the matrix
        col -- Number of column of the matrix
        cell_value -- the candidate value in order to set in the matrix after evaluating in the
        column, row and square
        """
        col_val = self.is_valid_value_in_column(col, cell_value)
        row_val = self.is_valid_value_in_row(row, cell_value)
        squa_val = self.is_valid_value_in_square(row, col, cell_value)

        if col_val and row_val and squa_val:
            return True
        else:
            return False

    def is_valid_value_in_column(self, col, cell_value):
        """
        Validate if the value to use is valid in the column

        keyword arguments 
        row -- Number of row of the matrix
        col -- Number of column of the matrix
        cell_value -- the candidate value in order to set in the matrix
        """
        for i in range(9):
            if cell_value == self.matrix[i][col].get_cell_value():
                return False
        return True

    def is_valid_value_in_row(self, row, cell_value):
        """
        Validate if the value to use is valid in the row

        keyword arguments 
        row -- Number of row of the matrix
        col -- Number of column of the matrix
        cell_value -- the candidate value in order to set in the matrix
        """
        for j in range(9):
            if cell_value == self.matrix[row][j].get_cell_value():
                return False
        return True

    def is_valid_value_in_square(self, row, col, cell_value):
        """
        Validate if the value to use is valid in the square

        keyword arguments 
        row -- Number of row of the matrix
        col -- Number of column of the matrix
        cell_value -- the candidate value in order to set in the matrix
        """
        row_offset = (row / 3) * 3
        col_offset = (col / 3) * 3
        for i in range(3):
            for j in range(3):
                if cell_value == \
                        (self.matrix[row_offset + i][col_offset + j]).get_cell_value():
                    return False
        return True