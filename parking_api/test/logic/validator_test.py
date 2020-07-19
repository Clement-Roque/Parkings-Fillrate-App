import pytest
import logic.validator

def test_parking_json_validator():

    valid_parking_json = {
        "Name": "ANTI",
        "Label": "Antigone",
        "Status": "Open",
        "Free": 123,
        "Total": 34,
        "Last_update": "2020-07-10T16:08:53"
    }

    invalid_parking_json = {
        "Name": 123,
        "Label": 34,
        "Status": 23,
        "Free": "number",
        "Total": 200,
        "Last_update": 34
    }

    assert logic.validator.parking_json_validator(valid_parking_json) is None
    with pytest.raises(Exception):
        assert logic.validator.parking_json_validator(invalid_parking_json)
