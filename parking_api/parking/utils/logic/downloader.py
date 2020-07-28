import requests

def download_as_text(ressource_url: str) -> str:

    response = requests.get(ressource_url)

    return response.text
