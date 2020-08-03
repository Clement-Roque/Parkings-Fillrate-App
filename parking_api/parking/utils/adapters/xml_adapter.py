import xml.etree.ElementTree as ElementTree
from typing import Dict, Optional
from ..ressources import meta_data


class XmlAdapter():

    def __init__(self, xml: str):

        self.xml = ElementTree.XML(xml)

    def get_data(self) -> Dict[str, Optional[str]]:

        return {field: self.xml.findtext(field) for field in meta_data.parking_fields}
