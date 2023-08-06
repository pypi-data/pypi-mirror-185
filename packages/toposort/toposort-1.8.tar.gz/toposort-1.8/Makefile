all: wheel sdist

wheel:
	python3 -m build --wheel

sdist:
	python3 -m build --sdist

clean:
	rm -rf build/ dist/ src/*.egg-info src/__pycache__ test/__pycache__

test:	unittest doctest

unittest:
	PYTHONPATH=src:test python3 -m test.test_toposort

doctest:
	PYTHONPATH=src python3 -m doctest README.txt

upload:
	twine upload dist/*
