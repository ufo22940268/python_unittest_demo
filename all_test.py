__author__ = 'cc'

import unittest
from test_a import TestA
from test_b import TestB


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTests([unittest.makeSuite(TestA), unittest.makeSuite(TestB)])
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
