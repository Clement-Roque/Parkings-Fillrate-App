from typing import Dict
from ..ressources import meta_data
import jsonschema   # type: ignore

def is_valid_parking_json(parking_json: Dict[str, str]) -> bool:

    try:
        jsonschema.validate(instance=parking_json,
                            schema=meta_data.parking_json_schema)
    except (jsonschema.exceptions.ValidationError, jsonschema.exceptions.SchemaError):
        return False
    return True
