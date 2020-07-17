import pytest
import Logic.Parser
import datetime

from xml.etree.ElementTree import Element


def test_ParseParkingXML():

	with open("./Test/Ressources/FR_MTP_ANTI.xml",'r') as parking_xml_to_read :
		parking_xml_to_parse = parking_xml_to_read.read()

	parking_xml_parsed = Logic.Parser.ParseParkingXML(parking_xml_to_parse)

	assert parking_xml_parsed is not None
	assert isinstance(parking_xml_parsed,dict)

	assert parking_xml_parsed['DateTime'] is not None
	assert parking_xml_parsed['Free'] is not None
	assert parking_xml_parsed['Name'] is not None
	assert parking_xml_parsed['Status'] is not None
	assert parking_xml_parsed['Total'] is not None

	assert len(parking_xml_parsed)==5
	assert parking_xml_parsed['Free'] <= parking_xml_parsed['Total']
	assert parking_xml_parsed['Name'] == 'ANTI'
	assert parking_xml_parsed['Status'] in ['Open','Close'] 
	assert datetime.datetime.strptime(parking_xml_parsed['DateTime'],'%Y-%m-%dT%H:%M:%S')
