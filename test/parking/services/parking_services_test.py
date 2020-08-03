from typing import cast
import pytest  # type: ignore
from parking_api.parking.services.parking_services import ParkingServices
from parking_api.parking.ressources import meta_data


@pytest.fixture
def parking_services_test() -> ParkingServices:
    return ParkingServices()

def test_get_parkings_labels(parking_services_test: ParkingServices):

    parkings_labels = parking_services_test.get_parkings_labels()

    assert len(parkings_labels) == len(meta_data.parkings_labels)
    for parking_label in parkings_labels:
        assert parking_label in meta_data.parkings_labels


def test_get_by_parking_label(parking_services_test: ParkingServices):

    parking_to_test = parking_services_test.get_by_parking_label("Antigone")

    assert parking_to_test
    assert isinstance(parking_to_test, dict)
    assert parking_to_test is not None

    assert int(cast(int, parking_to_test["Free"])) <= int(cast(int, parking_to_test["Total"]))
    assert parking_to_test["Status"] in ['Open', 'Closed']

def test_get_all(parking_services_test: ParkingServices):

    parkings = parking_services_test.get_all()

    assert len(parkings) == len(meta_data.parkings_labels_to_filenames)

    for parking_to_test in parkings:

        assert parking_to_test
        assert isinstance(parking_to_test, dict)
        assert parking_to_test is not None

        assert int(cast(int, parking_to_test["Free"])) <= int(cast(int, parking_to_test["Total"]))
        assert parking_to_test["Status"] in ['Open', 'Closed']
