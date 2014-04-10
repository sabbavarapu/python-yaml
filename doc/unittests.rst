.. _unittest:

Unit Tests
==========

Here are the `unit tests results <_static/results.html>`_ for this project.

This is using the default Python :ref:`unittest <references>` suite, but using
:ref:`nosetests <references>` to produce nice HTML output. A list of unit test
assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using::

    python-coverage run -a --include=testemployees.py,employees.py testemployees.py

Or::

    python -m unittest discover -v

Or::

	nosetests testemployees.py

The basic report of unit test results is::

    # Run unit tests
    # python -m unittest discover -v
    nosetests testemployees.py -v
    testAllByYear (testemployees.TestEmployees) ... ok
    testBadAllByYear (testemployees.TestEmployees) ... ok
    testBadByName (testemployees.TestEmployees) ... ok
    testBadId (testemployees.TestEmployees) ... ok
    testBadListByName (testemployees.TestEmployees) ... ok
    testBadListByYear (testemployees.TestEmployees) ... ok
    testBadNameByYear (testemployees.TestEmployees) ... ok
    testBadYearByYear (testemployees.TestEmployees) ... ok
    testByName (testemployees.TestEmployees) ... ok
    testByYear (testemployees.TestEmployees) ... ok
    testDump (testemployees.TestEmployees) ... ok
    testListByName (testemployees.TestEmployees) ... ok
    testListByYear (testemployees.TestEmployees) ... ok
    testLoadByFile (testemployees.TestEmployees) ... ok
    testLoadByName (testemployees.TestEmployees) ... ok
    testName (testemployees.TestEmployees) ... ok

    ----------------------------------------------------------------------
    Ran 16 tests in 0.052s

    OK

See also :ref:`coverage`.

.. EOF
