# Manage project
#
# You can run unittests using ...
# - python testemployees.py
# - unit2 discover -v
# - python -m unittest discover -v

COMMA:= ,
EMPTY:=
SPACE:= $(EMPTY) $(EMPTY)

COVER_DIR = target/cover
SRCS=main.py turnovers.py testturnovers.py employees.py testemployees.py
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
	python-coverage run --include=main.py,employees.py main.py -v test.yml
	# Run unit tests (append results)
	python-coverage run -a --include=turnovers.py testturnovers.py
	# Run unit tests (append results)
	python-coverage run -a --include=employees.py testemployees.py
	# Annotate file to see what has been tested
	python-coverage annotate turnovers.py employees.py
	# Generate coverage report
	python-coverage report --include=$(SRCS_LIST)

run:
	# Run main
	python main.py -v test.yml

test:
	# Run unit tests
	python -m unittest discover -v

doc: force_doc
	# Creating coverage HTML report
	$(RM) -rf $(COVER_DIR)
	python-coverage html -d $(COVER_DIR)
	# Create Sphinx documentation
	(cd doc; make html)

clean:
	# Cleaning workspace
	$(RM) -f *,cover
	$(RM) -f *.pyc
	$(RM) -rf target
	python-coverage erase
	(cd doc; make clean)

force_doc:
	true

#EOF
