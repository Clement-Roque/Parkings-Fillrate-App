from typing import Dict, Union
from parking_api.parking.logic import validator

def test_is_parking_json_valid() -> None:

    valid_parking_json: Dict[str, Union[str, int, None]] = {
        "Name": "ANTI",
        "Status": "Open",
        "Free": 23,
        "Total": 34,
        "DateTime": "2020-07-10T16:08:53"
    }

    invalid_parking_json: Dict[str, Union[str, int, None]] = {
        "Name": 123,
        "Label": 34,
        "Status": 23,
        "Free": "number",
        "Total": 200,
        "last_update": 34
    }

    assert validator.is_parking_json_valid(valid_parking_json) is True
    assert validator.is_parking_json_valid(invalid_parking_json) is False
