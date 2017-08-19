# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help

.PHONY: check run test doc clean help

COMMA:= ,
EMPTY:=
SPACE:= $(EMPTY) $(EMPTY)

COVER_DIR = target/cover
# srcs used by pychecker
SRCS=main.py employees/employees.py test/testemployees.py
SRCS_LIST=$(subst $(SPACE),$(COMMA),$(SRCS))

all: check cover run test doc dist

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: validate code and distribution config"
	@echo "  cover: run test coverage report"
	@echo "  run:   run against test data"
	@echo "  test:  run unit test"
	@echo "  doc:   create documentation including test converage and results"
	@echo "  dist:  create a distrbution archive"
	@echo "  clean: delete all generated files"
	@echo

check:
	# check with PyChecker
	pychecker --only $(SRCS)
	# check with Pep8
	pep8 --verbose $(SRCS)
	# check distutils
	python setup.py check

cover:
	# run main module
	python-coverage run --include=main.py,employees.employees.py -m main
	# run main module with verbose and test data
	python-coverage run --include=main.py,employees.employees.py -a -m main -v test/test.yaml
	# run unit tests (append results)
	python-coverage run --include=main.py,employees.employees.py -a -m test.testemployees
	# annotate file to see what has been tested
	python-coverage annotate employees/employees.py main.py
	# generate unit test coverage report
	python-coverage report

run:
	# run main
	python -m main -v test/test.yaml

test:
	# run unit tests
	# python -m unittest discover -v
	# list nodetests plugins using nosetests --plugins -vv
	# run using nosetests for text and html output
	nosetests --config=test/nosetests.cfg --with-html-output --html-out-file results.html --where $(PWD) --cover-package employees test/test*.py
	# run test class
	#   python -m test.testemployees -v
	# test documentation (run coverage first)
	#   (cd docs; make doctest; make linkcheck)

doc:
	# creating coverage html report to be included in final documentation
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# create sphinx documentation
	(cd docs; make singlehtml)

dist:
	# copy readme for use in distribution
	pandoc -t plain README.md > README
	# create source package and build distribution
	python setup.py clean
	python setup.py sdist --dist-dir=target/dist
	python setup.py build --build-base=target/build

clean:
	# cleaning workspace
	python-coverage erase
	# clean build distribution
	python setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf results.html
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v .noseids
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v README

# EOF
