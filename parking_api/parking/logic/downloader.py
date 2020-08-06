from typing import Dict, Optional
import xml.etree.ElementTree as ElementTree
import requests
from ..ressources import meta_data

def download_as_text(ressource_url: str) -> str:

    response: requests.Response = requests.get(ressource_url)

    return response.text

def get_data_from_xml_parking_ressource(ressource_url: str) -> Dict[str, Optional[str]]:

    xml: ElementTree.Element = ElementTree.XML(download_as_text(ressource_url))

    return {field: xml.findtext(field) for field in meta_data.parking_fields}
