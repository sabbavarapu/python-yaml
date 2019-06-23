.. _main:

This is an example `Python <references.html>`_ project used to demonstrate:

* documentation using `Sphinx <references.html>`_
* example processing a YAML file using `PyYAML <references.html>`_
* module help using `PyDoc <references.html>`_
* unit tests using `unittest framework <references.html>`_
* code coverage using `python-coverage <references.html>`_
* code style checks using `PEP8 <references.html>`_
* the project is managed using `GNU Make <references.html>`_

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

Here is the `coverage report <_static/index.html>`_.
    

.. EOF
