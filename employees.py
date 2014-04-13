#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    def filterByName(self, name):
        """ filter by name """
        for t in self.employees.get(name).get('turnover'):
            yield t

    def filterByYear(self, year):
        """ filter by year """
        for n in self.employees.keys():
            if year in self.employees.get(n).get('turnover'):
                yield self.employees.get(n).get('turnover').get(year)

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
        if not name in self.employees.keys():
            total = None
        else:
            total = sum(self.employees.get(name).get('turnover').get(t)
                        for t in self.filterByName(name))
        #try:
        #    total = sum(self.employees.get(name).get('turnover').get(t)
        #                for t in self.filterByName(name))
        #except:
        #    total = None
        return total

    def listByYear(self, year):
        """ List turnover by year. """
        turnovers = list(self.filterByYear(year))
        if not turnovers:
            turnovers = None
        return turnovers

    def listByName(self, name):
        """ List turnover by employee. """
        if not name in self.employees.keys():
            years = None
        else:
            years = list(self.filterByName(name))
        #try:
        #    years = list(self.filterByName(name))
        #except:
        #    years = None
        return years

    def getByYear(self, name, year):
        """ Returns turnover for an employees by year. """
        if not name in self.employees.keys():
            total = None
        else:
            total = sum(self.employees.get(name).get('turnover').get(t)
                        for t in self.filterByName(name)
                        if t == year)
        #try:
        #    total = sum(self.employees.get(name).get('turnover').get(t)
        #                for t in self.filterByName(name)
        #                if t == year)
        #except:
        #    total = None
        return total

    def getAllByYear(self, year):
        """ Returns turnover for all employees by year. """
        # from functools import reduce
        total = sum(self.getByYear(name, year)
                    for name in self.employees.keys())
        return total

#EOF
