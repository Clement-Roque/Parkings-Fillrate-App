import Model.Parking as Parking
import Logic.Downloader

class ParkingBuilder():

	def __init__(self):

		self.url = "http://data.montpellier3m.fr/sites/default/files/ressources/"
		self.ressources_files ={'Antigone': 'FR_MTP_ANTI.xml',}

	def build(self,parkingLabel:str)->Parking:

		parking_attributes = Logic.Downloader.DownloadXML(self.url+self.ressources_files[parkingLabel])

		return parking_attributes

	# def getRessource(parkingLabel:str)->Parking:

