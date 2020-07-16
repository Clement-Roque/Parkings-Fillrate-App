import pytest
import Logic.Downloader
import Test.Ressources.url

import xml.etree.ElementTree as ElementTree


def test_Download():

	assert Logic.Downloader.Download(Test.Ressources.url.parking_antigone_url)
	with pytest.raises(Exception):
		assert Logic.Downloader.Download("www.false.Ressources.com")

def test_DownloadXML():

	xml_dict = Logic.Downloader.DownloadXML(Test.Ressources.url.parking_antigone_url)

	assert xml_dict is not None
	assert isinstance(xml_dict,dict) 
