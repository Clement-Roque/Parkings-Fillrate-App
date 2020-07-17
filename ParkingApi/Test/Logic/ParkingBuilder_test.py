import pytest
from Model.Parking import Parking
from Logic.ParkingBuilder import ParkingBuilder
import Test.Ressources.url
import Ressources.MetaData as MetaData


@pytest.fixture
def parkingBuilderTest()->ParkingBuilder:
	return ParkingBuilder()

def test_build(parkingBuilderTest:ParkingBuilder):

	parkingAntigone = parkingBuilderTest.build("Antigone")
	
	assert parkingAntigone
	assert isinstance(parkingAntigone,Parking)

def test_buildAll(parkingBuilderTest:ParkingBuilder):

	parkings = parkingBuilderTest.buildAll()

	assert len(parkings)==len(MetaData.labels_to_filename)

	for parking in parkings:

		assert parking
		assert isinstance(parkingAntigone,Parking)
		assert parking.label in MetaData.labels_to_filename.keys()

		
