from typing import cast
import pytest  # type: ignore
from parking_api.parking.services.parking_services import ParkingServices
from parking_api.parking.ressources import meta_data


@pytest.fixture
def parking_services_test() -> ParkingServices:
    return ParkingServices()

def test_get_parking_labels(parking_services_test: ParkingServices):

    parking_labels = parking_services_test.get_parking_labels()

    assert len(parking_labels) == len(meta_data.parking_labels)
    for parking_label in parking_labels:
        assert parking_label in meta_data.parking_labels


def test_get_parking_by_label(parking_services_test: ParkingServices):

    parking_to_test = parking_services_test.get_parking_by_label("Antigone")

    assert parking_to_test
    assert isinstance(parking_to_test, dict)
    assert parking_to_test is not None

    assert int(cast(int, parking_to_test["Free"])) <= int(
        cast(int, parking_to_test["Total"]))
    assert parking_to_test["Status"] in ['Open', 'Closed']
