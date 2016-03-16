.. _unittest:

Unit Tests
==========

Here are the `unit tests results <_static/results.html>`_ for this project.

This is using the default Python :doc:`../references` suite, but using
:any:nosetests to produce nice HTML output. A list of unit test
assert methods is `here
<https://docs.python.org/2/library/unittest.html#classes-and-functions>`_

To run the unit tests using :download:`testemployees <../tests/testemployees.py>` :

	>>> python-coverage run --include=main.py,employees.employees.py -a -m tests.testemployees

Or::

	>>> python -m unittest discover tests/ -v

Or::

	>>> nosetests --config=tests/nosetests.cfg --verbose --where $PWD tests/test*.py

The basic report of unit test results is:

.. code::

   TestEmployees 0.3.0
   testBadById (__main__.TestEmployees) ... ok
   testBadByName (__main__.TestEmployees) ... ok
   testBadByYear (__main__.TestEmployees) ... ok
   testBadForNameByYear (__main__.TestEmployees) ... ok
   testBadId (__main__.TestEmployees) ... ok
   testBadListById (__main__.TestEmployees) ... ok
   testBadListByName (__main__.TestEmployees) ... ok
   testBadListByYear (__main__.TestEmployees) ... ok
   testByName (__main__.TestEmployees) ... ok
   testByYear (__main__.TestEmployees) ... ok
   testDump (__main__.TestEmployees) ... ok
   testForNameByYear (__main__.TestEmployees) ... ok
   testListById (__main__.TestEmployees) ... ok
   testListByName (__main__.TestEmployees) ... ok
   testListByYear (__main__.TestEmployees) ... ok
   testLoadByFile (__main__.TestEmployees) ... ok
   testLoadByName (__main__.TestEmployees) ... ok
   testName (__main__.TestEmployees) ... ok

   ----------------------------------------------------------------------
   Ran 18 tests in 0.121s

   OK


.. EOF
