import pytest
import datetime
from Model.Parking import Parking


@pytest.fixture
def parkingTest() -> Parking:
	return Parking(name="ANTI", label="Antigone",status="Open",free=192,total=280,last_update="2020-07-10T16:08:53")


def test_Parking_create(parkingTest:Parking):

	assert parkingTest
	assert isinstance(parkingTest,Parking)

def test_Parking_id(parkingTest:Parking):

	assert isinstance(parkingTest.name,str)
	assert parkingTest.name == "ANTI"

def test_Parking_name(parkingTest:Parking):

	assert isinstance(parkingTest.label,str)
	assert parkingTest.label == "Antigone"

def test_Parking_status(parkingTest:Parking):

	assert isinstance(parkingTest.name,str)
	assert parkingTest.status == "Open"

def test_Parking_free(parkingTest:Parking):

	assert isinstance(parkingTest.free,int)
	assert parkingTest.free == 192

def test_Parking_total(parkingTest:Parking):

	assert isinstance(parkingTest.total,int)
	assert parkingTest.total == 280

def test_Parking_last_update(parkingTest:Parking):

	assert isinstance(parkingTest.last_update,datetime.datetime)
	assert parkingTest.last_update == datetime.datetime.strptime("2020-07-10T16:08:53",'%Y-%m-%dT%H:%M:%S')