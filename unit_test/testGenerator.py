import unittest
import sys
sys.path.append( '../src' )
from generator import Generator
from grid import Grid

class testGenerator(unittest.TestCase):

    def test_the_random_number_is_less_than_ten_and_grather_than_0(self):
        gen = Generator()
        self.assertGreater(gen.generate_random_number(), 0)
        self.assertLess(gen.generate_random_number(), 10)
    
    def test_verify_if_row_generated_is_correct(self):
        gen = Generator()
        expected = [5, 6, 7, 8, 9, 1, 2, 3, 4]
        actual = gen.generate_row(5)
        for i in range(9):
            self.assertEqual(actual[i].get_value(), expected[i])

    def test_verify_if_values_generated_are_correct(self):
        matrix = Generator()
        matrix.print_matrix()
        pivote = matrix[6][0]
        row = generator.generate_row(pivote)
        for i in 9:
                self.assertEqual(row[i], matrix[6][i])

    def test_verify_if_values_generated_are_correct(self):
        matrix = Generator()
        pivote = matrix.get_grid(0, 0).get_value()
        row_pivote = matrix.generate_row(pivote)
        row_matrix = matrix.get_row(0)
        for i in range(9):
            self.assertEqual(str(row_matrix[i].get_value()), str(row_pivote[i].get_value()))


if __name__ == "__main__":
    unittest.main()

