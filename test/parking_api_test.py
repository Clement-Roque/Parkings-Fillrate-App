import os
import tempfile

import pytest  # type: ignore

from parking_api import create_app
from flask import Flask


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app: Flask):
    """A test client for the app."""
    return app.test_client()


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_home(client):
    response = client.get("/")

    assert response.data == b"Hello, World!"


def test_parking_by_label(client):
    response = client.get("/parking/Antigone")

    parking_json = response.get_json()

    assert parking_json
    assert parking_json is not None

    assert parking_json["DateTime"] is not None
    assert parking_json["Free"] is not None
    assert parking_json["Name"] is not None
    assert parking_json["Status"] is not None
    assert parking_json["Total"] is not None
    # assert parking_json["Label"] is not None

    assert int(parking_json["Free"]) <= int(parking_json["Total"])
    assert parking_json["Status"] in ['Open', 'Closed']
    # assert parking_json["Label"] == "Antigone"


def test_parking_by_label_not_found(client):
    response = client.get("/parking/Antine")
    assert response.status == '404 NOT FOUND'
