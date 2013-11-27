import random
from cell import Cell
from constant import *
from generator import Generator
from input_file import Input

class SudokuMatrix():

    sudoku_matrix = [[]]
    file_to_load = None
    dificult = LEVEL_EASY

    def __init__(self, source = None):
        """Set the sudoku matrix with values generated or load from txt or csv files"""
        self.sudoku_matrix = [[]]
        if (source == None):
            generator= Generator()
            dificult = self.get_cells_to_hide(self.dificult)
            self.sudoku_matrix = generator.get_matrix()
            self.hide_values_in_matrix(dificult)
        else:
            by_file = Input(source)
            self.sudoku_matrix = by_file.get_matrix_by_file()
        
    def get_cell(self, row, column):
        """Return the Cell object in the row and column position

        Keyword arguments:
        row     --    X Axis position in the matrix
        column  --    Y Axis position in the matrix

        Return  --    Cell Object 
        """
        return self.matrix[row][column]

    def set_cell_value(self, row, column, value):
        """Set with new value Cell object in the row and column position

        Keyword arguments:
        row     --    X Axis position in the matrix
        column  --    Y Axis position in the matrix
        value   --    Value in the Cell object
        """
        self.matrix[row][column].set_cell_value(value)

    def get_row(self, row):
        """Return a row specific from matrix"""
        return self.matrix[row]
    
    def print_sudoku_matrix(self):
        """Print the sudoku matrix in the console
        """
        for row in range(9):
            var = ""
            for column in range(9):
                if (self.sudoku_matrix[row][column].get_cell_visibility() == False):
                    var = var + '\t' + "."
                else:
                    var = var + '\t' + str(self.sudoku_matrix[row][column].get_cell_value())
            print (var)

    def hide_values_in_matrix(self, dificult):
        """Hide cell in the Matrix 

        Keyword arguments:
        dificult   --   Number of cells to hide in the matrix
        """
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if (dificult != 0):
            self.sudoku_matrix[row][column].set_cell_visibility(False)
            self.sudoku_matrix[row][column].set_cell_value(0)
            self.hide_values_in_matrix(dificult - 1)
        else:
            pass 

    def get_cells_to_hide(self, level):
        """Return the number of cells to hide in the matrix

        Keyword arguments:
        level   --      Level of sudoku game it can be "Easy", "Medium", "Hard"
        return  --      Number of cells to hide
        """
        level = LEVEL[level]
        bottom = level[BOTTOM]
        top = level[TOP]
        return random.randint(bottom, top)

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



    


