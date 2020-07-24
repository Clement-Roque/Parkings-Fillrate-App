import flask
from .utils.services.parking_services import ParkingServices
from .utils.ressources import meta_data

parking = flask.Blueprint('parking', __name__)


@parking.route('/parking/<parking_label>')
def parking_by_label(parking_label: str):

    if (parking_label in meta_data.labels_to_filenames.keys()):
        parking_service = ParkingServices()

        return flask.jsonify(parking_service.get_by_parking_label(parking_label).to_json())
