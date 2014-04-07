#!/usr/bin/python
# coding=utf-8

"""
Represents Employee turnover.
"""


class Turnover:

    """ Represents Employee turnover data. """

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id
        # list of dictionaries {year: value}
        self.data = []

    def __str__(self):
        return str(self.dump())

    def add(self, data):
        self.data.append(data)

    def year(self, year):
        """ Returns turnover for a specific year. """
        total = sum([t.values()[0] for t in self.data if year == t.keys()[0]])
        return total

    def total(self):
        """ Returns turnover for all years. """
        total = sum([t.values()[0] for t in self.data])
        return total

    def dump(self):
        return {'name': self.name, 'id': self.id, 'data': self.data}

#EOF
