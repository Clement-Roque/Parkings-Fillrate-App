from parking_api.parking.utils.adapters.xml_adapter import XmlAdapter
import xml.etree.ElementTree as ElementTree

import pytest  # type: ignore


@pytest.fixture
def xml_for_test() -> str:
    with open("test/parking/utils/ressources/FR_MTP_ANTI.xml", 'r') as parking_xml_to_read:
        parking_xml = parking_xml_to_read.read()
    return parking_xml


def test_xml_adapter(xml_for_test: str):
    xml_adapter = XmlAdapter(xml_for_test)
    assert xml_adapter
    assert isinstance(xml_adapter.xml, ElementTree.Element)

def test_get_data(xml_for_test: str):

    xml_adapter = XmlAdapter(xml_for_test)
    xml_content = xml_adapter.get_data()

    assert isinstance(xml_content, dict)
    assert len(xml_content) > 0
