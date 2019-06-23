#!/usr/bin/env python
# coding: utf-8

"""
Run unit tests for YAML file processing example, Employees.
"""

import os
import unittest
from employees.employees import Employees


class TestEmployees(unittest.TestCase):

    """ Tests for Employees. """

    __version__ = Employees.__version__

    TEST_FILE = 'test/test.yaml'

    @classmethod
    def setUpClass(cls):
        print(cls.__name__, cls.__version__)

    def setUp(self):
        testFile = os.path.join(os.getcwd(), self.TEST_FILE)
        self.assertTrue(os.access(testFile, os.R_OK))

    def testLoadByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)

    def testLoadByFile(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)

    def testDump(self):
        e = Employees(self.TEST_FILE)
        dump = e.dump()
        self.assertTrue(7, len(dump.split('\n')))
        self.assertIn('frank:', dump)
        self.assertIn('jo:', dump)

    def testName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual('frank', e.getName(3))
        self.assertEqual('jo', e.getName(4))

    def testByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(440000, e.getByName('frank'))
        self.assertEqual(560000, e.getByName('jo'))

    def testForNameByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(100000, e.getForNameByYear(name='frank', year=2011))
        self.assertEqual(140000, e.getForNameByYear(name='frank', year=2012))
        self.assertEqual(200000, e.getForNameByYear(name='frank', year=2013))
        self.assertEqual(130000, e.getForNameByYear(name='jo', year=2012))
        self.assertEqual(220000, e.getForNameByYear(name='jo', year=2013))
        self.assertEqual(210000, e.getForNameByYear(name='jo', year=2014))

    def testByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(100000, e.getByYear(2011))
        self.assertEqual(270000, e.getByYear(2012))
        self.assertEqual(420000, e.getByYear(2013))
        self.assertEqual(210000, e.getByYear(2014))

    def testListById(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        turnovers = list(e.listById(3))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def testListByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        turnovers = list(e.listByName('frank'))
        self.assertEqual(3, len(turnovers))
        self.assertIn(100000, turnovers)
        self.assertIn(140000, turnovers)
        self.assertIn(200000, turnovers)
        self.assertNotIn(220000, turnovers)

    def testListByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        turnover = list(e.listByYear(2013))
        self.assertEqual(2, len(turnover))
        self.assertIn(200000, turnover)
        self.assertIn(220000, turnover)
        self.assertNotIn(2013, turnover)

    def testBadId(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getName(1))

    def testBadById(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getById(1))

    def testBadByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getByName('badname'))

    def testBadByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(0, e.getByYear(1999))

    def testBadForNameByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getForNameByYear('frank', 1999))
        self.assertIsNone(e.getForNameByYear('jo', 1999))
        self.assertIsNone(e.getForNameByYear('badname', 2011))
        self.assertIsNone(e.getForNameByYear('badname', 2012))
        self.assertIsNone(e.getForNameByYear('badname', 2013))
        self.assertIsNone(e.getForNameByYear('badname', 2014))

    def testBadListById(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.listById(1))

    def testBadListByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.listByName('badname'))

    def testBadListByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.listByYear(1999))

    def tearDown(self):
        pass


#
# MAIN
#
if __name__ == '__main__':
    # to get verbose output use '-v' option
    unittest.main()
    # the following gives verbose output by default
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployees)
    # unittest.TextTestRunner(verbosity=2).run(suite)

# EOF
