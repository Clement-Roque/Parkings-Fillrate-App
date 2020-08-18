import flask
import werkzeug
from .services import parking_services
from .ressources import meta_data

parking_bp = flask.Blueprint('parking', __name__)

def is_parking_label_invalid(parking_label: str) -> bool:

    return parking_label not in meta_data.parking_labels_to_filenames.keys()


@parking_bp.route('/parking/<parking_label>')
def parking_by_label(parking_label: str) -> flask.Response:

    if is_parking_label_invalid(parking_label):
        raise werkzeug.exceptions.NotFound

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()

    response: flask.Response = flask.make_response(flask.jsonify(
        parking_service.get_parking_data_by_label(parking_label)))

    return response


@parking_bp.route('/parkings')
def parking_labels() -> flask.Response:

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()

    response: flask.Response = flask.make_response(flask.jsonify(
        parking_service.get_parking_labels()), {'Access-Control-Allow-Origin': '*'})

    return response
