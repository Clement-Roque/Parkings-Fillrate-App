import datetime
import logic.parser


def test_parse_parking_xml():

    with open("./test/ressources/FR_MTP_ANTI.xml", 'r') as parking_xml_to_read:
        parking_xml_to_parse = parking_xml_to_read.read()

    parking_xml_parsed = logic.parser.parse_parking_xml(parking_xml_to_parse)

    assert parking_xml_parsed is not None
    assert isinstance(parking_xml_parsed, dict)

    assert parking_xml_parsed['DateTime'] is not None
    assert isinstance(parking_xml_parsed['DateTime'], datetime.datetime)
    assert parking_xml_parsed['Free'] is not None
    assert isinstance(parking_xml_parsed['Free'], int)
    assert parking_xml_parsed['Name'] is not None
    assert isinstance(parking_xml_parsed['Name'], str)
    assert parking_xml_parsed['Status'] is not None
    assert isinstance(parking_xml_parsed['Status'], str)
    assert parking_xml_parsed['Total'] is not None
    assert isinstance(parking_xml_parsed['Total'], int)
    print(type(parking_xml_parsed['Total']))

    assert len(parking_xml_parsed) == 5
    assert parking_xml_parsed['Free'] <= parking_xml_parsed['Total']
    assert parking_xml_parsed['Name'] == 'ANTI'
    assert parking_xml_parsed['Status'] in ['Open', 'Closed']
