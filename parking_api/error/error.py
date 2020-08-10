import flask
import werkzeug

error_bp = flask.Blueprint('error', __name__)


@error_bp.app_errorhandler(werkzeug.exceptions.NotFound)
def handle_not_found_error(error):

    flask.current_app.logger.info(error)
    status_code: int = 404
    response = {
        'success': False,
        'error': {
            'type': 'NotFoundException',
            'message': 'Ressource Not Found'
        }
    }

    return flask.jsonify(response), status_code


@error_bp.app_errorhandler(Exception)
def handle_unexpected_error(error):

    flask.current_app.logger.info(error)
    status_code: int = 500
    response = {
        'success': False,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }

    return flask.jsonify(response), status_code
