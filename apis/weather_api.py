# -*- coding: utf-8 -*-
""" 
weather_api.py
@author: Clara
Module to retrieve weather forecast data from the National Weather Service API
"""

import unittest
import requests
import json

class WeatherForecast:
    """ Properties of a weather forecast """
    def __str__(self):
        """ Convert object to string """
        return "Class WeatherForecast:" + '\n' + \
            'number = ' + str(self.number) + '\n' + \
            'name = ' + str(self.name) + '\n' + \
            'startTime = ' + str(self.startTime) + '\n' + \
            'endTime = ' + str(self.endTime) + '\n' + \
            'isDaytime =  ' + str(self.isDaytime) + '\n' + \
            'temperature =  ' + str(self.temperature) + '\n' + \
            'temperatureUnit =  ' + str(self.temperatureUnit) + '\n' + \
            'temperatureTrend =  ' + str(self.temperatureTrend) + '\n' + \
            'windSpeed =  ' + str(self.windSpeed) + '\n' + \
            'windDirection =  ' + str(self.windDirection) + '\n' + \
            'icon =  ' + str(self.icon) + '\n' + \
            'shortForecast =  ' + str(self.shortForecast) + '\n' + \
            'detailedForecast =  ' + str(self.detailedForecast) + '\n' 
    number = None
    name = None
    startTime = None
    endTime = None
    isDaytime = None
    temperature = None
    temperatureUnit = None
    temperatureTrend = None
    windSpeed = None
    windDirection = None
    icon = None
    shortForecast = None
    detailedForecast = None

def get_weather_forecast_endpoint(lat, lng):
    """ Request weather forecast endpoint around lat and long"""
    # Request data 
    _response = requests.get("https://api.weather.gov/points/"+str(lat)+","+str(lng))
    
    _endpoint = None
    if _response.status_code == 200:
        # Retrieve forecast endpoint
        _json_response = _response.json()    
        properties = _json_response['properties']
        if (properties != None) :
            _endpoint = properties['forecast']
    return _endpoint

def get_weather_forecast_details(endpoint):
    """ Request weather forecast from endpoint """
    # Request data 
    _response = requests.get(endpoint)
    
    _weatherForecasts = []
    if _response.status_code == 200:
        # Retrieve forecasts from forecast endpoint
        _json_response = _response.json()    
        _properties = _json_response['properties']
        if (_properties != None):
            for _forecast in _properties['periods']:
                _weatherForecast = WeatherForecast()
                _weatherForecast.number = _forecast['number']
                _weatherForecast.name = _forecast['name']
                _weatherForecast.startTime = _forecast['startTime']
                _weatherForecast.endTime = _forecast['endTime']
                _weatherForecast.isDaytime = _forecast['isDaytime']
                _weatherForecast.temperature = _forecast['temperature']
                _weatherForecast.temperatureUnit = _forecast['temperatureUnit']
                _weatherForecast.temperatureTrend = _forecast['temperatureTrend']
                _weatherForecast.windSpeed = _forecast['windSpeed']
                _weatherForecast.windDirection = _forecast['windDirection']
                _weatherForecast.icon = _forecast['icon']
                _weatherForecast.shortForecast = _forecast['shortForecast']
                _weatherForecast.detailedForecast = _forecast['detailedForecast'] 
                _weatherForecasts.append(_weatherForecast)
                
    return _weatherForecasts

def get_weather_forecast(lat, lng):
    """ Request waether forecasts for lat, lng """
    _endpoint = get_weather_forecast_endpoint(lat, lng)
    _ret = None
    if (_endpoint != None):
       _ret = get_weather_forecast_details(_endpoint)
       
    return _ret


