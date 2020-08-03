from typing import Dict
import jsonschema   # type: ignore
from ..ressources import meta_data

def is_parking_json_valid(parking_json: Dict[str, str]) -> bool:

    try:
        jsonschema.validate(instance=parking_json,
                            schema=meta_data.parking_json_schema)
    except (jsonschema.exceptions.ValidationError, jsonschema.exceptions.SchemaError):
        return False
    return True
