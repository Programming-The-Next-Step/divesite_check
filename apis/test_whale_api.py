""" 
test_whale_api.py
@author: Clara
Module to unit test whale_api.py
"""

import unittest
import whale_api

class TestWhaleAPI(unittest.TestCase):
    """ Unit test cases"""
    def test_location1_cnt1(self):
        """ Test case: Count whales"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = .1
        _limit = 10
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 9, "Wrong whales count")
        
    def test_location1_cnt2(self):
        """ Test case: Count whales"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = .5
        _limit = 100
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 100, "Wrong whales count")

    def test_location1_cnt3(self):
        """ Test case: Count whales"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 50
        _limit = 100
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 100, "Wrong whales count")

    def test_location2_cnt1(self):
        """ Test case: Count whales"""
        _lat = 48.5159
        _lng = -123.1524
        _dist = 1
        _limit = 100
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 100, "Wrong whales count")

    def test_location2_cnt2(self):
        """ Test case: Count whales"""
        _lat = 48.5159
        _lng = -123.1524
        _dist = 10
        _limit = 100
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 100, "Wrong whales count")

    def test_location2_cnt3(self):
        """ Test case: Count whales"""
        _lat = 48.5159
        _lng = -123.1524
        _dist = 1000
        _limit = 100
        _sites = whale_api.get_whale_sightings(_lat, _lng, _dist, _limit) 
        self.assertEqual(len(_sites), 100, "Wrong whales count")

# Execute main
if __name__ == '__main__':
    unittest.main()