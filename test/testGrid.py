import unittest
import sys
sys.path.append( '../' )
from src.grid import Grid

class testGrid(unittest.TestCase):

    def test_the_fist_value_of_grid_is_zero(self):
    	grid = Grid()
    	self.assertTrue(grid.visible)

    def test_the_value_of_grid_alwas_is_zero_the_first_time(self):
    	grid = Grid()
    	self.assertEqual(grid.value, "0")

    def test_grid_can_set_a_new_value(self):
    	grid = Grid(True, "5")
    	self.assertEqual(grid.value, "5")

    def test_grid_can_be_return_a_value(self):
        grid = Grid(True, "6")
        self.assertEqual(grid.get_value(), "6")

    def test_verify_if_status_can_be_udate(self):
        grid = Grid()
        grid.set_status("hidden")
        self.assertEqual(grid.visible, "hidden")
	

if __name__ == "__main__":
	unittest.main()