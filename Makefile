# Manage project
#
# You can run unittests using ...
# - python testemployees.py
# - unit2 discover -v
# - python -m unittest discover -v

COVER_DIR = target/cover
SRCS=main.py turnover.py testturnover.py turnovers.py testturnovers.py employees.py testemployees.py
.PROXY: all

all: check cover test doc

check:
	# Check with PyChecker
	pychecker --only $(SRCS)
	# Check with Pep8
	pep8 $(SRCS)

cover:
	# Run main module
	python-coverage run --include=main.py,employees.py main.py -v test.yml
	# Run unit tests (append results)
	python-coverage run -a --include=*turnover.py testturnover.py
	# Run unit tests (append results)
	python-coverage run -a --include=*employees.py testemployees.py
	# Annotate file to see what has been tested
	python-coverage annotate employees.py turnover*.py 
	# Generate coverage report
	python-coverage report --include=*.py

run:
	# Run main
	python main.py test.yml

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
