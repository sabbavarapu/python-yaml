# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

COMMA:= ,
EMPTY:=
SPACE:= $(EMPTY) $(EMPTY)

COVER_DIR = target/cover
# srcs used by pychecker
SRCS=employees/main.py employees/employees.py test/testemployees.py
SRCS_LIST=$(subst $(SPACE),$(COMMA),$(SRCS))

.PROXY: all

all: check cover run test doc dist

check:
	# Check with PyChecker
	pychecker --only $(SRCS)
	# Check with Pep8
	pep8 --verbose $(SRCS)
	# Check distutils
	python setup.py check

cover:
	# Run main module
	python-coverage run --source=employees --include=main.py,employees.py -m employees.main
	python-coverage run -a --source=employees --include=main.py,employees.py -m employees.main -v data/test.yml
	# Run unit tests (append results)
	python-coverage run -a --source=employees --include=main.py,employees.py -m test.testemployees
	# Annotate file to see what has been tested
	python-coverage annotate employees/employees.py employees/main.py
	# Generate unit test coverage report
	python-coverage report

run:
	# Run main
	python -m employees.main -v data/test.yml

test: force_make
	# Run unit tests
	# python -m unittest discover -v
	# list nodetests plugins using nosetests --plugins -vv
	# make directory for HTML test results
	mkdir -p target/test
	# search test directory
	nosetests --config=test/nosetests.cfg --verbose --where $(PWD) test/test*.py
	# compare with
	# python -m test.testemployees -v

doc: force_make
	# Creating coverage HTML report
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# Create Sphinx documentation
	(cd docs; make html)

dist: force_make
	# Create source package and build distribution
	python setup.py clean
	python setup.py sdist --dist-dir=target/dist 
	python setup.py build --build-base=target/build

clean:
	# Cleaning workspace
	python-coverage erase
	$(RM) -f *,cover
	$(RM) -f MANIFEST
	$(RM) -f .noseids
	$(RM) -f *.pyc *.pyo
	$(RM) -rf employees/*.pyc test/*.pyo
	$(RM) -rf test/*.pyc test/*.pyo

cleanall: clean
	# remove dist and target (doc) too
	python setup.py clean
	$(RM) -rf target
	(cd docs; make clean)

force_make:
	true

#EOF
