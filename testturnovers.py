#!/usr/bin/python
# coding=utf-8

from turnovers import Turnovers
from turnover import Turnover
import os
import unittest


class TestTurnovers(unittest.TestCase):

    """ Unit tests for YAML file processing example. """

    TEST_FILE = 'test.yml'

    def setUp(self):
        testFile = os.path.join(os.getcwd(), self.TEST_FILE)
        self.assertTrue(os.access(testFile, os.R_OK))

    def testName(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertIn('frank', [t['name'] for t in turnovers.employees])
        self.assertIn('jo', [t['name'] for t in turnovers.employees])

    def testBadName(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertNotIn('bond', [t['name'] for t in turnovers.employees])

    def testId(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertIn(3, [t['id'] for t in turnovers.employees])
        self.assertIn(4, [t['id'] for t in turnovers.employees])

    def testBadId(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertNotIn(007, [t['id'] for t in turnovers.employees])

    def testTotals(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertTrue(100000, turnovers.total(2011))
        self.assertTrue(270000, turnovers.total(2012))
        self.assertTrue(420000, turnovers.total(2013))
        self.assertTrue(210000, turnovers.total(2014))

    def testBadYear(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertEqual(0, turnovers.total(2001))

    def testLoad(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertIsNotNone(turnovers)
        self.assertEqual(2, len(turnovers.employees))

    def testDump(self):
        turnovers = Turnovers(file(self.TEST_FILE))
        self.assertIsNotNone(turnovers.dump())
        self.assertEqual(2, len(turnovers.dump()))

    def tearDown(self):
        pass


#
# MAIN
#
if __name__ == '__main__':
    # to get verbose output use '-v' option
    unittest.main()
    # the following gives verbose output by default
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestTurnovers)
    # unittest.TextTestRunner(verbosity=2).run(suite)

#EOF
