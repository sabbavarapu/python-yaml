.. _build:

How to build the project using make
===================================

Build everything, including documentation, by running::

   make clean all doc

This will produce a copious quantity of output::

   # Cleaning workspace
   rm -f -f *,cover
   rm -f -f *.pyc
   rm -f -rf target
   python-coverage erase
   (cd doc; make clean)
   /home/frank/current/dev/python/yaml/doc
   make[1]: Entering directory `/home/frank/clients/telstra/dev/python/yaml/doc'
   rm -rf ../target/doc/*
   make[1]: Leaving directory `/home/frank/clients/telstra/dev/python/yaml/doc'
   # Check with PyChecker
   pychecker --only main.py employees.py testemployees.py

   Warnings...

   None
   # Check with Pep8
   pep8 --verbose main.py employees.py testemployees.py
   checking main.py
   checking employees.py
   checking testemployees.py
   # Run main module
   python-coverage run --include=main.py,employees.py main.py -v test.yml

   Show command line parameters ...
   infile = test.yml
   prog = main.py
   verbose = 1
   data:
   # list of company employees and their turnovers by year

   frank:
      id: 3
      turnover:
         2011: 100000
         2012: 140000
         2013: 200000

   jo:
      id: 4
      turnover:
         2012: 130000
         2013: 220000
         2014: 210000
   ...

   employees.dump:
   frank:
   id: 3
   turnover: {2011: 100000, 2012: 140000, 2013: 200000}
   jo:
   id: 4
   turnover: {2012: 130000, 2013: 220000, 2014: 210000}

   Turnover for employee name 'frank' ....: $440,000
   Employee name for id 3 ................: frank
   Employee name for id 4 ................: jo
   Turnover for employee 'frank' in 2012 .: $140,000
   Turnover for all in 2012 ..............: $270,000
   # Run unit tests (append results)
   python-coverage run -a --include=employees.py testemployees.py
   # Annotate file to see what has been tested
   python-coverage annotate employees.py
   # Generate unit test coverage report
   python-coverage report --include=main.py,employees.py,testemployees.py
   Name        Stmts   Miss  Cover
   -------------------------------
   employees      40      0   100%
   main           36      0   100%
   -------------------------------
   TOTAL          76      0   100%
   # Run unit tests
   python -m unittest discover -v
   true
   # Creating coverage HTML report
   rm -f -rf target/cover
   python-coverage html -d target/cover
   # Create Sphinx documentation
   (cd doc; make html)
   /home/frank/current/dev/python/yaml/doc
   make[1]: Entering directory `/home/frank/clients/telstra/dev/python/yaml/doc'
   sphinx-build -b html -d ../target/doc/doctrees   . ../target/doc/html
   Running Sphinx v1.1.3
   loading pickled environment... not yet created
   building [html]: targets for 10 source files that are out of date
   updating environment: 10 added, 0 changed, 0 removed
   reading sources... [ 10%] build
   reading sources... [ 20%] classes
   reading sources... [ 30%] coverage
   reading sources... [ 40%] dependencies
   reading sources... [ 50%] employees
   reading sources... [ 60%] index
   reading sources... [ 70%] main
   reading sources... [ 80%] references
   reading sources... [ 90%] testemployees
   reading sources... [100%] unittests

   looking for now-outdated files... none found
   pickling environment... done
   checking consistency... done
   preparing documents... done
   writing output... [ 10%] build
   writing output... [ 20%] classes
   writing output... [ 30%] coverage
   writing output... [ 40%] dependencies
   writing output... [ 50%] employees
   writing output... [ 60%] index
   writing output... [ 70%] main
   writing output... [ 80%] references
   writing output... [ 90%] testemployees
   writing output... [100%] unittests

   writing additional files... genindex py-modindex search
   copying downloadable files... [100%] /home/frank/clients/telstra/dev/python/yaml/doc/../main.py

   copying static files... done
   dumping search index... done
   dumping object inventory... done
   build succeeded.

   Build finished. The HTML pages are in ../target/doc/html.
   make[1]: Leaving directory `/home/frank/clients/telstra/dev/python/yaml/doc'

.. EOF
