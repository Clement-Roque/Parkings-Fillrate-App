import xml.etree.ElementTree as ElementTree
import Ressources.MetaData as MetaData
import datetime


def ParseParkingXML(xml_string:str)->dict:

	parking_informations_tree = ElementTree.fromstring(xml_string)

	parking_informations = {field : parking_informations_tree.find(field).text for field in MetaData.parking_fields}
	
	try:
		parking_informations['DateTime'] = datetime.datetime.strptime(parking_informations['DateTime'],'%Y-%m-%dT%H:%M:%S')
	except ValueError as value_error:
		parking_informations['DateTime'] = datetime.datetime.strptime(parking_informations['DateTime'],'%Y-%m-%dT%H:%M:%S.%f')

	parking_informations['Free'] = int(parking_informations['Free'])
	parking_informations['Name'] = str(parking_informations['Name'] )
	parking_informations['Status'] = str(parking_informations['Status'])
	parking_informations['Total'] = int(parking_informations['Total'])

	return parking_informations
