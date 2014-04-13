#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

from employees import Employees
import argparse
import logging
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
        version='%(prog)s 0.1.0')

    # process command line arguments
    args = parser.parse_args()
    prog = parser.prog
    infile = args.infile
    verbose = args.verbose

    # show command parameters
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)
    if verbose:
        logger.setLevel(logging.DEBUG)

    # load employees from YAML
    e = Employees(infile)

    logger.debug("infile ......................: {s}".format(s=infile.name))
    logger.debug("prog ........................: {s}".format(s=prog))
    logger.debug("verbose .....................: {s}".format(s=verbose))
    logger.debug("employees ...................: {s}".format(s=e.employees))

    t = e.getName(3)
    logger.debug("name for id 3 ...............: {s}".format(s=t))

    t = e.getById(3)
    logger.debug("turnover for 3 ..............: ${:,}".format(t))

    t = e.getByName('frank')
    logger.debug("turnover for frank ..........: ${:,}".format(t))

    t = e.getByYear(2012)
    logger.debug("turnover for 2012 ...........: ${:,}".format(t))

    t = list(e.listById(3))
    logger.debug("list turnover by id .........: {s}".format(s=t))

    t = list(e.listByName('frank'))
    logger.debug("list turnover by name .......: {s}".format(s=t))

    t = list(e.listByYear(2013))
    logger.debug("list turnover by year .......: {s}".format(s=t))

    return 0


#
# MAIN
#
if __name__ == '__main__':
    rc = main(sys.argv)
    sys.exit(rc)

#EOF
