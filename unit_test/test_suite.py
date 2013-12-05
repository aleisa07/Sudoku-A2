from coverage import coverage
cov = coverage()
cov.start()

import unittest
from test_backtracking_algorithm import testBacktracking
from test_cell import TestCell
from test_norvig_algorithm import TestNorvigAlgorithm
from test_config_xml_get import TestConfigXMLGet
from test_config_xml_set import TestConfigXMLSet
from test_generator import TestGenerator
from test_input import TestInput
from test_logger import TestLogger
from test_utils import TestUtilsMethods


suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(testBacktracking))
suite.addTests(unittest.makeSuite(TestCell))
suite.addTests(unittest.makeSuite(TestNorvigAlgorithm))
suite.addTests(unittest.makeSuite(TestConfigXMLGet))
suite.addTests(unittest.makeSuite(TestConfigXMLSet))
suite.addTests(unittest.makeSuite(TestGenerator))
suite.addTests(unittest.makeSuite(TestInput))
suite.addTests(unittest.makeSuite(TestLogger))
suite.addTests(unittest.makeSuite(TestUtilsMethods))

unittest.TextTestRunner(verbosity=2).run(suite)
cov.stop()
cov.html_report(directory='coverage_report')