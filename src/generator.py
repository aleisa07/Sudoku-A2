import random
from grid import Grid

class Generator():

    def __init__(self):
        self.matrix = [[Grid() for i in range(9)] for i in range(9)]
        self.matrix = self.generate_matrix()

    def generate_matrix(self):
        pivot = 0
        new_number = 0
        for i in range(9):
            if (i == 0 or i == 3 or i ==6):
                while self.exist_number_in_column(pivot, 0):
                    pivot = self.generate_random_number()
                new_number = pivot
            row = self.generate_row(new_number)
            self.set_row(i, row)
            if ((new_number + 3) > 9):
                new_number -= 3
                if self.exist_number_in_column(new_number, 0):
                    new_number -= 3
            else:
                if (self.exist_number_in_column(new_number + 3, 0)):
                    new_number -= 3
                else:
                    new_number += 3
        return self.matrix

    def generate_random_number(self):
        return random.randint(1, 9)

    def generate_row(self, initial_number):
        row_generated = [Grid() for i in range(9)]
        row_generated[0].set_value(initial_number)
        new_number = initial_number + 1
        for i in range(1, 9):
            if new_number > 9:
                new_number = 1
            row_generated[i].set_value(new_number)
            new_number += 1
        return row_generated

    def exist_number_in_column(self, number, column):
        for i in range(9):
            if int(self.matrix[i][column].get_value()) == int(number):
                return True
        return False

    def set_row(self, x, row):
        self.matrix[x] = row

    def get_grid(self, i, j):
        return self.matrix[i][j]

    def set_grid(self, x, y, value):
        self.matrix[x][y].set_value(value)

    def print_matrix(self):
        for i in range(9):
            var = ""
            for j in range(9):
                var = var + '\t' + str(self.get_grid(i, j).get_value())
            print (var)

    def get_row(self, row):
        return self.matrix[row]

    
if __name__ == "__main__":
    generator = Generator()
    generator.print_matrix()