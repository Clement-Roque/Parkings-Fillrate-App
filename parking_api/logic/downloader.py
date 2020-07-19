import requests
import logic.parser


def download(ressource_url: str) -> str:

    # try:
    response = requests.get(ressource_url)
    # except Exception as get_exception
    # raise

    return response.text


def download_xml(ressource_url: str) -> dict:

    return logic.parser.parse_parking_xml(download(ressource_url))
