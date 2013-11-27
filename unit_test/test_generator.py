import unittest
import sys
sys.path.append( '../src' )
from generator import Generator
from cell import Cell

class TestGenerator(unittest.TestCase):

    generator = Generator()
    matrix = generator.matrix

    def test_the_random_number_generated_is_between_nine_and_zero(self):
        self.assertGreater(self.generator.generate_random_number(), 0) 
        self.assertLess(self.generator.generate_random_number(), 10)
    
    def test_verify_if_row_generated_is_correct(self):
        expected = [5, 6, 7, 8, 9, 1, 2, 3, 4]
        actual = self.generator.generate_row(5, 0)
        for position in range(9):
            self.assertEqual(actual[position].get_cell_value(), expected[position])

    def test_values_generated_in_row_are_the_same_in_matrix(self):
        pivote = self.matrix[6][0].get_cell_value()
        row = self.generator.generate_row(pivote, 0)
        for i in range(9):
            self.assertEqual(row[i].get_cell_value(), self.matrix[6][i].get_cell_value())

    def test_verify_values_generated_are_correct(self):
        pivote = self.matrix[0][0].get_cell_value()
        row_pivote = self.generator.generate_row(pivote,0)
        row_matrix = self.matrix[0]
        for i in range(9):
            self.assertEqual(row_matrix[i].get_cell_value(), row_pivote[i].get_cell_value())


if __name__ == "__main__":
    unittest.main()

