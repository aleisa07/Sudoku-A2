import sys
sys.path.append('../src')

import unittest
import utils

__author__ = 'Carlos Gonzales'


class TestUtilsMethods(unittest.TestCase):

    def test_verify_if_exist_a_path(self):
        path = "../src"
        self.assertTrue(utils.exist_path(path))

    def test_verify_if_do_not_exist_a_path(self):
        path = "path/not/exist"
        self.assertFalse(utils.exist_path(path))

    def test_verify_if_a_path_is_valid(self):
        path = "/home/carledriss/unit_test"
        self.assertTrue(utils.is_valid_path(path))

    def test_verify_if_a_path_is_not_valid(self):
        path = "testing?"
        self.assertFalse(utils.is_valid_path(path))

    def test_verify_that_the_cross_method_generate_the_peers(self):
        self.cols = '123456789'
        self.rows = 'ABCDEFGHI'
        expected_peers = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                          'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
                          'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                          'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                          'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9',
                          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                          'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9',
                          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9',
                          'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        self.assertEqual(expected_peers, utils.cross(self.rows, self.cols))

if __name__ == '__main__':
    unittest.main()