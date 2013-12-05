import unittest
import sys
sys.path.append('../src')

from algorithm_norvig import AlgorithmNorvig
from algorithm_solver import AlgorithmSolver
from sudoku_matrix import SudokuMatrix

__author__ = 'Carlos Gonzales'


class TestNorvigAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solver = AlgorithmSolver(AlgorithmNorvig())

    def test_verify_that_the_algorithm_norvig_solve_a_sudoku_matrix_object(
            self):
        """
        4 1 9 |6 7 3 |5 2 8
        3 6 2 |8 5 9 |1 4 7
        7 5 8 |2 4 1 |3 6 9
        ------+------+------
        1 8 5 |4 2 6 |7 9 3
        2 4 3 |9 8 7 |6 1 5
        6 9 7 |1 3 5 |4 8 2
        ------+------+------
        9 7 4 |5 1 2 |8 3 6
        8 3 6 |7 9 4 |2 5 1
        5 2 1 |3 6 8 |9 7 4
        """
        sudoku_with_solution = SudokuMatrix()
        sudoku_with_solution.set_cell_value(0, 0, 4)
        sudoku_with_solution.set_cell_value(0, 1, 1)
        sudoku_with_solution.set_cell_value(0, 2, 9)
        sudoku_with_solution.set_cell_value(0, 3, 6)
        sudoku_with_solution.set_cell_value(0, 4, 7)
        sudoku_with_solution.set_cell_value(0, 5, 3)
        sudoku_with_solution.set_cell_value(0, 6, 5)
        sudoku_with_solution.set_cell_value(0, 7, 2)
        sudoku_with_solution.set_cell_value(0, 8, 8)

        sudoku_with_solution.set_cell_value(1, 0, 3)
        sudoku_with_solution.set_cell_value(1, 1, 6)
        sudoku_with_solution.set_cell_value(1, 2, 2)
        sudoku_with_solution.set_cell_value(1, 3, 8)
        sudoku_with_solution.set_cell_value(1, 4, 5)
        sudoku_with_solution.set_cell_value(1, 5, 9)
        sudoku_with_solution.set_cell_value(1, 6, 1)
        sudoku_with_solution.set_cell_value(1, 7, 4)
        sudoku_with_solution.set_cell_value(1, 8, 7)

        sudoku_with_solution.set_cell_value(2, 0, 7)
        sudoku_with_solution.set_cell_value(2, 1, 5)
        sudoku_with_solution.set_cell_value(2, 2, 8)
        sudoku_with_solution.set_cell_value(2, 3, 2)
        sudoku_with_solution.set_cell_value(2, 4, 4)
        sudoku_with_solution.set_cell_value(2, 5, 1)
        sudoku_with_solution.set_cell_value(2, 6, 3)
        sudoku_with_solution.set_cell_value(2, 7, 6)
        sudoku_with_solution.set_cell_value(2, 8, 9)

        sudoku_with_solution.set_cell_value(3, 0, 1)
        sudoku_with_solution.set_cell_value(3, 1, 8)
        sudoku_with_solution.set_cell_value(3, 2, 5)
        sudoku_with_solution.set_cell_value(3, 3, 4)
        sudoku_with_solution.set_cell_value(3, 4, 2)
        sudoku_with_solution.set_cell_value(3, 5, 6)
        sudoku_with_solution.set_cell_value(3, 6, 7)
        sudoku_with_solution.set_cell_value(3, 7, 9)
        sudoku_with_solution.set_cell_value(3, 8, 3)

        sudoku_with_solution.set_cell_value(4, 0, 2)
        sudoku_with_solution.set_cell_value(4, 1, 4)
        sudoku_with_solution.set_cell_value(4, 2, 3)
        sudoku_with_solution.set_cell_value(4, 3, 9)
        sudoku_with_solution.set_cell_value(4, 4, 8)
        sudoku_with_solution.set_cell_value(4, 5, 7)
        sudoku_with_solution.set_cell_value(4, 6, 6)
        sudoku_with_solution.set_cell_value(4, 7, 1)
        sudoku_with_solution.set_cell_value(4, 8, 5)

        sudoku_with_solution.set_cell_value(5, 0, 6)
        sudoku_with_solution.set_cell_value(5, 1, 9)
        sudoku_with_solution.set_cell_value(5, 2, 7)
        sudoku_with_solution.set_cell_value(5, 3, 1)
        sudoku_with_solution.set_cell_value(5, 4, 3)
        sudoku_with_solution.set_cell_value(5, 5, 5)
        sudoku_with_solution.set_cell_value(5, 6, 4)
        sudoku_with_solution.set_cell_value(5, 7, 8)
        sudoku_with_solution.set_cell_value(5, 8, 2)

        sudoku_with_solution.set_cell_value(6, 0, 9)
        sudoku_with_solution.set_cell_value(6, 1, 7)
        sudoku_with_solution.set_cell_value(6, 2, 4)
        sudoku_with_solution.set_cell_value(6, 3, 5)
        sudoku_with_solution.set_cell_value(6, 4, 1)
        sudoku_with_solution.set_cell_value(6, 5, 2)
        sudoku_with_solution.set_cell_value(6, 6, 8)
        sudoku_with_solution.set_cell_value(6, 7, 3)
        sudoku_with_solution.set_cell_value(6, 8, 6)

        sudoku_with_solution.set_cell_value(7, 0, 8)
        sudoku_with_solution.set_cell_value(7, 1, 3)
        sudoku_with_solution.set_cell_value(7, 2, 6)
        sudoku_with_solution.set_cell_value(7, 3, 7)
        sudoku_with_solution.set_cell_value(7, 4, 9)
        sudoku_with_solution.set_cell_value(7, 5, 4)
        sudoku_with_solution.set_cell_value(7, 6, 2)
        sudoku_with_solution.set_cell_value(7, 7, 5)
        sudoku_with_solution.set_cell_value(7, 8, 1)

        sudoku_with_solution.set_cell_value(8, 0, 5)
        sudoku_with_solution.set_cell_value(8, 1, 2)
        sudoku_with_solution.set_cell_value(8, 2, 1)
        sudoku_with_solution.set_cell_value(8, 3, 3)
        sudoku_with_solution.set_cell_value(8, 4, 6)
        sudoku_with_solution.set_cell_value(8, 5, 8)
        sudoku_with_solution.set_cell_value(8, 6, 9)
        sudoku_with_solution.set_cell_value(8, 7, 7)
        sudoku_with_solution.set_cell_value(8, 8, 4)

        sudoku_without_solution = SudokuMatrix()
        sudoku_without_solution.set_cell_value(0, 0, 4)
        sudoku_without_solution.set_cell_value(0, 1, 0)
        sudoku_without_solution.set_cell_value(0, 2, 9)
        sudoku_without_solution.set_cell_value(0, 3, 0)
        sudoku_without_solution.set_cell_value(0, 4, 7)
        sudoku_without_solution.set_cell_value(0, 5, 0)
        sudoku_without_solution.set_cell_value(0, 6, 5)
        sudoku_without_solution.set_cell_value(0, 7, 0)
        sudoku_without_solution.set_cell_value(0, 8, 8)

        sudoku_without_solution.set_cell_value(1, 0, 0)
        sudoku_without_solution.set_cell_value(1, 1, 6)
        sudoku_without_solution.set_cell_value(1, 2, 0)
        sudoku_without_solution.set_cell_value(1, 3, 0)
        sudoku_without_solution.set_cell_value(1, 4, 0)
        sudoku_without_solution.set_cell_value(1, 5, 9)
        sudoku_without_solution.set_cell_value(1, 6, 0)
        sudoku_without_solution.set_cell_value(1, 7, 4)
        sudoku_without_solution.set_cell_value(1, 8, 0)

        sudoku_without_solution.set_cell_value(2, 0, 7)
        sudoku_without_solution.set_cell_value(2, 1, 0)
        sudoku_without_solution.set_cell_value(2, 2, 0)
        sudoku_without_solution.set_cell_value(2, 3, 2)
        sudoku_without_solution.set_cell_value(2, 4, 4)
        sudoku_without_solution.set_cell_value(2, 5, 0)
        sudoku_without_solution.set_cell_value(2, 6, 3)
        sudoku_without_solution.set_cell_value(2, 7, 0)
        sudoku_without_solution.set_cell_value(2, 8, 0)

        sudoku_without_solution.set_cell_value(3, 0, 1)
        sudoku_without_solution.set_cell_value(3, 1, 0)
        sudoku_without_solution.set_cell_value(3, 2, 5)
        sudoku_without_solution.set_cell_value(3, 3, 0)
        sudoku_without_solution.set_cell_value(3, 4, 2)
        sudoku_without_solution.set_cell_value(3, 5, 6)
        sudoku_without_solution.set_cell_value(3, 6, 0)
        sudoku_without_solution.set_cell_value(3, 7, 9)
        sudoku_without_solution.set_cell_value(3, 8, 3)

        sudoku_without_solution.set_cell_value(4, 0, 0)
        sudoku_without_solution.set_cell_value(4, 1, 4)
        sudoku_without_solution.set_cell_value(4, 2, 3)
        sudoku_without_solution.set_cell_value(4, 3, 0)
        sudoku_without_solution.set_cell_value(4, 4, 8)
        sudoku_without_solution.set_cell_value(4, 5, 7)
        sudoku_without_solution.set_cell_value(4, 6, 0)
        sudoku_without_solution.set_cell_value(4, 7, 1)
        sudoku_without_solution.set_cell_value(4, 8, 5)

        sudoku_without_solution.set_cell_value(5, 0, 0)
        sudoku_without_solution.set_cell_value(5, 1, 0)
        sudoku_without_solution.set_cell_value(5, 2, 7)
        sudoku_without_solution.set_cell_value(5, 3, 0)
        sudoku_without_solution.set_cell_value(5, 4, 0)
        sudoku_without_solution.set_cell_value(5, 5, 5)
        sudoku_without_solution.set_cell_value(5, 6, 0)
        sudoku_without_solution.set_cell_value(5, 7, 0)
        sudoku_without_solution.set_cell_value(5, 8, 2)

        sudoku_without_solution.set_cell_value(6, 0, 0)
        sudoku_without_solution.set_cell_value(6, 1, 7)
        sudoku_without_solution.set_cell_value(6, 2, 4)
        sudoku_without_solution.set_cell_value(6, 3, 0)
        sudoku_without_solution.set_cell_value(6, 4, 0)
        sudoku_without_solution.set_cell_value(6, 5, 2)
        sudoku_without_solution.set_cell_value(6, 6, 8)
        sudoku_without_solution.set_cell_value(6, 7, 3)
        sudoku_without_solution.set_cell_value(6, 8, 0)

        sudoku_without_solution.set_cell_value(7, 0, 8)
        sudoku_without_solution.set_cell_value(7, 1, 0)
        sudoku_without_solution.set_cell_value(7, 2, 0)
        sudoku_without_solution.set_cell_value(7, 3, 7)
        sudoku_without_solution.set_cell_value(7, 4, 0)
        sudoku_without_solution.set_cell_value(7, 5, 4)
        sudoku_without_solution.set_cell_value(7, 6, 2)
        sudoku_without_solution.set_cell_value(7, 7, 0)
        sudoku_without_solution.set_cell_value(7, 8, 1)

        sudoku_without_solution.set_cell_value(8, 0, 5)
        sudoku_without_solution.set_cell_value(8, 1, 0)
        sudoku_without_solution.set_cell_value(8, 2, 1)
        sudoku_without_solution.set_cell_value(8, 3, 3)
        sudoku_without_solution.set_cell_value(8, 4, 0)
        sudoku_without_solution.set_cell_value(8, 5, 0)
        sudoku_without_solution.set_cell_value(8, 6, 9)
        sudoku_without_solution.set_cell_value(8, 7, 0)
        sudoku_without_solution.set_cell_value(8, 8, 4)

        solved_sudoku = self.solver.solve(sudoku_without_solution)
        self.assertTrue(sudoku_with_solution == solved_sudoku)

    def test_verify_that_the_algorithm_norvig_solve_a_sudoku_matrix_object_trying_all_the_possible_values(
            self):
        """
            1 2 3   4 5 6   7 8 9
          +-------+-------+-------+
        A | 4 1 9 | 6 7 3 | 5 2 8 |
        B | 2 6 3 | 8 5 9 | 1 4 7 |
        C | 7 5 8 | 2 4 1 | 3 6 9 |
          +-------+-------+-------+
        D | 1 8 5 | 4 2 6 | 7 9 3 |
        E | 3 4 2 | 9 8 7 | 6 1 5 |
        F | 6 9 7 | 1 3 5 | 4 8 2 |
          +-------+-------+-------+
        G | 9 7 4 | 5 1 2 | 8 3 6 |
        H | 8 3 6 | 7 9 4 | 2 5 1 |
        I | 5 2 1 | 3 6 8 | 9 7 4 |
          +-------+-------+-------+
        """

        sudoku_without_solution = SudokuMatrix()
        sudoku_without_solution.set_cell_value(0, 0, 4)
        sudoku_without_solution.set_cell_value(0, 1, 0)
        sudoku_without_solution.set_cell_value(0, 2, 9)
        sudoku_without_solution.set_cell_value(0, 3, 0)
        sudoku_without_solution.set_cell_value(0, 4, 7)
        sudoku_without_solution.set_cell_value(0, 5, 0)
        sudoku_without_solution.set_cell_value(0, 6, 5)
        sudoku_without_solution.set_cell_value(0, 7, 0)
        sudoku_without_solution.set_cell_value(0, 8, 8)

        sudoku_without_solution.set_cell_value(1, 0, 0)
        sudoku_without_solution.set_cell_value(1, 1, 6)
        sudoku_without_solution.set_cell_value(1, 2, 0)
        sudoku_without_solution.set_cell_value(1, 3, 0)
        sudoku_without_solution.set_cell_value(1, 4, 0)
        sudoku_without_solution.set_cell_value(1, 5, 9)
        sudoku_without_solution.set_cell_value(1, 6, 0)
        sudoku_without_solution.set_cell_value(1, 7, 4)
        sudoku_without_solution.set_cell_value(1, 8, 0)

        sudoku_without_solution.set_cell_value(2, 0, 7)
        sudoku_without_solution.set_cell_value(2, 1, 0)
        sudoku_without_solution.set_cell_value(2, 2, 0)
        sudoku_without_solution.set_cell_value(2, 3, 2)
        sudoku_without_solution.set_cell_value(2, 4, 4)
        sudoku_without_solution.set_cell_value(2, 5, 0)
        sudoku_without_solution.set_cell_value(2, 6, 3)
        sudoku_without_solution.set_cell_value(2, 7, 0)
        sudoku_without_solution.set_cell_value(2, 8, 0)

        sudoku_without_solution.set_cell_value(3, 0, 1)
        sudoku_without_solution.set_cell_value(3, 1, 0)
        sudoku_without_solution.set_cell_value(3, 2, 5)
        sudoku_without_solution.set_cell_value(3, 3, 0)
        sudoku_without_solution.set_cell_value(3, 4, 2)
        sudoku_without_solution.set_cell_value(3, 5, 6)
        sudoku_without_solution.set_cell_value(3, 6, 0)
        sudoku_without_solution.set_cell_value(3, 7, 9)
        sudoku_without_solution.set_cell_value(3, 8, 3)

        sudoku_without_solution.set_cell_value(4, 0, 0)
        sudoku_without_solution.set_cell_value(4, 1, 4)
        sudoku_without_solution.set_cell_value(4, 2, 0)
        sudoku_without_solution.set_cell_value(4, 3, 0)
        sudoku_without_solution.set_cell_value(4, 4, 8)
        sudoku_without_solution.set_cell_value(4, 5, 7)
        sudoku_without_solution.set_cell_value(4, 6, 0)
        sudoku_without_solution.set_cell_value(4, 7, 1)
        sudoku_without_solution.set_cell_value(4, 8, 5)

        sudoku_without_solution.set_cell_value(5, 0, 0)
        sudoku_without_solution.set_cell_value(5, 1, 0)
        sudoku_without_solution.set_cell_value(5, 2, 7)
        sudoku_without_solution.set_cell_value(5, 3, 0)
        sudoku_without_solution.set_cell_value(5, 4, 0)
        sudoku_without_solution.set_cell_value(5, 5, 5)
        sudoku_without_solution.set_cell_value(5, 6, 0)
        sudoku_without_solution.set_cell_value(5, 7, 0)
        sudoku_without_solution.set_cell_value(5, 8, 2)

        sudoku_without_solution.set_cell_value(6, 0, 0)
        sudoku_without_solution.set_cell_value(6, 1, 7)
        sudoku_without_solution.set_cell_value(6, 2, 4)
        sudoku_without_solution.set_cell_value(6, 3, 0)
        sudoku_without_solution.set_cell_value(6, 4, 0)
        sudoku_without_solution.set_cell_value(6, 5, 2)
        sudoku_without_solution.set_cell_value(6, 6, 8)
        sudoku_without_solution.set_cell_value(6, 7, 3)
        sudoku_without_solution.set_cell_value(6, 8, 0)

        sudoku_without_solution.set_cell_value(7, 0, 8)
        sudoku_without_solution.set_cell_value(7, 1, 0)
        sudoku_without_solution.set_cell_value(7, 2, 0)
        sudoku_without_solution.set_cell_value(7, 3, 7)
        sudoku_without_solution.set_cell_value(7, 4, 0)
        sudoku_without_solution.set_cell_value(7, 5, 4)
        sudoku_without_solution.set_cell_value(7, 6, 2)
        sudoku_without_solution.set_cell_value(7, 7, 0)
        sudoku_without_solution.set_cell_value(7, 8, 1)

        sudoku_without_solution.set_cell_value(8, 0, 5)
        sudoku_without_solution.set_cell_value(8, 1, 0)
        sudoku_without_solution.set_cell_value(8, 2, 1)
        sudoku_without_solution.set_cell_value(8, 3, 3)
        sudoku_without_solution.set_cell_value(8, 4, 0)
        sudoku_without_solution.set_cell_value(8, 5, 0)
        sudoku_without_solution.set_cell_value(8, 6, 9)
        sudoku_without_solution.set_cell_value(8, 7, 0)
        sudoku_without_solution.set_cell_value(8, 8, 4)

        solved_sudoku = self.solver.solve(sudoku_without_solution)

    def test_verify_that_the_algorithm_norvig_solve_a_sudoku_matrix_object_eliminate_the_possible_values(
            self):
        """
            1 2 3   4 5 6   7 8 9
          +-------+-------+-------+
        A | 4 1 9 | 3 7 6 | 5 2 8 |
        B | 2 6 3 | 5 9 8 | 1 4 7 |
        C | 7 5 8 | 2 4 1 | 3 6 9 |
          +-------+-------+-------+
        D | 1 8 5 | 4 2 9 | 6 7 3 |
        E | 3 4 2 | 6 1 7 | 8 9 5 |
        F | 6 9 7 | 8 5 3 | 4 1 2 |
          +-------+-------+-------+
        G | 9 7 4 | 1 8 5 | 2 3 6 |
        H | 8 2 6 | 9 3 4 | 7 5 1 |
        I | 5 3 1 | 7 6 2 | 9 8 4 |
          +-------+-------+-------+
        """

        sudoku_without_solution = SudokuMatrix()
        sudoku_without_solution.set_cell_value(0, 0, 0)
        sudoku_without_solution.set_cell_value(0, 1, 0)
        sudoku_without_solution.set_cell_value(0, 2, 9)
        sudoku_without_solution.set_cell_value(0, 3, 0)
        sudoku_without_solution.set_cell_value(0, 4, 7)
        sudoku_without_solution.set_cell_value(0, 5, 0)
        sudoku_without_solution.set_cell_value(0, 6, 5)
        sudoku_without_solution.set_cell_value(0, 7, 0)
        sudoku_without_solution.set_cell_value(0, 8, 8)

        sudoku_without_solution.set_cell_value(1, 0, 0)
        sudoku_without_solution.set_cell_value(1, 1, 6)
        sudoku_without_solution.set_cell_value(1, 2, 0)
        sudoku_without_solution.set_cell_value(1, 3, 0)
        sudoku_without_solution.set_cell_value(1, 4, 0)
        sudoku_without_solution.set_cell_value(1, 5, 0)
        sudoku_without_solution.set_cell_value(1, 6, 0)
        sudoku_without_solution.set_cell_value(1, 7, 4)
        sudoku_without_solution.set_cell_value(1, 8, 0)

        sudoku_without_solution.set_cell_value(2, 0, 0)
        sudoku_without_solution.set_cell_value(2, 1, 0)
        sudoku_without_solution.set_cell_value(2, 2, 0)
        sudoku_without_solution.set_cell_value(2, 3, 2)
        sudoku_without_solution.set_cell_value(2, 4, 0)
        sudoku_without_solution.set_cell_value(2, 5, 0)
        sudoku_without_solution.set_cell_value(2, 6, 3)
        sudoku_without_solution.set_cell_value(2, 7, 0)
        sudoku_without_solution.set_cell_value(2, 8, 0)

        sudoku_without_solution.set_cell_value(3, 0, 1)
        sudoku_without_solution.set_cell_value(3, 1, 0)
        sudoku_without_solution.set_cell_value(3, 2, 5)
        sudoku_without_solution.set_cell_value(3, 3, 0)
        sudoku_without_solution.set_cell_value(3, 4, 2)
        sudoku_without_solution.set_cell_value(3, 5, 0)
        sudoku_without_solution.set_cell_value(3, 6, 0)
        sudoku_without_solution.set_cell_value(3, 7, 0)
        sudoku_without_solution.set_cell_value(3, 8, 0)

        sudoku_without_solution.set_cell_value(4, 0, 0)
        sudoku_without_solution.set_cell_value(4, 1, 4)
        sudoku_without_solution.set_cell_value(4, 2, 0)
        sudoku_without_solution.set_cell_value(4, 3, 0)
        sudoku_without_solution.set_cell_value(4, 4, 0)
        sudoku_without_solution.set_cell_value(4, 5, 7)
        sudoku_without_solution.set_cell_value(4, 6, 0)
        sudoku_without_solution.set_cell_value(4, 7, 0)
        sudoku_without_solution.set_cell_value(4, 8, 5)

        sudoku_without_solution.set_cell_value(5, 0, 0)
        sudoku_without_solution.set_cell_value(5, 1, 0)
        sudoku_without_solution.set_cell_value(5, 2, 7)
        sudoku_without_solution.set_cell_value(5, 3, 0)
        sudoku_without_solution.set_cell_value(5, 4, 0)
        sudoku_without_solution.set_cell_value(5, 5, 0)
        sudoku_without_solution.set_cell_value(5, 6, 0)
        sudoku_without_solution.set_cell_value(5, 7, 0)
        sudoku_without_solution.set_cell_value(5, 8, 2)

        sudoku_without_solution.set_cell_value(6, 0, 0)
        sudoku_without_solution.set_cell_value(6, 1, 7)
        sudoku_without_solution.set_cell_value(6, 2, 0)
        sudoku_without_solution.set_cell_value(6, 3, 0)
        sudoku_without_solution.set_cell_value(6, 4, 0)
        sudoku_without_solution.set_cell_value(6, 5, 0)
        sudoku_without_solution.set_cell_value(6, 6, 0)
        sudoku_without_solution.set_cell_value(6, 7, 3)
        sudoku_without_solution.set_cell_value(6, 8, 0)

        sudoku_without_solution.set_cell_value(7, 0, 8)
        sudoku_without_solution.set_cell_value(7, 1, 0)
        sudoku_without_solution.set_cell_value(7, 2, 0)
        sudoku_without_solution.set_cell_value(7, 3, 0)
        sudoku_without_solution.set_cell_value(7, 4, 0)
        sudoku_without_solution.set_cell_value(7, 5, 4)
        sudoku_without_solution.set_cell_value(7, 6, 0)
        sudoku_without_solution.set_cell_value(7, 7, 0)
        sudoku_without_solution.set_cell_value(7, 8, 1)

        sudoku_without_solution.set_cell_value(8, 0, 0)
        sudoku_without_solution.set_cell_value(8, 1, 0)
        sudoku_without_solution.set_cell_value(8, 2, 1)
        sudoku_without_solution.set_cell_value(8, 3, 0)
        sudoku_without_solution.set_cell_value(8, 4, 0)
        sudoku_without_solution.set_cell_value(8, 5, 0)
        sudoku_without_solution.set_cell_value(8, 6, 9)
        sudoku_without_solution.set_cell_value(8, 7, 0)
        sudoku_without_solution.set_cell_value(8, 8, 4)

        solved_sudoku = self.solver.solve(sudoku_without_solution)

    def test_verify_that_an_exception_message_is_raised_when_the_sudoku_matrix_is_wrong_defined(self):
        sudoku_without_solution = SudokuMatrix()
        sudoku_without_solution.set_cell_value(0, 0, 4)
        sudoku_without_solution.set_cell_value(0, 1, 1)
        sudoku_without_solution.set_cell_value(0, 2, 9)
        sudoku_without_solution.set_cell_value(0, 3, 6)
        sudoku_without_solution.set_cell_value(0, 5, 3)
        sudoku_without_solution.set_cell_value(0, 6, 5)
        sudoku_without_solution.set_cell_value(0, 7, 2)
        sudoku_without_solution.set_cell_value(0, 8, 8)

        sudoku_without_solution.set_cell_value(1, 0, 0)
        sudoku_without_solution.set_cell_value(1, 1, 6)
        sudoku_without_solution.set_cell_value(1, 3, 8)
        sudoku_without_solution.set_cell_value(1, 4, 0)
        sudoku_without_solution.set_cell_value(1, 5, 9)
        sudoku_without_solution.set_cell_value(1, 6, 0)
        sudoku_without_solution.set_cell_value(1, 7, 4)
        sudoku_without_solution.set_cell_value(1, 8, 0)

        sudoku_without_solution.set_cell_value(2, 0, 7)
        sudoku_without_solution.set_cell_value(2, 1, 5)
        sudoku_without_solution.set_cell_value(2, 3, 2)
        sudoku_without_solution.set_cell_value(2, 4, 4)
        sudoku_without_solution.set_cell_value(2, 5, 0)
        sudoku_without_solution.set_cell_value(2, 6, 3)
        sudoku_without_solution.set_cell_value(2, 7, 6)
        sudoku_without_solution.set_cell_value(2, 8, 0)

        sudoku_without_solution.set_cell_value(3, 0, 1)
        sudoku_without_solution.set_cell_value(3, 1, 8)
        sudoku_without_solution.set_cell_value(3, 2, 5)
        sudoku_without_solution.set_cell_value(3, 3, 0)
        sudoku_without_solution.set_cell_value(3, 5, 6)
        sudoku_without_solution.set_cell_value(3, 6, 0)
        sudoku_without_solution.set_cell_value(3, 7, 9)
        sudoku_without_solution.set_cell_value(3, 8, 3)

        sudoku_without_solution.set_cell_value(4, 0, 0)
        sudoku_without_solution.set_cell_value(4, 1, 4)
        sudoku_without_solution.set_cell_value(4, 2, 3)
        sudoku_without_solution.set_cell_value(4, 3, 0)
        sudoku_without_solution.set_cell_value(4, 4, 8)
        sudoku_without_solution.set_cell_value(4, 6, 0)
        sudoku_without_solution.set_cell_value(4, 7, 1)
        sudoku_without_solution.set_cell_value(4, 8, 5)

        sudoku_without_solution.set_cell_value(5, 0, 0)
        sudoku_without_solution.set_cell_value(5, 1, 0)
        sudoku_without_solution.set_cell_value(5, 2, 7)
        sudoku_without_solution.set_cell_value(5, 3, 0)
        sudoku_without_solution.set_cell_value(5, 4, 0)
        sudoku_without_solution.set_cell_value(5, 6, 0)
        sudoku_without_solution.set_cell_value(5, 7, 0)
        sudoku_without_solution.set_cell_value(5, 8, 2)

        sudoku_without_solution.set_cell_value(6, 0, 0)
        sudoku_without_solution.set_cell_value(6, 1, 7)
        sudoku_without_solution.set_cell_value(6, 3, 5)
        sudoku_without_solution.set_cell_value(6, 4, 0)
        sudoku_without_solution.set_cell_value(6, 5, 2)
        sudoku_without_solution.set_cell_value(6, 6, 8)
        sudoku_without_solution.set_cell_value(6, 7, 3)
        sudoku_without_solution.set_cell_value(6, 8, 0)

        sudoku_without_solution.set_cell_value(7, 0, 8)
        sudoku_without_solution.set_cell_value(7, 1, 0)
        sudoku_without_solution.set_cell_value(7, 2, 6)
        sudoku_without_solution.set_cell_value(7, 3, 7)
        sudoku_without_solution.set_cell_value(7, 4, 0)
        sudoku_without_solution.set_cell_value(7, 6, 2)
        sudoku_without_solution.set_cell_value(7, 7, 0)
        sudoku_without_solution.set_cell_value(7, 8, 1)

        sudoku_without_solution.set_cell_value(8, 0, 5)
        sudoku_without_solution.set_cell_value(8, 1, 2)
        sudoku_without_solution.set_cell_value(8, 2, 1)
        sudoku_without_solution.set_cell_value(8, 3, 3)
        sudoku_without_solution.set_cell_value(8, 5, 8)
        sudoku_without_solution.set_cell_value(8, 6, 9)
        sudoku_without_solution.set_cell_value(8, 7, 7)
        sudoku_without_solution.set_cell_value(8, 8, 4)

        self.assertEquals("Invalid dictionary.  Try again...",
                          self.solver.solve(sudoku_without_solution))

if __name__ == '__main__':
    unittest.main()