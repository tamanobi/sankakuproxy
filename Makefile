.PHONY: format lint
format:
	isort .
	black .

lint:
	npx pyright .
