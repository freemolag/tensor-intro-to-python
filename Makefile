install:
	poetry install

test:
	poetry run pytest tensor_intro_to_python tests

lint:
	poetry run flake8 .