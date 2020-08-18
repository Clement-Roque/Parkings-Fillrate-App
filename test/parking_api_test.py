from __future__ import annotations
from typing import Generator
import pytest

from flask import Flask, testing, Response
from parking_api import create_app


@pytest.fixture
def app() -> Generator[Flask, None, None]:

    app = create_app({"TESTING": True})

    yield app


@pytest.fixture
def client(app: Flask) -> testing.FlaskClient[Response]:

    return app.test_client()


def test_config() -> None:

    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_home(client: testing.FlaskClient[Response]) -> None:
    response = client.get("/")

    assert response.status == '200 OK'


def test_parking_by_label(client: testing.FlaskClient[Response]) -> None:
    response = client.get("/parking/Antigone")

    parking_json = response.get_json()

    assert parking_json
    assert parking_json is not None

    assert parking_json["DateTime"] is not None
    assert parking_json["Free"] is not None
    assert parking_json["Name"] is not None
    assert parking_json["Status"] is not None
    assert parking_json["Total"] is not None

    assert int(parking_json["Free"]) <= int(parking_json["Total"])
    assert parking_json["Status"] in ['Open', 'Closed']


def test_parking_by_label_not_found(client: testing.FlaskClient[Response]) -> None:
    response = client.get("/parking/Antine")
    assert response.status_code == 404
    assert response.get_data(
        as_text=True) == '{"error":{"message":"Ressource Not Found","type":"NotFoundException"},"success":false}\n'


def test_parking_labels(client: testing.FlaskClient[Response]) -> None:
    response = client.get("/parkings")

    parking_labels = response.get_json()

    assert len(parking_labels) > 0
    for parking_label in parking_labels:
        assert isinstance(parking_label, str)
        assert len(parking_label) > 0
