
class Cell():

    def __init__(self, value, visible, row, column):
        """Initialize a cell to be part of matrix
        (e.g. Cell(2, False, "A", 1))
        
        Keyword arguments:

        visible -- status of cell to hide or display the value in the matrix
        value   -- value of cell it can be a number between 1 and 9
        row     -- it is the position en the row matrix [A, B, C, D, E, F, G, H, I]
        column  -- It is the position en the column matrix [1, 2, 3, 4, 5, 6, 7, 8, 9,]

        """
        self.visible = visible
        self.value = value
        self.row = row
        self.column = column

    def set_cell_visibility(self, status):
        self.visible = status

    def get_cell_visibility(self):
        return self.visible

    def set_cell_value(self, value):
        self.value = value

    def get_cell_value(self):
        return self.value

    def set_map(self, row, column):
        self.row = row
        self.column = column


if __name__ == "__main__":
    c = Cell(6, True, "B")
