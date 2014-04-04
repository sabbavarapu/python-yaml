#
# Manage YAML example project
#
TEST_DIR = target/test

.PROXY: all

all: check test doc

check:
	pychecker --only main.py employees.py testemployees.py
	pep8 main.py employees.py testemployees.py 
	python-coverage run --include=main.py,employees.py main.py -v test.yml
	python-coverage run --include=testemployees.py,employees.py testemployees.py
	python-coverage annotate -d $(TEST_DIR) --include=testemployees.py,employees.py testemployees.py
	python-coverage combine
	python-coverage report --include=testemployees.py,employees.py 
	python-coverage html -d $(TEST_DIR)

test:
	python testemployees.py

doc: force_doc
	cd doc; make html

clean:
	$(RM) -f *.pyc
	$(RM) -rf target
	python-coverage erase
	cd doc; make clean

force_doc:
	true

#EOF
