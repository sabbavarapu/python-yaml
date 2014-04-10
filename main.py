#!/usr/bin/python
# coding=utf-8

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
        version='%(prog)s 0.0.1')

    # process command line arguments
    args = parser.parse_args()
    prog = parser.prog
    infile = args.infile
    verbose = args.verbose

    # show command parameters
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # load employees from YAML
    e = Employees(infile)

    logging.debug("infile ......................: %s" % (infile.name))
    logging.debug("prog ........................: %s" % (prog))
    logging.debug("verbose .....................: %s" % (verbose))

    t = e.getName(3)
    logging.debug("name for id 3 ...............: %s" % t)

    t = e.getName(4)
    logging.debug("name for id 4 ...............: %s" % t)

    t = e.getByName('frank')
    # s = "${:,}".format(t)
    logging.debug("turnover for frank ..........: ${:,}".format(t))

    t = e.getByYear('frank', 2012)
    # s = "${:,}".format(t)
    logging.debug("turnover for frank in 2012 ..: ${:,}".format(t))

    t = e.getAllByYear(2012)
    # s = "${:,}".format(t)
    logging.debug("turnover for all in 2012 ....: ${:,}".format(t))

    t = list(e.listByName('frank'))
    logging.debug("list frank years ............: %s" % t)

    t = list(e.listByYear(2013))
    logging.debug("list turnover for 2013 ......: %s" % t)

    t = e.listByYear(1999)
    logging.debug("expect none for 1999 ........: %s" % t)


#
# MAIN
#
if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)

#EOF
