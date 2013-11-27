import random
import os
import csv
from constant import MAP_ROW
from cell import Cell

class Input():
    """ Read from a txt or csv file the contentand and put in a matrix of cells"""
    matrix = []

    def __init__(self, path_file):
        """This class read matrix from txt or csv file"""
        self.matrix = []
        self.fill_matrix_from_input_file(path_file)

    def fill_matrix_from_input_file(self, file_path):
        """ Select the type of file is send to fill the matrix

        Keyword arguments:
        file_path   --   Absolute path of file to load the matrix"""
        if (self.get_file_extension(file_path) == "txt"):
            self.fill_matrix_from_txt_file(file_path)
        elif (self.get_file_extension(file_path) == "csv"):
                self.fill_matrix_from_csv_file(file_path)
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
        finally:
            csv_file.close()   

    def get_matrix_by_file(self):
        """Return the matrix fill with data read from a txt or csv"""
        return self.matrix

    def get_file_path(self, file_to_read):
        file_path = os.path.dirname(file_to_read)

        print (file_path)

    def get_file_extension(self, file_name):
        """Return the extension of a file name
        
        Keyword arguments:
        filename    --   the filename to get the extension

        return      --   extension of a name file send
        """
        extension = file_name[-3:]
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
                list_row.append(Cell( line[column], False, MAP_ROW[row_position], column))
            else:
                list_row.append(Cell( line[column], True, MAP_ROW[row_position], column))

        return list_row






