.PHONY: install test lint fix-lint clean run

install:
	uv sync --all-extras

test:
	uv run Test/Test.py

lint:
	uv run ruff check .
fix-lint:
	uv run ruff check --fix .
	uv run ruff format .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
run:
	uv run Interface/Home.py