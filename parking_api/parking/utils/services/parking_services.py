from typing import List, Optional, Dict
from ..ressources import meta_data
from ..logic import downloader

class ParkingServices():

    def __init__(self):

        self.parking_url = meta_data.PARKING_URL
        self.parkings_label = meta_data.parkings_label
        self.parkings_label_to_filenames = meta_data.parkings_label_to_filenames

    def get_by_parking_label(self, parking_label: str) -> Dict[str, Optional[str]]:

        parking_filename = self.parkings_label_to_filenames[parking_label]
        parking_xml_url = self.parking_url + parking_filename

        return downloader.get_data_from_xml_parking_ressource(parking_xml_url)

    def get_all(self) -> List[Dict[str, Optional[str]]]:

        parkings: List[Dict[str, Optional[str]]] = []
        for parking_label in self.parkings_label:
            parkings.append(self.get_by_parking_label(parking_label))

        return parkings

    def get_parkings_label(self) -> List[str]:

        return self.parkings_label
