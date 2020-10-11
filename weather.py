# Using the 'Open Weather Map' API
# Reference: https://openweathermap.org/api/one-call-api

from datetime import datetime
import requests
import json

WEATHER_API_KEY = 'becb35ce5edff73926224c138d9520a8'
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&units={units}&APPID={api_key}'

# exclude param options: current, minutely, hourly, daily, alerts

class Weather:

    latitude = ''
    longitude = ''
    exclude = 'current,minutely,hourly,alerts'
    units = 'imperial'

    low_temp = 0
    high_temp = 100
    wind_speed = 0
    cloud_percentage = 0
    precipation_probability = 0.00 # Represents a decimal value, 0.29 = 29% chance of preciptation

    # dt = datetime.utcfromtimestamp(int(today_json["dt"]))

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

        json_resp = self.make_request()
        self.get_todays_forecast(json_resp)
    
    def make_request(self):
        url = API_ENDPOINT.format(latitude=self.latitude,longitude=self.longitude,exclude=self.exclude,units=self.units,api_key=WEATHER_API_KEY)
        r = requests.get(url)
        return json.loads(r.text)

    def get_todays_forecast(self, json_str):
        today_json = json_str["daily"][0]
        self.low_temp = int(today_json["temp"]["min"])
        self.high_temp = int(today_json["temp"]["max"])
        self.wind_speed = int(today_json["wind_speed"])
        self.cloud_percentage = int(today_json["clouds"])
        self.precipation_probability = float(today_json["pop"])

    def pretty_print_json(self, json_str):
        print(json.dumps(json_str, indent=2))