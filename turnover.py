#!/usr/bin/python
# coding=utf-8

"""
Represents Employee turnover.
"""


class Turnover:

    """ Represents Employee turnover data. """

    def __init__(self, name=None, id=None):
        self.turnover = {'name': name, 'id': id, 'data': []}

    def setName(self, name):
        self.turnover['name'] = name

    def name(self):
        return self.turnover['name']

    def setId(self, id):
        self.turnover['id'] = id

    def id(self):
        return self.turnover['id']

    def append(self, data):
        self.turnover['data'].append(data)

    def year(self, year):
        """ Returns turnover for a specific year. """
        total = sum([t.values()[0]
            for t in self.turnover.get('data')
            if year == t.keys()[0]])
        return total

    def total(self):
        """ Returns turnover for all years. """
        total = sum([t.values()[0]
            for t in self.turnover.get('data')])
        return total

    def dump(self):
        return self.turnover

#EOF
