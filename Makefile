.PHONY: test

test:
	poetry run python -m unittest discover -v


build:
	poetry build

publish:
	poetry publish


config:
	poetry config pypi-token.pypi your-token-here
