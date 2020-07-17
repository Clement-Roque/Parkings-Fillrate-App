from jsonschema import validate

def parkingJsonValidator(parking_json):

	parking_json_schema = {
		"name" :"string",
		"label" : "string",
		"status" : "string",
		"free" : "number",
		"total" : "number",
		"last_update" : "string",
	}

	return validate(instance=parking_json, schema=parking_json_schema)
