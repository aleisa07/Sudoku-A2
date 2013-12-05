import sys
sys.path.append('../src')

from constant import *
import utils
import unittest
from config_xml import ConfigXML

__author__ = 'Carlos Gonzales'


class TestConfigXMLGet(unittest.TestCase):

    def setUp(self):
        self.config_xml = ConfigXML("config.xml")

    def test_verify_if_config_xml_exist(self):
        self.assertTrue(utils.exist_path(self.config_xml.file_name))

    def test_verify_that_is_possible_to_get_the_output_value(self):
        expected_value = "c:\\"
        attribute = "value"
        self.assertEqual(expected_value,
                         self.config_xml.get_node(attribute, XPATH_OUTPUT))

    def test_verify_that_is_possible_to_get_the_algorithm_solve_value(self):
        expected_value = ALGORITHM_BACKTRACKING
        attribute = "value"
        self.assertEqual(expected_value,
                         self.config_xml.get_node(attribute, XPATH_ALGORITHM))

    def test_verify_that_is_possible_to_get_the_difficulty_value(self):
        expected_value = LEVEL_CUSTOM
        attribute = "value"
        self.assertEqual(expected_value,
                         self.config_xml.get_node(attribute, XPATH_LEVEL))

    def test_verify_that_is_possible_to_get_the_levels_limits_min(self):
        expected_value = "20"
        attribute = "min"
        self.assertEqual(expected_value,
                         self.config_xml.get_node(attribute,
                                                  XPATH_HOLES_NUMBER))

    def test_verify_that_is_possible_to_get_the_levels_limits_max(self):
        expected_value = "60"
        attribute = "max"
        self.assertEqual(expected_value,
                         self.config_xml.get_node(attribute,
                                                  XPATH_HOLES_NUMBER))

if __name__ == '__main__':
    unittest.main()