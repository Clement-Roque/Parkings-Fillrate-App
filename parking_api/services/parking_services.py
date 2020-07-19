from model.parking import Parking
import logic.downloader
import ressources.meta_data as meta_data

class ParkingServices():

    def __init__(self):

        self.parking_url = meta_data.PARKING_URL
        self.labels_to_filenames = meta_data.labels_to_filenames

    def get(self, parking_label: str) -> Parking:

        parking_filename = self.labels_to_filenames[parking_label]

        parking_data = logic.downloader.download_xml(
            self.parking_url + parking_filename)

        return Parking(name=parking_data['Name'],
                       label=parking_label,
                       status=parking_data['Status'],
                       free=parking_data['Free'],
                       total=parking_data['Total'],
                       last_update=parking_data['DateTime'])

    def get_all(self) -> list:

        parkings = []
        for parking_label in self.labels_to_filenames:
            parkings.append(self.get(parking_label))

        return parkings
