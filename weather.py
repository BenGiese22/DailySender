# Using the 'Open Weather Map' API
# Reference: https://openweathermap.org/api/one-call-api

import requests

WEATHER_API_KEY = 'becb35ce5edff73926224c138d9520a8'
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude={exclude}&units={units}&APPID={api_key}'

# exclude param options: current, minutely, hourly, daily, alerts

class Weather:

    latitude = ''
    longitude = ''
    exclude = ''
    units = ''

    def __init__(self, latitude, longitude, exclude, units):
        self.latitude = latitude
        self.longitude = longitude
        self.exclude = exclude
        self.units = units

        self.make_request()
    
    def make_request(self):
        url = API_ENDPOINT.format(latitude=self.latitude,longitude=self.longitude,exclude=self.exclude,units=self.units,api_key=WEATHER_API_KEY)
        print(url)
        r = requests.get(url)
        print(r)
        print(r.text)

    def get_todays_forecast(self):
        print('temp')


"""
import requests

url = "https://rapidapi.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""