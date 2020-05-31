""" 
weather_api.py
@author: Clara
Module to retrieve data from the openweathermap API
"""

import urllib
import json

appid = "XXX"

class WeatherForecast:
    """ Properties of a weather forecast """
    def __str__(self):
        """ Convert object to string """
        return "Class WeatherForecast:" + '\n' + \
            'weatherId = ' + str(self.weatherId) + '\n' + \
            'weatherMain = ' + str(self.weatherMain) + '\n' + \
            'weatherDescription = ' + str(self.weatherDescription) + '\n' + \
            'weatherIcon = ' + str(self.weatherIcon) + '\n' + \
            'mainTemp = ' + str(self.mainTemp) + '\n' + \
            'mainTempMin = ' + str(self.mainTempMin) + '\n' + \
            'mainTempMax = ' + str(self.mainTempMax) + '\n' + \
            'mainTempFeelsLike = ' + str(self.mainTempFeelsLike) + '\n' + \
            'windSpeed = ' + str(self.windSpeed) + '\n' + \
            'windDeg = ' + str(self.windDeg) + '\n' + \
            'cloudsAll = ' + str(self.cloudsAll) + '\n' 
    weatherId = None
    weatherMain = None
    weatherDescription = None
    weatherIcon = None
    mainTemp = None
    mainTempMin = None
    mainTempMax = None
    mainTempFeelsLike = None
    windSpeed = None
    windDeg = None
    cloudsAll = None
   
def get_weather_forecast(lat, lng):
    """ Request weather for lat and long """
    # Convert lat and long in valid range
    if (lat > 90):
        lat = lat - 180
    if (lng > 180):
        lng = lng -360
    if (lat < -90):
        lat = lat + 180
    if (lng < -180):
        lng = lng + 360
    # Request data 
    _response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lng)+"&appid="+str(appid))
    
    # Create result
    _weatherForecast = WeatherForecast()
    if _response.getcode() == 200:
        _html = _response.read()
        _json_response = json.loads(_html.decode('latin-1')) 
        if (_json_response != None):
            _weatherForecast.weatherId = _json_response['weather'][0]['id']
            _weatherForecast.weatherMain = _json_response['weather'][0]['main']
            _weatherForecast.weatherDescription = _json_response['weather'][0]['description']
            _weatherForecast.weatherIcon = _json_response['weather'][0]['icon']
            _weatherForecast.mainTemp = _json_response['main']['temp']
            _weatherForecast.mainTempMin = _json_response['main']['temp_min']
            _weatherForecast.mainTempMax = _json_response['main']['temp_max']
            _weatherForecast.mainTempFeelsLike = _json_response['main']['feels_like']
            _weatherForecast.windSpeed = _json_response['wind']['speed']
            _weatherForecast.windDeg = _json_response['wind']['deg']
            _weatherForecast.cloudsAll = _json_response['clouds']['all'] 
            
    return _weatherForecast

def weather_forecast_string_R(lat, lng):
    """ Return weather forecast in R format"""
    s = "main,icon, temp, temp_min, temp_max, feels_like, wind_speed, wind_deg, clouds_all\n"
    _forecast = get_weather_forecast(lat, lng)
    s += str(_forecast.weatherMain) + "," \
    + str(_forecast.weatherIcon) + "," \
    + str(_forecast.mainTemp) + "," \
    + str(_forecast.mainTempMin) + "," \
    + str(_forecast.mainTempMax) + "," \
    + str(_forecast.mainTempFeelsLike) + "," \
    + str(_forecast.windSpeed) + "," \
    + str(_forecast.windDeg) + "," \
    + str(_forecast.cloudsAll) \
    + "\n"

    return s
    
