#
# Manage YAML example project
#
# You can run just the unittests using ...
# python testemployees.py

TEST_DIR = target/test

.PROXY: all

all: check test doc

check:
	pychecker --only main.py employees.py testemployees.py
	pep8 main.py employees.py testemployees.py 

test:
	# Run main module
	python-coverage run --include=main.py,employees.py main.py -v test.yml
	# Run all unit tests (append results)
	python-coverage run -a --include=testemployees.py,employees.py testemployees.py
	# Report unit tests to console
	python-coverage report --include=testemployees.py,employees.py,main.py 
	# Annotate file to see what has been tested
	python-coverage annotate employees.py

doc: force_doc
	# Creating coverage HTML report
	$(RM) -rf $(TEST_DIR)
	python-coverage html -d $(TEST_DIR)
	# Create Sphinx documentation
	cd doc; make html

clean:
	$(RM) -f *,cover
	$(RM) -f *.pyc
	$(RM) -rf target
	python-coverage erase
	cd doc; make clean

force_doc:
	true

#EOF
