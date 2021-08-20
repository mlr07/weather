import os
import requests
import json
import bottle
from bottle import route, template, run, error
from dotenv import load_dotenv

# load coords from json
def read_json(fp):
    with open(fp, "r") as f:
        return json.load(f)

# query for weather data
def get_weather():
    urls = []

    for k,v in crds.items():
        lat = crds[k][0]
        lon = crds[k][1]
        base = "https://api.openweathermap.org/data/2.5/"
        local = f"weather?&lat={lat}&lon={lon}&appid={key}&units={units}" 
        urls.append(base+local)
        #urls.append(f"https://api.openweathermap.org/data/2.5/weather?&lat={lat}&lon={lon}&appid={key}&units={units}")

    return [json.loads(requests.get(url).text) for url in urls if url]

# main route
@route("/")
def weather_():
    data = get_weather()
    # main view
    return template("report_weather.tpl", data=data)

# handle bad data in url
@error(403)
def mistake403(error):
    return "There was an error in the URL."

# handle incorrect url
@error(404)
def mistake404(error):
    return "This page does not exist."

# load keys and model 
load_dotenv()
key = os.getenv("KEY")
units = os.getenv("UNITS")
crds = read_json("./coords.json")

# hook for local dev with default host
if __name__ == "__main__":
   run(host="0.0.0.0", port=8080, debug=True, reloader=True)

# hook for gunicorn
app = bottle.default_app()
