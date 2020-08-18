import os
from typing import Dict, Optional
from flask import Flask
from .index import index  # type: ignore
from .parking import parking
from .error import error


def _initialize_blueprints(app: Flask) -> None:
    app.register_blueprint(index.index_bp)
    app.register_blueprint(parking.parking_bp)


def _initialize_errors_hanlders(app: Flask) -> None:
    app.register_blueprint(error.error_bp)


def _initialize_url_rules(app: Flask) -> None:
    app.add_url_rule('/', endpoint='index')


def create_app(test_config: Optional[Dict[str, bool]] = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        _initialize_blueprints(app)
        _initialize_errors_hanlders(app)
        _initialize_url_rules(app)

    return app
