#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)

    def testLoadByFile(self):
        e = Employees(file(self.TEST_FILE))
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
        self.assertEquals(440000, e.getByName('frank'))
        self.assertEquals(560000, e.getByName('jo'))

    def testByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEquals(100000, e.getByYear(name='frank', year=2011))
        self.assertEquals(140000, e.getByYear(name='frank', year=2012))
        self.assertEquals(200000, e.getByYear(name='frank', year=2013))
        self.assertEquals(130000, e.getByYear(name='jo', year=2012))
        self.assertEquals(220000, e.getByYear(name='jo', year=2013))
        self.assertEquals(210000, e.getByYear(name='jo', year=2014))

    def testAllByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEquals(100000, e.getAllByYear(2011))
        self.assertEquals(270000, e.getAllByYear(2012))
        self.assertEquals(420000, e.getAllByYear(2013))
        self.assertEquals(210000, e.getAllByYear(2014))

    def testListByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        turnover = list(e.listByYear(2013))
        self.assertEquals(2, len(turnover))
        self.assertIn(200000, turnover)
        self.assertIn(220000, turnover)
        self.assertNotIn(2013, turnover)

    def testListByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        years = list(e.listByName('frank'))
        self.assertEquals(3, len(years))
        self.assertIn(2011, years)
        self.assertIn(2012, years)
        self.assertIn(2013, years)
        self.assertNotIn(2014, years)

    def testBadId(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getName(1))

    def testBadByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getByName('badname'))

    def testBadNameByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.getByYear(name='badname', year=2012))

    def testBadYearByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(0, e.getByYear(name='frank', year=1999))

    def testBadAllByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertEqual(0, e.getAllByYear(1999))

    def testBadListByYear(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.listByYear(1999))

    def testBadListByName(self):
        e = Employees(self.TEST_FILE)
        self.assertIsNotNone(e)
        self.assertIsNone(e.listByName('badname'))

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
