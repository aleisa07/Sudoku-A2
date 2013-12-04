import unittest
import sys
sys.path.append('../src')

from generator import Generator
from cell import Cell
import utils


class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()
        self.matrix = self.generator.get_matrix()

    def test_the_random_number_generated_is_between_nine_and_zero(self):
        self.assertGreater(utils.generate_random_number(), 0)
        self.assertLess(utils.generate_random_number(), 10)
    
    def test_verify_if_row_generated_is_correct(self):
        expected = [5, 6, 7, 8, 9, 1, 2, 3, 4]
        actual = self.generator.generate_row(5, 0)
        for position in range(9):
            self.assertEqual(actual[position].get_cell_value(), expected[position])

    def test_values_generated_in_row_are_the_same_in_matrix(self):
        pivot = self.matrix[6][0].get_cell_value()
        row = self.generator.generate_row(pivot, 0)
        for i in range(9):
            self.assertEqual(row[i].get_cell_value(), self.matrix[6][i].get_cell_value())

    def test_verify_values_generated_are_correct(self):
        pivot = self.matrix[0][0].get_cell_value()
        row_pivot = self.generator.generate_row(pivot, 0)
        row_matrix = self.matrix[0]
        for i in range(9):
            self.assertEqual(row_matrix[i].get_cell_value(), row_pivot[i].get_cell_value())

    def test_verify_if_row_in_the_matriz_generated_are_correct(self):
        value = 1
        for row in self.matrix:
            repetitions = 0
            for cell in row:
                if(cell.get_cell_value() == value):
                    repetitions +=1
            value += 1
            self.assertEqual(repetitions, 1)

    def test_verify_if_column_in_the_matriz_generated_are_correct(self):
        for value in range(9):
            repetitions = 0
            for row in self.matrix:
                if (row[0].get_cell_value() == value+1):
                    repetitions += 1
            self.assertEqual(repetitions, 1)

if __name__ == "__main__":
    unittest.main()

