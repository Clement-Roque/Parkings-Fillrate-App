from typing import List, Optional, Dict
from ..ressources import meta_data
from ..logic import downloader

class ParkingServices():

    def __init__(self):

        self.parking_url: str = meta_data.PARKING_URL
        self.parking_labels: List[str] = meta_data.parking_labels
        self.parking_labels_to_filenames: Dict[str,
                                               str] = meta_data.parking_labels_to_filenames

    def get_parking_by_label(self, parking_label: str) -> Dict[str, Optional[str]]:

        parking_filename: str = self.parking_labels_to_filenames[parking_label]
        parking_xml_url: str = self.parking_url + parking_filename

        return downloader.get_data_from_xml_parking_ressource(parking_xml_url)

    def get_parking_labels(self) -> List[str]:

        return self.parking_labels
