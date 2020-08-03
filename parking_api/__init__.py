import os
from flask import Flask
from .index import index  # type: ignore
from .parking import parking  # type: ignore


def _initialize_blueprints(app):
    app.register_blueprint(index.index_bp)
    app.register_blueprint(parking.parking_bp)


def _initialize_url_rules(app):
    app.add_url_rule('/', endpoint='index')


def create_app(test_config=None):
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
        _initialize_url_rules(app)

    return app
