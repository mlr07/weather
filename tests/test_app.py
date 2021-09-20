import pytest
from app import get_weather, crds, key, units, app 
from webtest import TestApp


# run with python -m pytest tests/ from project root
# this will add root to sys.path


def test_get_weather():
    """
    functional test to check response from openweather api.
    """

    data = get_weather(crds, key, units)

    for i in data:
        assert i["cod"] == 200


def test_route_weather():
    """
    functional test to check weather route.
    """

    test_app = TestApp(app)
    resp = test_app.get("/")

    assert resp.status == "200 OK"

