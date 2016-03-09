#!/usr/bin/env python
# coding: utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""


class Employees:

    """ Read Employee data to return turnover information. """

    __version__ = '0.2.0'

    def __init__(self, infile=None):
        self.employees = None
        if infile is not None:
            self.load(infile)

    def filterById(self, eid):
        """ filter by id
        :param eid:
        """
        for n in self.employees.keys():
            if eid == self.employees.get(n).get('id'):
                for t in self.employees.get(n).get('turnover'):
                    yield self.employees.get(n).get('turnover').get(t)

    def filterByName(self, name):
        """ filter by name
        :param name:
        """
        for t in self.employees.get(name).get('turnover'):
            yield self.employees.get(name).get('turnover').get(t)

    def filterByYear(self, year):
        """ filter by year
        :param year:
        """
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
        return dump(self.employees, encoding='utf-8')

    def getName(self, eid):
        """ Returns name of employee by id.
        :param eid:
        """
        name = None
        for n in self.employees.keys():
            if eid == self.employees.get(n).get('id'):
                name = n
                break
        return name

    def getById(self, eid):
        """ Returns turnover for all years for an employee by id.
        :param eid:
        """
        turnovers = list(self.filterById(eid))
        if len(turnovers) > 0:
            total = sum(turnovers)
        else:
            total = None
        return total

    def getByName(self, name):
        """ Returns turnover for all years for an employee by name.
        :param name:
        """
        if name in self.employees.keys():
            total = sum(self.filterByName(name))
        else:
            total = None
        return total

    def getByYear(self, year):
        """ Returns turnover for all employees by year.
        :param year:
        """
        total = sum(self.filterByYear(year))
        return total

    def getForNameByYear(self, name, year):
        """ Returns turnover for an employee for a specific year.
        :param year:
        :param name:
        """
        if name in self.employees.keys():
            turnovers = list(self.employees.get(name).get('turnover').get(t)
                             for t in self.employees.get(name).get('turnover')
                             if t == year)
            if len(turnovers) > 0:
                total = sum(turnovers)
            else:
                total = None
        else:
            total = None
        return total

    def listById(self, eid):
        """ List turnover by id.
        :param eid:
        """
        turnovers = list(self.filterById(eid))
        if len(turnovers) > 0:
            pass
        else:
            turnovers = None
        return turnovers

    def listByName(self, name):
        """ List turnover by name.
        :param name:
        """
        if name in self.employees.keys():
            turnovers = list(self.filterByName(name))
        else:
            turnovers = None
        return turnovers

    def listByYear(self, year):
        """ List turnover by year.
        :param year:
        """
        turnovers = list(self.filterByYear(year))
        if len(turnovers) > 0:
            pass
        else:
            turnovers = None
        return turnovers

# EOF
