#!/usr/bin/python
# coding=utf-8

"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

import argparse
from employees import Employees
import os.path
import sys


def main(argv=sys.argv):

    """ Test employees class. """

    parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        usage='%(prog)s [options]',
        description='a Python example program to show YAML processing',
        epilog='© 2014 Frank H Jung mailto:frankhjung@linux.com')
    parser.add_argument(
        'infile',
        nargs='?',
        type=argparse.FileType('r'),
        default='test.yml',
        help='alternate YAML file to test')
    parser.add_argument(
        '-v',
        '--verbose',
        help='verbose output',
        action='count')
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.0.1')

    # process command line arguments
    args = parser.parse_args()
    prog = parser.prog
    infile = args.infile
    verbose = args.verbose

    # load employees from YAML
    employees = Employees(infile)

    # show command parameters
    if verbose:
        print "\nShow command line parameters ..."
        print "\tinfile = %s" % (infile.name)
        print "\tprog = %s" % (prog)
        print "\tverbose = %s" % (verbose)
        print "\tdata:\n%s" % (infile.read())

    print "\nDump YAML document ..."
    print employees.dump()

    print "Python type of employees ..............:", type(employees.employees)

    t = employees.getByName('frank')
    print "Turnover for employee name 'frank' ....: %s" % ("${:,}".format(t))

    t = employees.getById(4)
    print "Turnover for employee id 4 ............: %s" % ("${:,}".format(t))

    t = employees.getByYear('frank', 2012)
    print "Turnover for employee 'frank' in 2012 .: %s" % ("${:,}".format(t))

    t = employees.getAllByYear(2012)
    print "Turnover for all in 2012 ..............: %s" % ("${:,}".format(t))


#
# MAIN
#
if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)

#EOF
