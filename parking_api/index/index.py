import flask
from parking_api.parking.ressources.meta_data import parking_labels

index_bp = flask.Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def index():
    return flask.render_template('index.html', parking_labels=parking_labels)
