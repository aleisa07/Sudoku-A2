class AlgorithmSolver(object):
    
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, sudoku_matrix):
        """Return the solution for the sudoku.

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        return self.algorithm.solve(sudoku_matrix)
    
    def change_algorithm(self, new_algorithm):
        """Method to change the algorithm.

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        self.algorithm = new_algorithm

    def display(self, sudoku_matrix):
        """Method to display a Sudoku.

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        self.algorithm.display(sudoku_matrix)
