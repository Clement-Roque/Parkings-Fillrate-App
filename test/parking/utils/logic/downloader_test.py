from ..ressources import url
import pytest  # type: ignore
from parking_api.parking.utils.logic import downloader

def test_download_as_text():

    with pytest.raises(Exception):
        assert downloader.download_as_text("www.false.Ressources.com")

    text = downloader.download_as_text(
        url.PARKING_ANTIGONE_URL)

    assert text is not None
    assert isinstance(text, str)
