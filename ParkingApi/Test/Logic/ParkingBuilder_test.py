import pytest
from Model.Parking import Parking
from Logic.ParkingBuilder import ParkingBuilder
import Test.Ressources.url

@pytest.fixture
def parkingBuilderTest()->ParkingBuilder:
	return ParkingBuilder()

def test_build(parkingBuilderTest:ParkingBuilder):

	parkingAntigone = parkingBuilderTest.build("Antigone")
	
	assert parkingAntigone
	assert isinstance(parkingAntigone,Parking)

	
