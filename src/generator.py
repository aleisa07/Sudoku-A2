import random
from cell import Cell
from constant import MAP_ROW
import utils


class Generator():

    def __init__(self):
        """This class generate a matrix 9x9 with Cell Objects"""

        self.generate_matrix()

    def generate_matrix(self):
        """ Fill the matrix with cell objects"""
        self.matrix = []
        pivot = utils.generate_random_number()
        self.matrix.append(self.generate_row(pivot, 0))
        for row in range(8):
            if (row == 2 or row ==5):
                while self.exist_number_in_column(pivot):
                    pivot = utils.generate_random_number()
            else:
                pivot = self.get_new_pivot(pivot)
            self.matrix.append(self.generate_row(pivot, row))

    def get_matrix_by_generation(self):
        """Return the matrix generated"""
        
        return self.matrix

    def get_new_pivot(self, pivot):
        """ Calculate the next pivot in the row

        Keyword arguments:
        pivot  --    New possible number

        return  --    New pivot calculated
        """
        new_pivot = pivot + 3
        if (new_pivot > 9):
            new_pivot = pivot - 3
            if (self.exist_number_in_column(new_pivot)):
                    new_pivot -= 3
        else:
            if (self.exist_number_in_column(new_pivot)):
                new_pivot = pivot - 3
                if (self.exist_number_in_column(new_pivot)):
                    new_pivot -= 3

        return new_pivot

    def generate_row(self, initial_number, new_row):
        """ Generated a row of 9 Cell elements

        Keyword arguments:
        initial_number  --    Pivot to generate the row
        new_row         --    Row position 

        return  list of Cells   [Cell1, Cell2 ... Cell9]
        """
        row_generated = []
        row_generated.append(Cell(initial_number, False, MAP_ROW[new_row], 0))
        new_number = initial_number + 1
        column = 1
        for row in range(1, 9):
            if new_number > 9:
                new_number = 1
            row_generated.append(Cell(new_number, False, MAP_ROW[new_row], column))
            new_number += 1
            column += 1
        return row_generated

    def get_matrix(self):
        """Return the matrix generated"""
        return self.matrix

    def exist_number_in_column(self, number):
        """Return false if the number does not in the column 0 of matrix

        Keyword arguments:
        number  --   Number to verify if exist in the column 0 of matrix

        return  --   A boolean value"""
        for row in range(len(self.matrix)):
            if (int(self.matrix[row][0].get_cell_value()) == int(number)):
                return True
        return False
