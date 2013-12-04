import random
from cell import Cell
from constant import *
from generator import Generator
from input_file import Input
import copy


class SudokuMatrix():

    dificult = LEVEL_EASY

    def __init__(self, source=None):
        """Set the sudoku matrix with values generated or load from txt or csv files

        Keyword arguments:
        source        --     path of file to read and load a sudoku matrix
        """
        self.sudoku_matrix = []

        if (source == None):
            generator = Generator()
            dificult = self.get_cells_to_hide(self.dificult)
            self.sudoku_matrix = generator.get_matrix()
            self.sudoku_matrix_solved = copy.copy(self.sudoku_matrix)
            self.hide_values_in_matrix(dificult)
        else:
            by_file = Input(source)
            self.sudoku_matrix = by_file.get_matrix_by_file()

    def set_sudoku_matrix(self, matrix):
        """Set a new sudoku matrix with new matrix

        Keyword arguments:
        matrix    --    New matrix to set as default matrix
        """
        self.sudoku_matrix = matrix

    def get_cell(self, row, column):
        """Return the Cell object in the row and column position

        Keyword arguments:
        row     --    X Axis position in the Sudoku matrix
        column  --    Y Axis position in the Sudoku matrix

        Return  --    Cell Object 
        """
        return self.sudoku_matrix[row][column]

    def set_cell_value(self, row, column, value):
        """Set with new value Cell object in the row and column position

        Keyword arguments:
        row     --    X Axis position in the Sudoku matrix
        column  --    Y Axis position in the Sudoku matrix
        value   --    Value in the Cell object
        """
        self.sudoku_matrix[row][column].set_cell_value(value)

    def get_row(self, row):
        """Return a row specific from matrix"""
        
        return self.sudoku_matrix[row]

    def print_sudoku_matrix(self):
        """Print the sudoku matrix in the console
        """
        for row in range(len(self.sudoku_matrix)):
            var = ""
            for column in range(9):
                if (self.sudoku_matrix[row][column].get_cell_visibility() == True):
                    var = var + '\t' + "."
                else:
                    var = var + '\t' + str(self.sudoku_matrix[row][column].get_cell_value())
            print (var)

    def hide_values_in_matrix(self, dificult):
        """Hide cell in the Sudoku Matrix 

        Keyword arguments:
        dificult   --   Number of cells to hide in the sudoku matrix
        """
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if (dificult != 0):
            self.sudoku_matrix[row][column].set_cell_visibility(True)
            self.sudoku_matrix[row][column].set_cell_value(0)
            self.hide_values_in_matrix(dificult - 1)
        else:
            pass

    def get_cells_to_hide(self, level):
        """Return the number of cells to hide in the sudoku matrix

        Keyword arguments:
        level   --      Level of sudoku game it can be "Easy", "Medium", "Hard"
        return  --      Number of cells to hide
        """
        level = LEVEL[level]
        bottom = level[BOTTOM]
        top = level[TOP]
        return random.randint(bottom, top)

    def get_sudoku_matrix(self):
        """Return a sudoku matrix 
        """
        return self.sudoku_matrix

    def get_sudoku_matrix_solved(self):
        """Return a sudoku matrix solved
        """
        return self.sudoku_matrix_solved

    def __eq__(self, other):
        equals = False
        for row in range(9):
            for col in range(9):
                if int(self.get_cell(row, col).get_cell_value()) == int(
                        other.get_cell(row, col).get_cell_value()):
                    equals = True
                else:
                    return False
        return equals


if __name__ == "__main__":
    print("    -----------FROM GENERATOR--------")
    generator = SudokuMatrix()
    generator.print_sudoku_matrix()
    print("    -----------FROM CSV FILE---------")
    csv = SudokuMatrix("../input_files/file.csv")
    csv.print_sudoku_matrix()
    print("    -----------FROM TXT FILE---------")
    txt = SudokuMatrix("../input_files/file.txt")
    txt.print_sudoku_matrix()



    


