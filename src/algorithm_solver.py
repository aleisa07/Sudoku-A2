import time


class AlgorithmSolver(object):
    
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, sudoku_matrix):
        """Return the solution for the sudoku.

        Keyword arguments:
        sudoku_matrix -- Sudoku Matrix Object

        """
        return self.algorithm.solve(sudoku_matrix)


def time_decorator(func):
    def wrapper(*arg):
        initial_time = time.time()
        response = func(*arg)
        time_result = time.time() - initial_time
        return response, time_result
    return wrapper