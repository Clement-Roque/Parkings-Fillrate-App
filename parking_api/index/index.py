import flask

index_bp = flask.Blueprint(
    'index', __name__, template_folder='templates', static_folder='static')


@index_bp.route('/')
def index():

    return flask.render_template('index.jinja2')
