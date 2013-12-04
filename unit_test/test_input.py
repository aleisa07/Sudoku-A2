import unittest
import sys
sys.path.append( '../src' )
from input_file import Input

class TestInput(unittest.TestCase):

	def setUp(self):
		self.input_file = Input("../input_files/file.txt")
		self.matrix = self.input_file.get_matrix_by_file()

	def test_verify_the_returned_extension_is_correct(self):
		extension = "txt"
		actual = self.input_file.get_file_extension()
		self.assertEqual(extension, actual) 
    
	def test_values_were_load_correctly_from_txt_file(self):
		expected_matrix =[[1,0,3,4,5,0,7,8,0],
						  [0,5,6,7,8,0,1,0,3],
						  [7,0,9,1,2,3,4,5,6],
						  [2,0,4,5,6,7,0,9,1],
						  [5,6,7,8,9,1,2,0,4],
						  [8,9,0,2,0,4,0,6,7],
						  [3,4,5,6,7,8,0,1,2],
					  	  [6,0,8,9,1,0,3,4,5],
						  [9,0,3,2,4,0,6,0,0]]

		for row in range(9):
			for column in range(9):
				self.assertEqual(str(self.matrix[row][column].get_cell_value()), 
								 str(expected_matrix[row][column]))

	def test_values_were_load_correctly_from_csv_file(self):
		csv_file = Input("../input_files/file.csv")
		csv_matrix = csv_file.get_matrix_by_file()

		expected_matrix =[[1,2,0,4,5,0,7,0,9],
						  [4,0,6,0,8,9,1,0,3],
						  [7,8,9,1,0,3,4,5,0],
						  [2,0,4,5,6,7,8,9,1],
						  [5,6,7,0,9,1,2,3,4],
						  [0,9,1,2,3,4,0,6,7],
						  [3,0,5,0,7,0,9,0,2],
						  [6,7,8,9,1,2,0,4,5],
						  [0,1,2,3,4,5,6,0,8]]

		for row in range(9):
			for column in range(9):
				self.assertEqual(str(csv_matrix[row][column].get_cell_value()), 
								 str(expected_matrix[row][column]))



if __name__ == "__main__":
    unittest.main()

