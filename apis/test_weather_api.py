# -*- coding: utf-8 -*-
""" 
test_weather_api.py
@author: Clara
Module to unit test weather_api.py
"""

import unittest
import weather_api

class TestWeatherAPI(unittest.TestCase):
    """ Unit test cases"""
    def test_location1_cnt(self):
        """ Test case: Count dive sites"""
        _lat = 37.5407
        _lng = -77.4361
        _forecasts = weather_api.get_weather_forecast(_lat, _lng) 
        self.assertEqual(len(_forecasts), 14, "Wrong forecasts count")

    def test_location2_cnt(self):
        """ Test case: Count dive sites"""
        _lat = 37
        _lng = 77
        _forecasts = weather_api.get_weather_forecast(_lat, _lng) 
        self.assertEqual(_forecasts, None, "Wrong forecasts")

# Execute main
if __name__ == '__main__':
    unittest.main()
