import requests
import Logic.Parser


def Download(ressource_url:str)->str:

	# try:
	response = requests.get(ressource_url)
	# except Exception as get_exception
		# raise

	return response.text


def DownloadXML(ressource_url:str)->dict:

	return Logic.Parser.ParseParkingXML(Download(ressource_url))