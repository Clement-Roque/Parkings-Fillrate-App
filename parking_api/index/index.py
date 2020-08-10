import flask
from typing import Dict, Optional
from parking_api.parking.ressources.meta_data import parking_labels
from parking_api.parking.services import parking_services

index_bp = flask.Blueprint(
    'index', __name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def index():

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()

    parking_informations: Dict[Dict[str, Optional[str]]] = {}

    for parking_label in parking_labels:
        parking_informations[parking_label] = parking_service.get_parking_by_label(
            parking_label)

    return flask.render_template('index.jinja2', parking_informations=parking_informations)
