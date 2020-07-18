import pytest
from Model.Parking import Parking
from Services.ParkingServices import ParkingServices
import Test.Ressources.url
import Ressources.MetaData as MetaData
import datetime

@pytest.fixture
def ParkingServicesTest()->ParkingServices:
	return ParkingServices()

def test_get(ParkingServicesTest:ParkingServices):

	parking_to_test = ParkingServicesTest.get("Antigone")
	
	assert parking_to_test
	assert isinstance(parking_to_test,Parking)
	assert parking_to_test is not None

	assert parking_to_test.last_update is not None
	assert isinstance(parking_to_test.last_update,datetime.datetime)
	assert parking_to_test.free is not None
	assert isinstance(parking_to_test.free,int)
	assert parking_to_test.name is not None
	assert isinstance(parking_to_test.name,str)
	assert parking_to_test.status is not None
	assert isinstance(parking_to_test.status,str)
	assert parking_to_test.total is not None
	assert isinstance(parking_to_test.total,int)

	assert parking_to_test.free <= parking_to_test.free
	assert parking_to_test.status in ['Open','Closed']

def test_getAll(ParkingServicesTest:ParkingServices):

	parkings = ParkingServicesTest.getAll()

	assert len(parkings)==len(MetaData.labels_to_filenames)

	for parking_to_test in parkings:

		assert parking_to_test
		assert isinstance(parking_to_test,Parking)
		assert parking_to_test is not None

		assert parking_to_test.last_update is not None
		assert isinstance(parking_to_test.last_update,datetime.datetime)
		assert parking_to_test.free is not None
		assert isinstance(parking_to_test.free,int)
		assert parking_to_test.name is not None
		assert isinstance(parking_to_test.name,str)
		assert parking_to_test.status is not None
		assert isinstance(parking_to_test.status,str)
		assert parking_to_test.total is not None
		assert isinstance(parking_to_test.total,int)
		assert parking_to_test.label is not None
		assert isinstance(parking_to_test.label,str)

		assert parking_to_test.free <= parking_to_test.free
		assert parking_to_test.status in ['Open','Closed']
		assert parking_to_test.label in MetaData.labels_to_filenames.keys()

		
