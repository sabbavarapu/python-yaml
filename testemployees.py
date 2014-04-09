#!/usr/bin/python
# coding=utf-8

"""
Run unit tests for YAML file processing example, Employees.
"""

from employees import Employees
import os
import unittest


class TestEmployees(unittest.TestCase):

    """ Tests for Employees. """

    TEST_FILE = 'test.yml'

    def setUp(self):
        testFile = os.path.join(os.getcwd(), self.TEST_FILE)
        self.assertTrue(os.access(testFile, os.R_OK))

    def testLoadByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)

    def testLoadByFile(self):
        employees = Employees(file(self.TEST_FILE))
        self.assertIsNotNone(employees)

    def testDump(self):
        employees = Employees(self.TEST_FILE)
        dump = employees.dump()
        self.assertTrue(7, len(dump.split('\n')))
        self.assertIn('frank:', dump)
        self.assertIn('jo:', dump)

    def testByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertTrue(440000, employees.getByName('frank'))
        self.assertTrue(560000, employees.getByName('jo'))

    def testName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual('frank', employees.getName(3))
        self.assertEqual('jo', employees.getName(4))

    def testByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertTrue(100000, employees.getByYear(name='frank', year=2011))
        self.assertTrue(140000, employees.getByYear(name='frank', year=2012))
        self.assertTrue(200000, employees.getByYear(name='frank', year=2013))
        self.assertTrue(130000, employees.getByYear(name='jo', year=2012))
        self.assertTrue(220000, employees.getByYear(name='jo', year=2013))
        self.assertTrue(210000, employees.getByYear(name='jo', year=2014))

    def testAllByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertTrue(100000, employees.getAllByYear(2011))
        self.assertTrue(270000, employees.getAllByYear(2012))
        self.assertTrue(420000, employees.getAllByYear(2013))
        self.assertTrue(210000, employees.getAllByYear(2014))

    def testBadId(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getName(1))

    def testBadGetByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getByName('badname'))

    def testBadAllByYearName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getByYear(name='badname', year=2012))

    def testBadAllByYearYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertEqual(0, employees.getAllByYear(1999))

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

#EOF
