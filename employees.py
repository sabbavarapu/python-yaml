#!/usr/bin/python
# coding=utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""


class Employees:

    """ Read Employee data to return turnover information. """

    def __init__(self, infile=None):
        self.employees = None
        if infile is not None:
            self.loadFromFile(infile)

    def loadFromFile(self, infile):
        from yaml import load
        if isinstance(infile, file):
            self.employees = load(infile)
        else:
            self.employees = load(file(infile))

    def dump(self):
        from yaml import dump
        return dump(self.employees, encoding=('utf-8'))

    def getById(self, eid):
        """ Returns turnover for all years for an employee. """
        t = [self.getByName(e) for e in self.employees.keys() if
             self.employees.get(e).get('id') == int(eid)]
        # return None if no entries for this Id
        return t and t[0] or None

    def getByName(self, name):
        """ Returns turnover for all years for an employee. """
        if self.employees.get(name):
            total = 0
            for t in self.employees.get(name).get('turnover'):
                total += sum(t.values())
        else:
            total = None
        # return None if no entries for this name
        return total

    def getByYear(self, name, year):
        """ Returns turnover for an employees by year. """
        if self.employees.get(name):
            total = 0
            for t in self.employees.get(name).get('turnover'):
                if t.get(year):
                    total += sum(t.values())
        else:
            total = None
        # return None if no entries for this name
        return total

    def getAllByYear(self, year):
        """ Returns turnover for all employees by year. """
        count = 0
        total = 0
        for n in self.employees.values():
            for t in n.get('turnover'):
                if t.get(year):
                    total += sum(t.values())
                    count += 1
        # return None if no entries for this year
        return count and total or None

#EOF
