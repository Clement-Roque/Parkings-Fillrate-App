import flask
from .services import parking_services
from .ressources import meta_data

parking_bp = flask.Blueprint('parking', __name__)

def is_parking_label_invalid(parking_label: str) -> bool:

    return parking_label not in meta_data.parking_labels_to_filenames.keys()


@parking_bp.route('/parking/<parking_label>')
def parking_by_label(parking_label: str):

    if is_parking_label_invalid(parking_label):
        flask.abort(404)

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()
    return flask.jsonify(parking_service.get_by_parking_label(parking_label))


@parking_bp.route('/parkings/')
def parkings():

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()

    return flask.jsonify(parking_service.get_all())


@parking_bp.route('/parkings/labels')
def parking_labels():

    parking_service: parking_services.ParkingServices = parking_services.ParkingServices()

    response: flask.Flask.response_class = flask.make_response(flask.jsonify(
        parking_service.get_parking_labels()), {'Access-Control-Allow-Origin': '*'})

    return response
