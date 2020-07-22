setup:
	pip install pipenv
	pipenv install --dev

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

check:	clean
	pipenv run pytest parking_api --cov=parking_api --cov-fail-under 95
	pipenv run mypy parking_api

start_parking_api :
	export FLASK_APP=parking_app && pipenv run flask run

