#!/usr/bin/python
# coding=utf-8

from turnover import Turnover


class Turnovers(object):

    """ Read turnover data for each employee. """

    def __init__(self, infile=None):
        self.employees = None
        self.years = None
        if infile:
            self.load(infile)

    def load(self, infile):
        from yaml import load
        self.employees = []
        self.years = []
        if isinstance(infile, file):
            employees = load(infile)
            for e in employees:
                t = {}
                t['name'] = e
                t['id'] = employees.get(e).get('id')
                t['turnover'] = []
                for to in employees.get(e).get('turnover'):
                    t['turnover'].append(to)
                self.years.extend(t['turnover'])
                self.employees.append(t)

    def total(self, year):
        return sum(list(y.values()[0] for y in self.years if y.keys()[0] == year))

    def dump(self):
        return self.employees

#EOF
