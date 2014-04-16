.. _unittest:

Unit Tests
==========

Here are the `unit tests results <_static/results.html>`_ for this project.

This is using the default Python :ref:`unittest <references>` suite, but using
:ref:`nosetests <references>` to produce nice HTML output. A list of unit test
assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using :download:`testemployees <../tests/testemployees.py>`::

	python-coverage run -a --source=employees --include=main.py,employees.py -m tests.testemployees

Or::

    python -m unittest discover tests/ -v

Or::

    nosetests --config=tests/nosetests.cfg --verbose --where $PWD tests/test*.py
    

The basic report of unit test results is::

    TestEmployees 0.1.0
    testBadById (testemployees.TestEmployees) ... ok
    testBadByName (testemployees.TestEmployees) ... ok
    testBadByYear (testemployees.TestEmployees) ... ok
    testBadForNameByYear (testemployees.TestEmployees) ... ok
    testBadId (testemployees.TestEmployees) ... ok
    testBadListById (testemployees.TestEmployees) ... ok
    testBadListByName (testemployees.TestEmployees) ... ok
    testBadListByYear (testemployees.TestEmployees) ... ok
    testByName (testemployees.TestEmployees) ... ok
    testByYear (testemployees.TestEmployees) ... ok
    testDump (testemployees.TestEmployees) ... ok
    testForNameByYear (testemployees.TestEmployees) ... ok
    testListById (testemployees.TestEmployees) ... ok
    testListByName (testemployees.TestEmployees) ... ok
    testListByYear (testemployees.TestEmployees) ... ok
    testLoadByFile (testemployees.TestEmployees) ... ok
    testLoadByName (testemployees.TestEmployees) ... ok
    testName (testemployees.TestEmployees) ... ok

    ----------------------------------------------------------------------
    Ran 18 tests in 0.084s

    OK

See also :ref:`coverage`.

.. EOF
