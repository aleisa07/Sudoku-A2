import unittest
from src.algorithm_norvig import AlgorithmNorvig
from src.algorithm_solver import AlgorithmSolver
from src.sudoku_matrix import SudokuMatrix

__author__ = 'Carlos Gonzales'


class TestNorvigAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solver = AlgorithmSolver(AlgorithmNorvig())

    def test_verify_that_the_algorithm_norvig_solve_a_sudoku(self):
        """
        2 4 5 |9 8 1 |3 7 6
        1 6 9 |2 7 3 |5 8 4
        8 3 7 |5 6 4 |2 1 9
        ------+------+------
        9 7 6 |1 2 5 |4 3 8
        5 1 3 |4 9 8 |6 2 7
        4 8 2 |7 3 6 |9 5 1
        ------+------+------
        3 9 1 |6 5 7 |8 4 2
        7 2 8 |3 4 9 |1 6 5
        6 5 4 |8 1 2 |7 9 3
        """
        sudoku_easy = {'A1': '2', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '8',
                       'A6': '0', 'A7': '3', 'A8': '0', 'A9': '0',
                       'B1': '0', 'B2': '6', 'B3': '0', 'B4': '0', 'B5': '7',
                       'B6': '0', 'B7': '0', 'B8': '8', 'B9': '4',
                       'C1': '0', 'C2': '3', 'C3': '0', 'C4': '5', 'C5': '0',
                       'C6': '0', 'C7': '2', 'C8': '0', 'C9': '9',
                       'D1': '0', 'D2': '0', 'D3': '0', 'D4': '1', 'D5': '0',
                       'D6': '5', 'D7': '4', 'D8': '0', 'D9': '8',
                       'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0',
                       'E6': '0', 'E7': '0', 'E8': '0', 'E9': '0',
                       'F1': '4', 'F2': '0', 'F3': '2', 'F4': '7', 'F5': '0',
                       'F6': '6', 'F7': '0', 'F8': '0', 'F9': '0',
                       'G1': '3', 'G2': '0', 'G3': '1', 'G4': '0', 'G5': '0',
                       'G6': '7', 'G7': '0', 'G8': '4', 'G9': '0',
                       'H1': '7', 'H2': '2', 'H3': '0', 'H4': '0', 'H5': '4',
                       'H6': '0', 'H7': '0', 'H8': '6', 'H9': '0',
                       'I1': '0', 'I2': '0', 'I3': '4', 'I4': '0', 'I5': '1',
                       'I6': '0', 'I7': '0', 'I8': '0', 'I9': '3'}

        expect_sudo = {'A1': '2', 'A2': '4', 'A3': '5', 'A4': '9', 'A5': '8',
                       'A6': '1', 'A7': '3', 'A8': '7', 'A9': '6',
                       'B1': '1', 'B2': '6', 'B3': '9', 'B4': '2', 'B5': '7',
                       'B6': '3', 'B7': '5', 'B8': '8', 'B9': '4',
                       'C1': '8', 'C2': '3', 'C3': '7', 'C4': '5', 'C5': '6',
                       'C6': '4', 'C7': '2', 'C8': '1', 'C9': '9',
                       'D1': '9', 'D2': '7', 'D3': '6', 'D4': '1', 'D5': '2',
                       'D6': '5', 'D7': '4', 'D8': '3', 'D9': '8',
                       'E1': '5', 'E2': '1', 'E3': '3', 'E4': '4', 'E5': '9',
                       'E6': '8', 'E7': '6', 'E8': '2', 'E9': '7',
                       'F1': '4', 'F2': '8', 'F3': '2', 'F4': '7', 'F5': '3',
                       'F6': '6', 'F7': '9', 'F8': '5', 'F9': '1',
                       'G1': '3', 'G2': '9', 'G3': '1', 'G4': '6', 'G5': '5',
                       'G6': '7', 'G7': '8', 'G8': '4', 'G9': '2',
                       'H1': '7', 'H2': '2', 'H3': '8', 'H4': '3', 'H5': '4',
                       'H6': '9', 'H7': '1', 'H8': '6', 'H9': '5',
                       'I1': '6', 'I2': '5', 'I3': '4', 'I4': '8', 'I5': '1',
                       'I6': '2', 'I7': '7', 'I8': '9', 'I9': '3'}

        sudoku_matrix_easy = self.solver.algorithm.convert_dict_to_matrix(
            sudoku_easy)
        sudoku_matrix_expected = self.solver.algorithm.convert_dict_to_matrix(
            expect_sudo)
        solved_sudoku = self.solver.solve(sudoku_matrix_easy)
        #self.solver.display(sudoku_matrix_expected)
        #self.solver.display(solved_sudoku)
        self.assertTrue(solved_sudoku == sudoku_matrix_expected)

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
        sudoku_without_solution.set_cell_value(0, 1, 1)
        sudoku_without_solution.set_cell_value(0, 2, 9)
        sudoku_without_solution.set_cell_value(0, 3, 6)
        sudoku_without_solution.set_cell_value(0, 4, 7)
        sudoku_without_solution.set_cell_value(0, 5, 3)
        sudoku_without_solution.set_cell_value(0, 6, 5)
        sudoku_without_solution.set_cell_value(0, 7, 2)
        sudoku_without_solution.set_cell_value(0, 8, 8)

        sudoku_without_solution.set_cell_value(1, 0, 0)
        sudoku_without_solution.set_cell_value(1, 1, 6)
        sudoku_without_solution.set_cell_value(1, 2, 0)
        sudoku_without_solution.set_cell_value(1, 3, 8)
        sudoku_without_solution.set_cell_value(1, 4, 0)
        sudoku_without_solution.set_cell_value(1, 5, 9)
        sudoku_without_solution.set_cell_value(1, 6, 0)
        sudoku_without_solution.set_cell_value(1, 7, 4)
        sudoku_without_solution.set_cell_value(1, 8, 0)

        sudoku_without_solution.set_cell_value(2, 0, 7)
        sudoku_without_solution.set_cell_value(2, 1, 5)
        sudoku_without_solution.set_cell_value(2, 2, 0)
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
        sudoku_without_solution.set_cell_value(7, 5, 4)
        sudoku_without_solution.set_cell_value(7, 6, 2)
        sudoku_without_solution.set_cell_value(7, 7, 0)
        sudoku_without_solution.set_cell_value(7, 8, 1)

        sudoku_without_solution.set_cell_value(8, 0, 5)
        sudoku_without_solution.set_cell_value(8, 1, 2)
        sudoku_without_solution.set_cell_value(8, 2, 1)
        sudoku_without_solution.set_cell_value(8, 3, 3)
        sudoku_without_solution.set_cell_value(8, 4, 6)
        sudoku_without_solution.set_cell_value(8, 5, 8)
        sudoku_without_solution.set_cell_value(8, 6, 9)
        sudoku_without_solution.set_cell_value(8, 7, 7)
        sudoku_without_solution.set_cell_value(8, 8, 4)

        solved_sudoku = self.solver.solve(sudoku_without_solution)
        #self.solver.display(sudoku_with_solution)
        #self.solver.display(solved_sudoku)
        self.assertTrue(sudoku_with_solution == solved_sudoku)

if __name__ == '__main__':
    unittest.main()