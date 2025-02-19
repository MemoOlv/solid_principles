all: check tests

.PHONY: \
		all \
		clean \
		check \
		format \
		tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive src/__pycache__
	rm --force --recursive tests/__pycache__

check:
	black --check --line-length 100 src
	black --check --line-length 100 tests
	mypy src/*.py

format:
	black --line-length 100 src
	black --line-length 100 tests

tests:
	pytest --verbose