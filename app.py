import os
import requests
import json
import bottle
from bottle import route, template, run, error
from dotenv import load_dotenv


# load coords from json
def read_json(fp):
    try:
        with open(fp, "r") as f:
            return json.load(f)
    except IOError as error:
        print("coords did not load from file")


# query for weather data
def get_weather():
    urls = []
    # this is an error point, from the server point of view
    # AttributeError: NoneType for any item in the dict
    try:
        for k,v in crds.items():
            lat = crds[k][0]
            lon = crds[k][1]
            base = "https://api.openweathermap.org/data/2.5/"
            local = f"weather?&lat={lat}&lon={lon}&appid={key}&units={units}" 
            urls.append(base+local)
    except AttributeError as error:
        print(f"{error} --> nothing in the dictionary")

    # need to see what this returns when the key or url is wrong
    return [json.loads(requests.get(url).text) for url in urls if url]


# main route
@route("/")
def weather_():
    # put this in a try/except, have an error page if it fails
    # if get_weather fails it will just return and empty list
    # if data is empty a blank template will render
    data = get_weather()
    print(data) 
    # main view
    return template("report_weather.tpl", data=data)


# handle 500 internal server error


# load keys and model, these are global variables 
crds = read_json("./coords.json")
load_dotenv()
key = os.getenv("KEY")
units = os.getenv("UNITS")


# hook for gunicorn
app = bottle.default_app()


# hook for local dev with default host
if __name__ == "__main__":
   run(host="0.0.0.0", port=8080, debug=True, reloader=True)
