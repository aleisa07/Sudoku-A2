from src.algorithm_base import AlgorithmBase

class Backtracking(AlgorithmBase):
     
    def __init__(self):
        self.sudoku_matrix = None
   
    def solve(self, matrix):
        self.sudoku_matrix = matrix
        self.solveInline(0, 0)    

    def solveInline(self, row, col):        
        if  (col >= 9):
            col = 0        
            row = row +1;
            if (row >= 9):
                return True      
        
        if ((self.sudoku_matrix[row][col]).get_cell_value() != 0):           
            return self.solveInline(row , (col + 1))       

        for cellValue in range(1,10):    
            if (self.isValidValue(row, col, cellValue)):
                self.sudoku_matrix[row][col].set_cell_value(cellValue)                
                if (self.solveInline(row, (col + 1))):
                    return True              
        (self.sudoku_matrix[row][col]).set_cell_value(0)
        return False

    def isValidValue(self,row, col, cellValue):
        for row in range(9):             
            if (cellValue == self.sudoku_matrix[row][col].get_cell_value()):             
                return False
                    
        for col in range(9):            
            if (cellValue == self.sudoku_matrix[row][col].get_cell_value()):             
                return False
                    
        rowOffset = (row / 3) * 3
        colOffset = (col / 3) * 3

        for i in range(3):
            for j in range(3):
                if (cellValue == (self.sudoku_matrix[rowOffset + i][colOffset + j]).get_cell_value()):
                    return False                
                
        return True
    
    def get_grid(self, row, col):
        return self.sudoku_matrix[row][col]

    def display(self):
        for row in range(9):
            var = ""
            for col in range(9):
                var = var + '\t' + str(self.get_grid(row, col).get_cell_value())
            print (var)

    def get_matrix_solved(self):
        return  sudoku_matrix

    
    
