import flask
from parking_api.parking.utils.ressources.meta_data import parkings_label_to_filenames

index_bp = flask.Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def index():
    return flask.render_template('index.html', parking_labels=parkings_label_to_filenames.keys())
