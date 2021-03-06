setup:
	pip install pipenv
	pipenv install --dev


clean-mypy:
	find . -name '.mypy_cache' -exec rm -fr {} +

clean-test:
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -fr {} +
	find . -name '.coverage.*' -exec rm -fr {} +


clean: clean-test clean-mypy

checks:	clean
	pipenv run pytest --cov=. --cov-fail-under 95
	pipenv run mypy --strict --allow-untyped-decorators parking_api/
	pipenv run mypy --strict --allow-untyped-decorators  test/
	pipenv run pylint parking_api/ --disable=C0114,C0115,C0116
	pipenv run pylint test/ --disable=C0114,C0115,C0116,C0301,W0621,E1136


start_parking_api :
	export FLASK_APP=parking_api && export FLASK_ENV=development && pipenv run flask run

