import random
import os
import os.path
import csv
from constant import MAP_ROW
from cell import Cell
import utils

class Input():
    """ Read from a txt or csv file the contentand and put in a matrix of cells"""

    def __init__(self, path_file):
        """This class read matrix from txt or csv file
        
        Keyword arguments:
        path_file   --    Path of file to load in the matrix"""
        self.matrix = []
        self.path_file = path_file
        if(utils.exist_file(path_file)):
            self.fill_matrix_from_input_file()


    def fill_matrix_from_input_file(self):
        """ Select the type of file is send to fill the matrix

        Keyword arguments:
        file_path   --   Absolute path of file to load the matrix"""
        if (self.get_file_extension() == "txt"):
            self.fill_matrix_from_txt_file(self.path_file)
        elif (self.get_file_extension() == "csv"):
            self.fill_matrix_from_csv_file(self.path_file)
        else: 
            print ("The application does not support this kind of file")   

    def fill_matrix_from_txt_file(self, path_txt_file):
        """Read a file from txt file and fill a matrix with Cell object

        Keyword arguments:
        path_file   --    Absolute path of txt file to load
        """
        try:
            content = open(path_txt_file)
            row_position = 0
            for line in iter(content):
                row = self.add_cell_in_row_matrix(line, row_position)
                self.matrix.append(row)
                row_position += 1
            content.close()
            
        except IOError:
            print ("The file cannot open")

    def fill_matrix_from_csv_file(self, file_path):
        """Read a csv file and fill a matrix with cell Object
        
        Keyword arguments:
        file_path   --    Absolute path of csv file to load
        """
        csv_file = open(file_path, 'r') 
        try:
            reader = csv.reader(csv_file)
            for csv_row in reader:
                row_position = 0
                for line in csv_row:
                    row = self.add_cell_in_row_matrix(line, row_position)
                    self.matrix.append(row)
                    row_position += 1
        except:
            print("File not exist")
        finally:
            csv_file.close()   

    def get_matrix_by_file(self):
        """Return the matrix fill with data read from a txt or csv"""
        return self.matrix

    def get_file_extension(self):
        """Return the extension of a file name
        
        Keyword arguments:
        filename    --   the filename to get the extension

        return      --   extension of a name file send
        """
        extension = self.path_file[-3:]
        return extension

    def add_cell_in_row_matrix(self, line, row_position):
        """Add at the end of row a new Cell
        
        Keyword arguments:
        line          --   A line of a txt or csv file
        row_position  --   Position that row will fill
        
        return        --   Retuen a list of Cell object
        """
        list_row = []
        for column in range(9):
            if(line[column] == "." or line[column] == "0"):
                list_row.append(Cell(0, True, MAP_ROW[row_position], column))
            else:
                list_row.append(Cell(line[column], False, MAP_ROW[row_position], column))

        return list_row

    def test_values_were_load_correctly(self):
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
                if (str(self.matrix[row][column].get_cell_value()) == str(expected_matrix[row][column])):
                    print(str(self.matrix[row][column].get_cell_value())+"="+str(expected_matrix[row][column]))
                else:
                    print ("no iguales")

#i = Input("../input_files/file.txt")
#i.test_values_were_load_correctly()


