from typing import List, Optional, Dict
from ..ressources import meta_data
from ..logic import downloader
from ..adapters import xml_adapter

class ParkingServices():

    def __init__(self):

        self.parking_url = meta_data.PARKING_URL
        self.labels_to_filenames = meta_data.labels_to_filenames

    def get_by_parking_label(self, parking_label: str) -> Dict[str, Optional[str]]:

        parking_filename = self.labels_to_filenames[parking_label]
        parking_xml_url = self.parking_url + parking_filename

        parking_xml_adapter = xml_adapter.XmlAdapter(
            downloader.download_as_text(parking_xml_url))
        return parking_xml_adapter.get_data()

    def get_all(self) -> List[Dict[str, Optional[str]]]:

        parkings: List[Dict[str, Optional[str]]] = []
        for parking_label in self.labels_to_filenames:
            parkings.append(self.get_by_parking_label(parking_label))

        return parkings
