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
            self.load(infile)

    def load(self, infile):
        from yaml import load
        if isinstance(infile, file):
            self.employees = load(infile)
        else:
            self.employees = load(file(infile))

    def dump(self):
        from yaml import dump
        return dump(self.employees, encoding=('utf-8'))

    def getName(self, eid):
        """ Returns name of employee by id. """
        name = None
        for n in self.employees.keys():
            if eid == self.employees.get(n).get('id'):
                name = n
                break
        return name

    def getByName(self, name):
        """ Returns turnover for all years for an employee. """
        try:
            total = 0
            for t in self.employees.get(name).get('turnover'):
                total += self.employees.get(name).get('turnover').get(t)
        except:
            total = None
        return total

    def getByYear(self, name, year):
        """ Returns turnover for an employees by year. """
        try:
            total = sum(list(self.employees.get(name).get('turnover').get(t)
                for t in self.employees.get(name).get('turnover')
                if t == year))
        except:
            total = None
        return total

    def getAllByYear(self, year):
        """ Returns turnover for all employees by year. """
        total = 0
        for name in self.employees.keys():
            total += self.getByYear(name, year)
        return total

#EOF
