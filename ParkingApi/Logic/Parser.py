import xml.etree.ElementTree as ElementTree
import Ressources.MetaData as MetaData


def ParseParkingXML(xml_string:str)->dict:

	xml_content = {}

	parking_information = ElementTree.fromstring(xml_string)

	return {field : parking_information.find(field).text for field in MetaData.parking_fields}
