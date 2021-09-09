import pytest
import app
import boddle  # not sure if needed

# this handles the unit testing of methods (get_weather)
# wsgi app server not needed

def test_get_weather():
    # mock weather response
    crds = None
    key = None
    units = None
    data = weather(crds, key, units)
    # assert
    pass


def test_get_weather_empty():
    # mock empty response
    bad_crds = None
    key = None
    units = None
    data = weather(bad_crds, key, units)
    pass


def test_get_weather_bad_key():
    # mock bad api
    crds = None
    bad_key = None
    units = None
    data = weather(crds, bad_key, units)
    pass



