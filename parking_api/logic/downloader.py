import requests
from parking_api.logic import parser


def download(ressource_url: str) -> str:

    # try:
    response = requests.get(ressource_url)
    # except Exception as get_exception
    # raise

    return response.text


def download_xml(ressource_url: str) -> dict:

    return parser.parse_parking_xml(download(ressource_url))
