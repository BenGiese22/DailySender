# Using the 'Open Weather Map' API

class Weather:
    def __init__(self):
        print('weather instantiated')
    
    def other_method(self):
        print('other thing')


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