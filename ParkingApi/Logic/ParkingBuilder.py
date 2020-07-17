from Model.Parking import Parking
import Logic.Downloader
import Ressources.MetaData as MetaData

class ParkingBuilder():

	def __init__(self):

		self.url = MetaData.parking_url
		self.labels_to_filename = MetaData.labels_to_filename

	def build(self,parking_label:str)->Parking:

		parking_filename = self.labels_to_filename[parking_label]

		parking_attributes = Logic.Downloader.DownloadXML(self.url+parking_filename)

		return Parking(name=parking_attributes['Name'], 
				label=parking_label,
				status=parking_attributes['Status'],
				free=int(parking_attributes['Free']),
				total=int(parking_attributes['Total']), 
				last_update=parking_attributes['DateTime'])

	def buildAll(self)->list:

		parkings = []
		for parking_label, parking_filename in self.labels_to_filename.items():
			print(parking_label)
			parkings.append(self.build(parking_label))

		return parkings