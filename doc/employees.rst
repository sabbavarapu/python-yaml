.. _employees:

Employees
=========

Help on module employees::

    NAME
        employees

    FILE
        employees.py

    DESCRIPTION
        Read Employee data to return turnover information.
        This is a example Python program to read and process YAML files.

    CLASSES
        Employees
        
        class Employees
        |  Read Employee data to return turnover information.
        |  
        |  Methods defined here:
        |  
        |  __init__(self, infile=None)
        |  
        |  dump(self)
        |  
        |  filterByName(self, name)
        |      filter by name
        |  
        |  filterByYear(self, year)
        |      filter by year
        |  
        |  getAllByYear(self, year)
        |      Returns turnover for all employees by year.
        |  
        |  getByName(self, name)
        |      Returns turnover for all years for an employee.
        |  
        |  getByYear(self, name, year)
        |      Returns turnover for an employees by year.
        |  
        |  getName(self, eid)
        |      Returns name of employee by id.
        |  
        |  listByName(self, name)
        |      List turnover by employee.
        |  
        |  listByYear(self, year)
        |      List turnover by year.
        |  
        |  load(self, infile)


.. automodule:: employees
   :members:

.. EOF
