# method unit tests
import pytest
from app import get_weather, crds, key, units 

# for web integration tests
# import app
# import webtest
# test if get_weather returns 200.
# if test fails config or openweather is broken.

# run with python -m pytest tests/ from project root
# this will add root to sys.path

def test_get_weather():
    """
    integration test to confirm that weather data is returned form openweather.

    test uses coordinates, api key, and units from config files in app.

    test passes if data is a list and status code in first response is 200.

    if test fails something is wrong with the method or config files. 
    """

    data = get_weather(crds, key, units)
    assert data
    assert type(data) == list
    assert type(data[0]) == dict
    assert data[0]["cod"] == 200

