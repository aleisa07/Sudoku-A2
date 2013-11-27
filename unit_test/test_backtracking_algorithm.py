import unittest
import sys
sys.path.append( '../src' )
from generator import Generator
from cell import Cell
from solver import AlgorithmSolver
from algorithm_backtracking import Backtracking


class testBacktracking(unittest.TestCase):

    def test_solve_sudoku_using_backtracking_algorithm(self):
        generator = Generator()
        sudoku_matrix = generator.generate_matrix()

        for i in range(9):
            var = ""
            for j in range(9):
                var = var + '\t' + str(sudoku_matrix.get_grid(i, j).get_value())
            print var

        sudoku_matrix.set_grid(1, 2, Cell())
        sudoku_matrix.set_grid(2, 2, Cell())
        sudoku_matrix.set_grid(3, 2, Cell())
        sudoku_matrix.set_grid(4, 2, Cell())
        sudoku_matrix.set_grid(5, 7, Cell())
        sudoku_matrix.set_grid(6, 8, Cell())

        print "#####################"

        for i in range(9):
            var = ""
            for j in range(9):
                var = var + '\t' + str(sudoku_matrix.get_grid(i, j).get_value())
            print var
        solver = AlgorithmSolver(Backtracking())
        values = solver.solve(sudoku_matrix)
        print values
        #solver.display(values)



        #for key, value in dict.iteritems():
        #    print key, value

if __name__ == "__main__":
    unittest.main()


	
	


