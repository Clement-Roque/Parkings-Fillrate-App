import pytest
import Logic.Validator

def test_parkingJsonValidator():
	
	valid_parking_json = {
		"name" :"ANTI",
		"label" : "Antigone",
		"status" : "Open",
		"free" : 123,
		"total" : 34,
		"last_update" : "2020-07-10T16:08:53"
	}

	invalid_parking_json = {
		"name" :123,
		"label" : 34,
		"status" : 23,
		"free" : "number",
		"total" : 200,
		"last_update" : 34
	}

	assert Logic.Validator.parkingJsonValidator(valid_parking_json) is None
	with pytest.raises(Exception):
		assert Logic.Validator.parkingJsonValidator(invalid_parking_json)