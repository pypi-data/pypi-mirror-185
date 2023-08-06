.phony: all clean upload

all:
	python -m build

clean:
	rm -rf src/*.egg-info
	rm -rf dist/
	rm -rf build/

upload: all
	python -m twine upload dist/*
