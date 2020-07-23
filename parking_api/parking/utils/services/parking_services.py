from typing import List, Optional
from ..model.parking import Parking
from ..logic import downloader
from ..ressources import meta_data

class ParkingServices():

    def __init__(self):

        self.parking_url = meta_data.PARKING_URL
        self.labels_to_filenames = meta_data.labels_to_filenames

    def get_by_parking_label(self, parking_label: str) -> Parking:

        parking_filename = self.labels_to_filenames[parking_label]

        parking_data = downloader.download_xml(
            self.parking_url + parking_filename)

        return Parking(name=parking_data['Name'],
                       label=parking_label,
                       status=parking_data['Status'],
                       free=parking_data['Free'],
                       total=parking_data['Total'],
                       last_update=parking_data['DateTime'])

    def get_all(self) -> List[Optional[Parking]]:

        parkings: List[Optional[Parking]] = []
        for parking_label in self.labels_to_filenames:
            parkings.append(self.get_by_parking_label(parking_label))

        return parkings
