import test.ressources.url
import pytest  # type: ignore
import logic.downloader

def test_download():

    assert logic.downloader.download(test.ressources.url.PARKING_ANTIGONE_URL)
    with pytest.raises(Exception):
        assert logic.downloader.download("www.false.Ressources.com")

def test_download_xml():

    xml_dict = logic.downloader.download_xml(
        test.ressources.url.PARKING_ANTIGONE_URL)

    assert xml_dict is not None
    assert isinstance(xml_dict, dict)
