.. _unittest:

Unit Tests
==========

Here I am using the default Python :ref:`unittest <references>` suite. A list
of unit test assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using::

    python-coverage run -a --include=testemployees.py,employees.py testemployees.py

Or::

    python -m unittest discover -v

Or::

	unit2 discover -v

The basic report of unit test results is::

    testDump (testemployees.TestEmployees) ... ok
    testIdContains (testemployees.TestEmployees) ... ok
    testLoadFromFile1 (testemployees.TestEmployees) ... ok
    testLoadFromFile2 (testemployees.TestEmployees) ... ok
    testNameContains (testemployees.TestEmployees) ... ok
    testNoId (testemployees.TestEmployees) ... ok
    testNoName (testemployees.TestEmployees) ... ok
    testTurnoverAllByYear (testemployees.TestEmployees) ... ok
    testTurnoverByName (testemployees.TestEmployees) ... ok
    testTurnoverByYear (testemployees.TestEmployees) ... ok
    testZeroTurnover (testemployees.TestEmployees) ... ok

    ----------------------------------------------------------------------
    Ran 11 tests in 0.090s

    OK

See also :ref:`coverage`.

.. EOF
