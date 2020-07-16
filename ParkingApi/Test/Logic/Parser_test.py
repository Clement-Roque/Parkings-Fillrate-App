import pytest
import Logic.Parser

from xml.etree.ElementTree import Element


def test_ParseXML():

	with open("./Test/Ressources/FR_MTP_ANTI.xml",'r') as xml_to_read :
		xml_to_parse = xml_to_read.read()

	xml_parsed = Logic.Parser.ParseXML(xml_to_parse)

	assert xml_parsed is not None
	assert isinstance(xml_parsed,dict)
