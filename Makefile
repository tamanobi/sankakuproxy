PYTHON_DIR = prox
CONFIG_PATH = $(PYTHON_DIR)/pyproject.toml

.PHONY: format lint test
format:
	isort $(PYTHON_DIR)
	black $(PYTHON_DIR)

lint:
	pflake8 --config $(CONFIG_PATH)
	npx pyright --project $(CONFIG_PATH)

test:
	pytest -c $(CONFIG_PATH)
