import os
import unittest
from src.config_xml import ConfigXML

__author__ = 'Carlos Gonzales'


class TestConfigXML(unittest.TestCase):

    config_xml = ConfigXML("../config.xml")

    def test_verify_if_config_xml_exist(self):
        self.assertTrue(os.path.exists(self.config_xml.file_name))

    def test_verify_that_is_possible_to_get_the_output_value(self):
        self.assertEqual("c:\\", self.config_xml.get_node("value", ".//path_output"))

    def test_verify_that_is_possible_to_get_the_algorithm_solve_value(self):
        self.assertEqual("backtracking", self.config_xml.get_node("value", ".//algorithm"))

    def test_verify_that_is_possible_to_get_the_difficulty_value(self):
        self.assertEqual("custom", self.config_xml.get_node("value", ".//difficulty/level"))

    def test_verify_that_is_possible_to_get_the_levels_limits_min(self):
        self.assertEqual("20", self.config_xml.get_node("min", ".//difficulty/level/limits_holes"))

    def test_verify_that_is_possible_to_get_the_levels_limits_max(self):
        self.assertEqual("60", self.config_xml.get_node("max", ".//difficulty/level/limits_holes"))

    def test_verify_that_is_possible_to_set_the_output_value(self):
        new_output = "c:\\Test"
        self.config_xml.set_node("value", ".//path_output", new_output)
        self.assertEqual(new_output, self.config_xml.get_node("value", ".//path_output"))

    def test_verify_that_is_possible_to_set_the_algorithm_solve_value(self):
        new_algorithm = "peter_norving"
        self.config_xml.set_node("value", ".//algorithm", new_algorithm)
        self.assertEqual(new_algorithm, self.config_xml.get_node("value", ".//algorithm"))

    def test_verify_that_is_possible_to_set_the_difficulty_value(self):
        new_difficulty = "easy"
        self.config_xml.set_node("value", ".//difficulty/level", new_difficulty)
        self.assertEqual(new_difficulty, self.config_xml.get_node("value", ".//difficulty/level"))

    def test_verify_that_is_possible_to_set_the_levels_limits_min(self):
        new_min_limit_holes = "30"
        self.config_xml.set_node("min", ".//difficulty/level/limits_holes", new_min_limit_holes)
        self.assertEqual(new_min_limit_holes, self.config_xml.get_node("min", ".//difficulty/level/limits_holes"))

    def test_verify_that_is_possible_to_set_the_levels_limits_max(self):
        new_max_limit_holes = "70"
        self.config_xml.set_node("max", ".//difficulty/level/limits_holes", new_max_limit_holes)
        self.assertEqual(new_max_limit_holes, self.config_xml.get_node("max", ".//difficulty/level/limits_holes"))

if __name__ == '__main__':
    unittest.main()