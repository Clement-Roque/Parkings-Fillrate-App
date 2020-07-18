from Model.Parking import Parking
import Logic.Downloader
import Ressources.MetaData as MetaData

class ParkingServices():

	def __init__(self):

		self.parking_url = MetaData.parking_url
		self.labels_to_filenames = MetaData.labels_to_filenames

	def get(self,parking_label:str)->Parking:

		parking_filename = self.labels_to_filenames[parking_label]

		parking_data = Logic.Downloader.DownloadXML(self.parking_url+parking_filename)

		return Parking(name=parking_data['Name'], 
				label=parking_label,
				status=parking_data['Status'],
				free=parking_data['Free'],
				total=parking_data['Total'], 
				last_update=parking_data['DateTime'])

	def getAll(self)->list:

		parkings = []
		for parking_label in self.labels_to_filenames.keys():
			parkings.append(self.get(parking_label))

		return parkings