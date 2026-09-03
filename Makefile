.PHONY: test

test-unit:
	poetry run python -u -m unittest discover -s tests/unit -v 2>&1 | tee test_output.txt

test-real:
	poetry run python -u -m unittest discover -s tests/real -v 2>&1 | tee test_output.txt


build:
	poetry build

publish:
	poetry publish


config:
	poetry config pypi-token.pypi your-token-here
