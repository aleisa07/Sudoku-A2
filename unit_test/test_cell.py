import unittest
import sys
sys.path.append( '../' )
from src.cell import Cell

class testGrid(unittest.TestCase):
    cell = Cell(6, True, "B", 3)

    def test_cell_can_set_new_value(self):
    	cell = Cell(5, True, "A", 0)
    	self.assertEqual(cell.value, 5)

    def test_cell_can_return_value(self):
        self.assertEqual(self.cell.get_cell_value(), 6)

    def test_verify_if_status_can_udated(self):
        self.cell.set_cell_visibility(False)
        self.assertFalse(self.cell.visible)

    def test_set_the_cell_as_hide(self):
        self.cell.set_cell_visibility(False)
        self.assertFalse(self.cell.get_cell_visibility())

    def test_values_map_of_cell_are_correct(self):
        self.assertEqual(self.cell.row, "B")
        self.assertEqual(self.cell.column, 3)

if __name__ == "__main__":
	unittest.main()