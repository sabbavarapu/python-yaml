#!/usr/bin/python
# coding=utf-8

"""
Run unit tests for YAML file processing example, Employees.
"""

from turnover import Turnover
import unittest


class TestTurnover(unittest.TestCase):

    """ Tests for Employees. """

    TEST_TURNOVER = {
        'name': "frank",
        'id': 3,
        'data': [{2011: 100000}, {2012: 140000}, {2013: 200000}]}

    def setUp(self):
        pass

    def testDump(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        for d in self.TEST_TURNOVER['data']:
            turnover.add(d)
        self.assertEqual(self.TEST_TURNOVER, turnover.dump())

    def testStr(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        for d in self.TEST_TURNOVER['data']:
            turnover.add(d)
        self.assertEqual(str(self.TEST_TURNOVER), str(turnover))

    def testName(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        self.assertEqual('frank', turnover.name)

    def testId(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        self.assertEqual(3, turnover.id)

    def testYear(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        for d in self.TEST_TURNOVER['data']:
            turnover.add(d)
        self.assertEquals(140000, turnover.year(2012))

    def testTotal(self):
        turnover = Turnover()
        turnover.name = self.TEST_TURNOVER['name']
        turnover.id = self.TEST_TURNOVER['id']
        for d in self.TEST_TURNOVER['data']:
            turnover.add(d)
        self.assertEquals(440000, turnover.total())

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
