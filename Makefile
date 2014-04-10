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
	$(RM) -f .noseids
	$(RM) -f *.pyc *.pyo
	$(RM) -f results.html
	$(RM) -rf target
	python-coverage erase
	(cd doc; make clean)

force_doc:
	true

#EOF
