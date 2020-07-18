import xml.etree.ElementTree as ElementTree
import Ressources.MetaData as MetaData
import datetime


def ParseParkingXML(xml_string:str)->dict:

	parking_data_tree = ElementTree.fromstring(xml_string)

	parking_data = {field : parking_data_tree.find(field).text for field in MetaData.parking_fields}
	
	try:
		parking_data['DateTime'] = datetime.datetime.strptime(parking_data['DateTime'],'%Y-%m-%dT%H:%M:%S')
	except ValueError as value_error:
		parking_data['DateTime'] = datetime.datetime.strptime(parking_data['DateTime'],'%Y-%m-%dT%H:%M:%S.%f')

	parking_data['Free'] = int(parking_data['Free'])
	parking_data['Name'] = str(parking_data['Name'] )
	parking_data['Status'] = str(parking_data['Status'])
	parking_data['Total'] = int(parking_data['Total'])

	return parking_data
