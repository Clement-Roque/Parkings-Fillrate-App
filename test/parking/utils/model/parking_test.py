from datetime import datetime
import pytest  # type: ignore
from parking_api.parking.utils.model.parking import Parking
from parking_api.parking.utils.logic import validator


@pytest.fixture
def parking_test() -> Parking:
    return Parking(name="ANTI",
                   label="Antigone", status="Open", free=192,
                   total=280,
                   last_update=datetime.strptime("2020-07-10T16:08:53", '%Y-%m-%dT%H:%M:%S'))


def test_parking_create(parking_test: Parking):

    assert parking_test
    assert isinstance(parking_test, Parking)

def test_parking_id(parking_test: Parking):

    assert isinstance(parking_test.name, str)
    assert parking_test.name == "ANTI"

def test_parking_name(parking_test: Parking):

    assert isinstance(parking_test.label, str)
    assert parking_test.label == "Antigone"

def test_parking_status(parking_test: Parking):

    assert isinstance(parking_test.name, str)
    assert parking_test.status == "Open"

def test_parking_free(parking_test: Parking):

    assert isinstance(parking_test.free, int)
    assert parking_test.free == 192

def test_parking_total(parking_test: Parking):

    assert isinstance(parking_test.total, int)
    assert parking_test.total == 280

def test_parking_last_update(parking_test: Parking):

    assert isinstance(parking_test.last_update, datetime)
    assert parking_test.last_update == datetime.strptime(
        "2020-07-10T16:08:53", '%Y-%m-%dT%H:%M:%S')

def test_to_json(parking_test: Parking):

    assert validator.parking_json_validator(parking_test.to_json()) is None
