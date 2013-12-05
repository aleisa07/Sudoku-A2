class AlgorithmSolver(object):
    
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, sudoku_matrix):
        """Return the solution for the sudoku.

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        return self.algorithm.solve(sudoku_matrix)
