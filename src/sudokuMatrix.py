import random
from grid import Grid
from generator import Generator

class SudokuMatrix():

    sudoku_matrix =[[]]
    dificult = "normal"
    level = { "easy": 	20,
    		  "normal":	50,
    		  "demente":70}
    file_to_load = None

    def __init__(self):
        generator= Generator()
        generator.print_matrix()
        self.sudoku_matrix = generator.matrix
        


    def hidden_values_in_matrix(self, cont=0):
    	i = random.randint(0, 8)
    	j = random.randint(0, 8)
    	if (cont != self.level[self.dificult]):
    		self.sudoku_matrix[i][j].set_status(False)

    		self.hidden_values_in_matrix(cont + 1)
    	else:
    		return 

    def print_sudoku_matrix(self):
        for i in range(9):
            var = ""
            for j in range(9):
            	if (self.sudoku_matrix[i][j].get_status() == False):
            		var = var + '\t' + "."
            	else:
                	var = var + '\t' + str(self.sudoku_matrix[i][j].get_value())
            print (var)

if __name__ == "__main__":
    sudoku = SudokuMatrix()
    sudoku.hidden_values_in_matrix()
    print("    -----------WITH LEVEL------------")
    sudoku.print_sudoku_matrix()

