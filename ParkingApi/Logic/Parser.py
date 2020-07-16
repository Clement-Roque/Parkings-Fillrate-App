import xml.etree.ElementTree as ElementTree

def ParseXML(xml_string:str)->dict:

	xml_content = {}

	xml_tree = ElementTree.fromstring(xml_string)

	return {child.tag : child.attrib for child in xml_tree}

