# Using the 'Open Weather Map' API

import requests

WEATHER_API_KEY = 'becb35ce5edff73926224c138d9520a8'
API_CALL = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={city name}&cnt={cnt}&mode=json&APPID={API key}'

class Weather:

    city_name = ''
    num_of_days_forecast = 1
    
    def __init__(self, city_name, state_code, num_of_days_forecast):
        self.city_name = city_name
        self.state_code = state_code
        self.num_of_days_forecast = num_of_days_forecast

        """
        City name, state code and country code divided by comma, use ISO 3166 country codes.
        You can specify the parameter not only in English.
        In this case, the API response should be returned in the same language as the language of requested location name if the location is in our predefined list of more than 200,000 locations.
        """

        self.get_todays_forecast()
    
    def get_todays_forecast(self):
        url = API_CALL.replace('{city name}', self.city_name).replace('{cnt}', str(self.num_of_days_forecast)).replace('{API key}', WEATHER_API_KEY)
        print(url)
        # r = requests.get(url)
        # print(r)
        # print(r.text)


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