import flask
from parking_api.parking.utils.ressources.meta_data import parkings_labels

index_bp = flask.Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def index():
    return flask.render_template('index.html', parkings_labels=parkings_labels)
