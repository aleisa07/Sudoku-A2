import sys
sys.path.append( '../src' )
import unittest
from cell import Cell


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(6, True, "B", 3)

    def test_cell_can_set_new_value(self):
        other_cell = Cell(5, True, "A", 0)
        self.assertEqual(other_cell.value, 5)

    def test_verify_if_status_can_updated(self):
        self.cell.set_cell_visibility(False)
        self.assertFalse(self.cell.get_cell_visibility())

    def test_set_the_cell_as_hide(self):
        self.cell.set_cell_visibility(False)
        self.assertFalse(self.cell.get_cell_visibility())

    def test_values_map_of_cell_are_correct(self):
        self.assertEqual(self.cell.row, "B")
        self.assertEqual(self.cell.column, 3)

    def test_the_value_returned_is_correct(self):
        cell = Cell(5, True, "A", 0)
        self.assertEqual(cell.get_cell_value(), 5)

    def test_verify_the_position_set_with_new_value_in_cell_object(self):
        self.cell.set_cell_value(8)
        self.assertEqual(self.cell.get_cell_value(), 8)

    def test_the_values_referenced_for_each_cell_are_set_correctly(self):
        self.cell.set_map("C", 2)
        self.assertEqual(self.cell.row, "C")
        self.assertEqual(self.cell.column, 2)


if __name__ == "__main__":
    unittest.main()