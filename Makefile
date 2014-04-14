# Manage project
#
# You can run unittests using ...
# - python -m tests.testemployees -v
# - python -m unittest discover -v

COMMA:= ,
EMPTY:=
SPACE:= $(EMPTY) $(EMPTY)

COVER_DIR = target/cover
# srcs used by pychecker
SRCS=employees/main.py employees/employees.py tests/testemployees.py
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
	python-coverage run --source=employees --include=main.py,employees.py -m employees.main
	python-coverage run -a --source=employees --include=main.py,employees.py -m employees.main -v tests/test.yml
	# Run unit tests (append results)
	python-coverage run -a --source=employees --include=main.py,employees.py -m tests.testemployees
	# Annotate file to see what has been tested
	python-coverage annotate employees/employees.py employees/main.py
	# Generate unit test coverage report
	python-coverage report employees.*

run:
	# Run main
	python -m employees.main -v tests/test.yml

test:
	# Run unit tests
	# python -m unittest discover -v
	# list nodetests plugins using nosetests --plugins -vv
	# make directory for HTML test results
	mkdir -p target/tests
	# search tests directory
	nosetests --config=tests/nosetests.cfg --verbose --where $(PWD) tests/test*.py
	# compare with
	# python -m tests.testemployees -v

doc: force_make
	# Creating coverage HTML report
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# Create Sphinx documentation
	(cd docs; make html)

dist: force_make
	# Create package for distribution
	python setup.py sdist

clean:
	# Cleaning workspace
	python-coverage erase
	$(RM) -f *,cover
	$(RM) -f MANIFEST
	$(RM) -f .noseids
	$(RM) -f *.pyc *.pyo
	$(RM) -rf dist/*
	$(RM) -rf employees/*.pyc tests/*.pyo
	$(RM) -rf tests/*.pyc tests/*.pyo

cleanall: clean
	$(RM) -rf target
	(cd docs; make clean)

force_make:
	true

#EOF
