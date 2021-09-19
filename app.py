import os
import requests
import json
import bottle
from bottle import route, template, run, error, abort
from dotenv import load_dotenv


# load coords from json
def read_json(fp):
    try:
        with open(fp, "r") as f:
            return json.load(f)
    except IOError as error:
        print("Coordinates did not load from file.")


# query for weather data
def get_weather(crds, key, unit):
    data = []
    
    try:
        # if no crds error will raise
        for k,v in crds.items():
            lat = crds[k][0]
            lon = crds[k][1]
            base = "https://api.openweathermap.org/data/2.5/"
            local = f"weather?&lat={lat}&lon={lon}&appid={key}&units={units}" 
            req = json.loads(requests.get(base+local).text)
            data.append(req)

    except AttributeError as error:
        print(f"{error}")  # log error 

    finally:
        # data returned will be none or a response
        return data


# main route
@route("/")
def weather():
    data = get_weather(crds, key, units)
    print(type(data))
    print(data)

    if data and data[0]["cod"] == 200:
        return template("report_weather.tpl", data=data)
    
    else:
        abort(404, "Something went wrong. Check logs.")
    

# load keys and model, these are global variables 
crds = read_json("./coords.json")  # if broken returns none
load_dotenv()
key = os.getenv("KEY")  # if broken returns 401 invalid api key
units = os.getenv("UNITS")  # if broken fails silently, gives temp in kelvin


# hook for gunicorn
app = bottle.default_app()


# hook for local dev with default host
if __name__ == "__main__":
   run(host="0.0.0.0", port=8080, debug=True, reloader=True)
