import requests
import Logic.Parser


def Download(url:str)->str:

	# try:
	response = requests.get(url)
	# except Exception as get_exception
		# raise

	return response.text


def DownloadXML(url:str)->dict:

	return Logic.Parser.ParseParkingXML(Download(url))