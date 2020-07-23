from typing import Dict
from jsonschema import validate  # type: ignore

def parking_json_validator(parking_json: Dict[str, str]):

    parking_json_schema = {
        "Name": "string",
        "Label": "string",
        "status": "string",
        "free": "number",
        "total": "number",
        "last_update": "string",
    }

    return validate(instance=parking_json, schema=parking_json_schema)
