.. _main:

Main
====

.. automodule:: employees.main
   :members:

Help on module :download:`main <../employees/main.py>`::

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

The :download:`main <../employees/main.py>` module exists just to test the
:ref:`employees` class from command line.

There is also help using the ``-h`` option::

    python main.py -h
    usage: main.py [options]

    a Python example program to show YAML processing

    positional arguments:
    infile         alternate YAML file to test

    optional arguments:
    -h, --help     show this help message and exit
    -v, --verbose  verbose output
    --version      show program's version number and exit

    © 2014 Frank H Jung mailto:frankhjung@linux.com


.. EOF
