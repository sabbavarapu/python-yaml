.. _build:

How to build the project using make
===================================

Build everything, including documentation, by running::

   make clean all doc

The Makefile used is::

    # Manage project
    #
    # You can run unittests using ...
    # - python testemployees.py
    # - python -m unittest discover -v

    COMMA:= ,
    EMPTY:=
    SPACE:= $(EMPTY) $(EMPTY)

    COVER_DIR = target/cover
    # srcs used by pychecker
    SRCS=main.py employees.py testemployees.py
    SRCS_LIST=$(subst $(SPACE),$(COMMA),$(SRCS))

    .PROXY: all

    all: check cover test

    check:
        # Check with PyChecker
        pychecker --only $(SRCS)
        # Check with Pep8
        pep8 --verbose $(SRCS)

    cover:
        # Run main module
        python-coverage run --include=main.py,employees.py main.py
        python-coverage run -a --include=main.py,employees.py main.py -v test.yml
        # Run unit tests (append results)
        python-coverage run -a --include=employees.py testemployees.py
        # Annotate file to see what has been tested
        python-coverage annotate employees.py main.py
        # Generate unit test coverage report
        python-coverage report --include=${SRCS_LIST}

    run:
        # Run main
        python main.py -v test.yml

    test:
        # Run unit tests
        # python -m unittest discover -v
        nosetests testemployees.py -v
        mkdir -p target/tests
        mv results.html target/tests

    doc: force_doc
        # Creating coverage HTML report
        $(RM) -rf $(COVER_DIR)
        python-coverage html -d $(COVER_DIR)
        # Create Sphinx documentation
        (cd doc; make html)

    clean:
        # Cleaning workspace
        $(RM) -f *,cover
        $(RM) -f *.pyc *.pyo
        $(RM) -f results.html
        $(RM) -rf target
        python-coverage erase
        (cd doc; make clean)

    force_doc:
        true

    #EOF

This will produce a copious quantity of output::

    # Cleaning workspace
    rm -f -f *,cover
    rm -f -f *.pyc *.pyo
    rm -f -f results.html
    rm -f -rf target
    python-coverage erase
    (cd doc; make clean)
    /home/frank/dev/python/yaml/doc
    make[1]: Entering directory `/home/frank/dev/python/yaml/doc'
    rm -rf ../target/doc/*
    make[1]: Leaving directory `/home/frank/dev/python/yaml/doc'
    # Check with PyChecker
    pychecker --only main.py employees.py testemployees.py
    Processing module main (main.py)...
    Processing module employees (employees.py)...
    Processing module testemployees (testemployees.py)...

    Warnings...

    None
    # Check with Pep8
    pep8 --verbose main.py employees.py testemployees.py
    local configuration: in /home/frank/dev/python/yaml
    checking main.py
    checking employees.py
    checking testemployees.py
    # Run main module
    python-coverage run --include=main.py,employees.py main.py
    python-coverage run -a --include=main.py,employees.py main.py -v test.yml
    2014-04-11 00:02:49,213 infile ......................: test.yml
    2014-04-11 00:02:49,213 prog ........................: main.py
    2014-04-11 00:02:49,213 verbose .....................: 1
    2014-04-11 00:02:49,213 name for id 3 ...............: frank
    2014-04-11 00:02:49,213 turnover for frank ..........: $440,000
    2014-04-11 00:02:49,213 turnover for frank in 2012 ..: $140,000
    2014-04-11 00:02:49,213 turnover for all in 2012 ....: $270,000
    2014-04-11 00:02:49,213 list frank years ............: [2011, 2012, 2013]
    2014-04-11 00:02:49,213 list turnover for 2013 ......: [200000, 220000]
    # Run unit tests (append results)
    python-coverage run -a --include=employees.py testemployees.py
    ................
    ----------------------------------------------------------------------
    Ran 16 tests in 0.094s

    OK
    # Annotate file to see what has been tested
    python-coverage annotate employees.py main.py
    # Generate unit test coverage report
    python-coverage report --include=main.py,employees.py,testemployees.py
    Name        Stmts   Miss  Cover
    -------------------------------
    employees      54      0   100%
    main           39      0   100%
    -------------------------------
    TOTAL          93      0   100%
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
    Ran 16 tests in 0.050s

    OK
    mkdir -p target/tests
    mv results.html target/tests
    true
    # Creating coverage HTML report
    rm -f -rf target/cover
    python-coverage html -d target/cover
    # Create Sphinx documentation
    (cd doc; make html)
    /home/frank/dev/python/yaml/doc
    make[1]: Entering directory `/home/frank/dev/python/yaml/doc'
    sphinx-build -b html -a -q -d ../target/doc/doctrees  . ../target/doc/html
    Making output directory...

    Build finished. The HTML pages are in ../target/doc/html.
    make[1]: Leaving directory `/home/frank/dev/python/yaml/doc'

.. EOF
