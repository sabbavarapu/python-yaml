.. _main:

This is an example `Python <references>`_ project used to demonstrate:

* documentation using `Sphinx <references>`_
* example processing a YAML file using `PyYAML <references>`_
* module help using `PyDoc <references>`_
* unit tests using `unittest framework <references>`_
* code coverage using `python-coverage <references>`_
* code style checks using `PEP8 <references>`_
* the project is managed using `GNU Make <references>`_

Main
====

Module help:

.. code::

   NAME
      main

   FILE
      main.py

   DESCRIPTION
      Read Employee data to return turnover information.
      This is a example Python program to read and process YAML files.

   FUNCTIONS
      main(argv)
         Test employees class.


The module :download:`main.py <../main.py>` exists just to run the
:ref:`employees` class from command line.

There is also help using the ``-h`` option::

    usage: main.py [options] infile

    a Python example program to show YAML processing

    positional arguments:
      infile         alternate YAML file to test

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  verbose output
      --version      show program's version number and exit

    © 2014 Frank H Jung mailto:frankhjung@linux.com


Coverage
--------

Here is the `coverage report for main.py <_static/index.html>`_.
    

.. EOF
