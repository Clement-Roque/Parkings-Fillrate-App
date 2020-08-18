from typing import Dict, Union
import pytest
from parking_api.parking.logic import downloader
from parking_api.parking.logic import validator
from ..ressources import url


def test_download_as_text() -> None:

    with pytest.raises(Exception):
        assert downloader.download_as_text("www.false.Ressources.com")

    text: str = downloader.download_as_text(
        url.PARKING_ANTIGONE_URL)

    assert text is not None
    assert isinstance(text, str)


def test_get_data_from_xml_parking_ressource() -> None:

    xml_content: Dict[str, Union[str, int, None]] = downloader.get_data_from_xml_parking_ressource(
        url.PARKING_ANTIGONE_URL)

    assert isinstance(xml_content, dict)
    assert len(xml_content) > 0
    assert validator.is_parking_json_valid(xml_content) is True
