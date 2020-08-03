from parking_api.parking.utils.logic import validator

def test_is_parking_json_valid():

    valid_parking_json = {
        "Name": "ANTI",
        "Status": "Open",
        "Free": "123",
        "Total": "34",
        "DateTime": "2020-07-10T16:08:53"
    }

    invalid_parking_json = {
        "Name": 123,
        "Label": 34,
        "Status": 23,
        "Free": "number",
        "Total": 200,
        "last_update": 34
    }

    assert validator.is_parking_json_valid(valid_parking_json) is True
    assert validator.is_parking_json_valid(invalid_parking_json) is False
