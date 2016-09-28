.. _unittest:

Unit Tests
==========

Here are the unit tests :download:`results <../results.html>` for this project.

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

.. EOF
