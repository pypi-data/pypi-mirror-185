build:
	python3 -m build
deploy:
	python3 -m twine upload dist/*
install:
	pip install -e .
fmt:
	python -m black .
types:
	mypy src
test: # run this with SPINPY_TEST_PUBLIC, SPINPY_TEST_PRIVATE, SPINPY_TEST_CITIZEN environment variables set; also put a bigger than 10Mb file at tests/test.mp4
	python tests/smoke_test.py
	python tests/smoke_test2.py
	python tests/smoke_test3.py
	python tests/smoke_test4.py
freeze:
	pip freeze > requirements.txt

.PHONY: setupenv
setupenv:
	python3 -m venv env
	. env/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt && \
	make install
