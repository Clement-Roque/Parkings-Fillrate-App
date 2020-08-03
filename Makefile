setup:
	pip install pipenv
	pipenv install --dev

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

check:	clean
	pipenv run pytest --cov=. --cov-fail-under 95
	pipenv run mypy parking_api/ test/
	pipenv run pylint parking_api/ --disable=C0114,C0115,C0116
	pipenv run pylint test/ --disable=C0114,C0115,C0116,W0621


start_parking_api :
	export FLASK_APP=parking_api && export FLASK_ENV=development && pipenv run flask run

