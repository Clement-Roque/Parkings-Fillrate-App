from jsonschema import validate

def parking_json_validator(parking_json):

    parking_json_schema = {
        "Name": "string",
        "Label": "string",
        "status": "string",
        "free": "number",
        "total": "number",
        "last_update": "string",
    }

    return validate(instance=parking_json, schema=parking_json_schema)