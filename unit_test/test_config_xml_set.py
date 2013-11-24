import unittest
from src.config_xml import ConfigXML
from src.constant import *

__author__ = 'Carlos Gonzales'


class TestConfigXML(unittest.TestCase):
    def setUp(self):
        self.config_xml = ConfigXML("config_set.xml")

    def test_verify_that_is_possible_to_set_the_output_value(self):
        new_output = "c:\\Test"
        attribute = "value"
        self.config_xml.set_node(attribute, XPATH_OUTPUT, new_output)
        self.assertEqual(new_output,
                         self.config_xml.get_node(attribute, XPATH_OUTPUT))

    def test_verify_that_is_possible_to_set_the_algorithm_solve_value(self):
        new_algorithm = ALGORITHM_NORVIG
        attribute = "value"
        self.config_xml.set_node(attribute, XPATH_ALGORITHM, new_algorithm)
        self.assertEqual(new_algorithm,
                         self.config_xml.get_node(attribute, XPATH_ALGORITHM))

    def test_verify_that_is_possible_to_set_the_difficulty_value(self):
        new_difficulty = LEVEL_EASY
        attribute = "value"
        self.config_xml.set_node(attribute, XPATH_LEVEL, new_difficulty)
        self.assertEqual(new_difficulty,
                         self.config_xml.get_node(attribute, XPATH_LEVEL))

    def test_verify_that_is_possible_to_set_the_levels_limits_min(self):
        new_min_limit_holes = "30"
        attribute = "min"
        self.config_xml.set_node(attribute, XPATH_HOLES_NUMBER,
                                 new_min_limit_holes)
        self.assertEqual(new_min_limit_holes,
                         self.config_xml.get_node(attribute,
                                                  XPATH_HOLES_NUMBER))

    def test_verify_that_is_possible_to_set_the_levels_limits_max(self):
        new_max_limit_holes = "70"
        attribute = "max"
        self.config_xml.set_node(attribute, XPATH_HOLES_NUMBER,
                                 new_max_limit_holes)
        self.assertEqual(new_max_limit_holes,
                         self.config_xml.get_node(attribute,
                                                  XPATH_HOLES_NUMBER))

if __name__ == '__main__':
    unittest.main()