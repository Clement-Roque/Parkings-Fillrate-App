# Parking's Fillrate App
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Clement-Roque/Parking/Tests)

<img src="https://user-images.githubusercontent.com/15324903/94539609-beadeb00-0245-11eb-80d4-9efe8a661e1b.png" height="400">

This application use OpenData from the south french city Montpellier in order to provide a fillrate for the various parking in the city.
It's build using Python 3.8 and the Flask framework.

http://data.montpellier3m.fr/

https://docs.python.org/fr/3.8/index.html

https://flask.palletsprojects.com/en/1.1.x/

I'm developping this project using XP, TDD and clean code principles.




# Launch

Thanks to the Makefile, you can easily launch this project from an unix system.
It required at least Python 3.8 and pip for being installed :
	
	make setup

Then you can launch the app using the following command, but be carreful, it's not production ready :

	make start_parking_api

And you can run the checks (pytest, pylint and mypy) using this command :

	make checks

