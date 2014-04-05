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

    def testLoadFromFile1(self):
        employees = Employees()
        employees.loadFromFile(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')

    def testLoadFromFile2(self):
        employees = Employees()
        employees.loadFromFile(file(self.TEST_FILE))
        self.assertIsNotNone(employees, 'expected employees')

    def testDump(self):
        employees = Employees(self.TEST_FILE)
        dump = employees.dump()
        count = len(dump.split('\n'))
        self.assertEqual(count, 15, "expected %i lines dump, got %i"
                         % (15, count))

    def testTurnoverByName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        years = employees.getByName('frank')
        self.assertEqual(len(years), 3)
        total = 0
        for y in years:
            total += y['value']
        self.assertEqual(total, 100000 + 140000 + 200000)

    def testNoName(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        self.assertIsNone(employees.getByName('badname'))

    def testNameContains(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        expected = {'value': 210000, 'year': 2014}
        years = employees.getByName('jo')
        self.assertTrue(any(True for expected in years),
                        "expected to find %s" % (expected))

    def testIdContains(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        expected = {'value': 210000, 'year': 2014}
        years = employees.getById(004)
        self.assertTrue(any(True for expected in years),
                        "expected to find %s" % (expected))

    def testNoId(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        self.assertIsNone(employees.getById(001))

    def testTurnoverByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getByYear(name='frank', year=2012)
        self.assertEqual(turnover, 140000)

    def testTurnoverAllByYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
        turnover = employees.getAllByYear(2012)
        self.assertEqual(turnover, 270000)

    def testNoYear(self):
        employees = Employees(self.TEST_FILE)
        self.assertIsNotNone(employees, 'expected employees')
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
