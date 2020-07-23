from ..ressources import url
import pytest  # type: ignore
from parking_api.parking.utils.logic import downloader

def test_download():

    assert downloader.download(url.PARKING_ANTIGONE_URL)
    with pytest.raises(Exception):
        assert downloader.download("www.false.Ressources.com")

def test_download_xml():

    xml_dict = downloader.download_xml(
        url.PARKING_ANTIGONE_URL)

    assert xml_dict is not None
    assert isinstance(xml_dict, dict)
