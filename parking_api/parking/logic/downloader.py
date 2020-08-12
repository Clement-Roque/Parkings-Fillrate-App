from typing import Optional, cast, Union, Dict
import xml.etree.ElementTree as ElementTree
import requests
from ..ressources import meta_data

def download_as_text(ressource_url: str) -> str:

    response: requests.Response = requests.get(ressource_url)

    return response.text

def get_data_from_xml_parking_ressource(ressource_url: str) -> Dict[str, Optional[Union[str, int]]]:

    xml: ElementTree.Element = ElementTree.XML(download_as_text(ressource_url))

    data_from_xml: Dict[str, Optional[Union[str, int]]] = {
        field: xml.findtext(field) for field in meta_data.parking_fields}

    data_from_xml["Total"] = int(cast(int, data_from_xml["Total"]))
    data_from_xml["Free"] = int(cast(int, data_from_xml["Free"]))

    return data_from_xml
