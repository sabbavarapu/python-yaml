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
        count = len(dump.split('\n'))
        self.assertEqual(
            count, 13, "expected %i lines dump, got %i" % (13, count))

    def testTurnoverByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        total = employees.getByName('frank')
        self.assertEqual(total, 100000 + 140000 + 200000)

    def testTurnoverById(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        total = employees.getById(4)
        self.assertEqual(total, 130000 + 220000 + 210000)

    def testTurnoverByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnover = employees.getByYear(name='frank', year=2012)
        self.assertEqual(turnover, 140000)

    def testTurnoverAllByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnover = employees.getAllByYear(2012)
        self.assertEqual(turnover, 270000)

    def testBadId(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getById(001))

    def testBadGetByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getByName('badname'))

    def testBadByYearName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        self.assertIsNone(employees.getByYear(name='badname', year=2012))

    def testBadYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees)
        turnover = employees.getAllByYear(2001)
        self.assertIsNone(turnover)

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
