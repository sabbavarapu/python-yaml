# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help

.PHONY: check clean cover dist doc help run test

COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)

COVER	:= target/cover
SRCS	:=main.py employees/employees.py test/testemployees.py

all: check test cover doc run dist version

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
	# check with pyflakes
	pyflakes $(SRCS)
	# check with pycodestyle
	pycodestyle --verbose $(SRCS)
	# check distutils
	python3 setup.py check

cover:
	nosetests --with-coverage --cover-erase --cover-html-dir=results --cover-html --where $(PWD) --config=test/nosetests.cfg --cover-package employees test/test*.py

run:
	python3 -m main -v test/test.yaml

test:
	nosetests --with-html-output --html-out-file=results.html --where $(PWD) --config=test/nosetests.cfg employees test/test*.py

doc:
	# creating coverage html report to be included in final documentation
	$(RM) -rf $(COVER)
	coverage html -d $(COVER)
	# create sphinx documentation
	(cd docs; make html)

dist:
	# copy readme for use in distribution
	pandoc -t plain README.md > README
	# create source package and build distribution
	python setup.py clean
	python setup.py sdist --dist-dir=target/dist
	python setup.py build --build-base=target/build

clean:
	# cleaning workspace
	coverage erase
	# clean build distribution
	python setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf __pycache__
	$(RM) -f results.html
	$(RM) -rf results/
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v .noseids
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v README

version:
	@grep -F '__version__' employees/employees.py

