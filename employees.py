#!/usr/bin/python
# coding=utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""


class Employees:

    """
    Read Employee data to return turnover information.
    """

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

    def getById(self, id):
        """ Returns turnover for all years for an employee. """
        for e in self.employees:
            if e['employee']['id'] == id:
                return e['employee']['turnover']

    def getByName(self, name):
        """ Returns turnover for all years for an employee. """
        for e in self.employees:
            if e['employee']['name'] == name:
                return e['employee']['turnover']

    def getByYear(self, name, year):
        """ Returns turnover for an employees by year. """
        years = self.getByName(name)
        for y in years:
            if y['year'] == int(year):
                return y['value']

    def getAllByYear(self, year):
        """ Returns turnover for all employees by year. """
        total = 0
        for e in self.employees:
            for y in e['employee']['turnover']:
                if y['year'] == int(year):
                    total += y['value']
        return total

#EOF
