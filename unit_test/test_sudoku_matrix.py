import unittest
import sys
sys.path.append('../src')

from sudoku_matrix import SudokuMatrix
from generator import Generator
from input_file import Input

class TestSudokuMatrix(unittest.TestCase):

    def setUp(self):
        self.sudoku_matrix = SudokuMatrix()
        self.matrix = self.sudoku_matrix.get_sudoku_matrix()
        self.generator = Generator()
        self.sudoku_matrix_from_file = SudokuMatrix("../input_files/file.txt")

    def test_the_matrix_can_be_set_with_other_matrix(self):
        new_matrix = self.generator.get_matrix_by_generation()
        self.sudoku_matrix.set_sudoku_matrix(new_matrix)
        self.assertEqual(self.sudoku_matrix.get_sudoku_matrix(), new_matrix)

    def test_verify_if_value_get_from_matrix_is_correct(self):
        self.assertEqual(self.sudoku_matrix_from_file.get_cell(2,8).get_cell_value(), 6)

if __name__ == "__main__":
    unittest.main()

