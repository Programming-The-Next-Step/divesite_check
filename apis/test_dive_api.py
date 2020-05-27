# -*- coding: utf-8 -*-
""" 
test_dive_api.py
@author: Clara
Module to unit test dive_api.py
"""

import unittest
import dive_api

class TestDiveAPI(unittest.TestCase):
    """ Unit test cases"""
    def test_location1_cnt1(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 20
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 67, "Wrong dive site count")

    def test_location1_cnt2(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 1
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 1, "Wrong dive site count")

    def test_location1_attributes(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 20
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        for _site in _sites:
            self.assertNotEqual(_site.ident, '', "Empty ident in "+str(_site))
            self.assertNotEqual(_site.lat, '', "Empty lat in "+str(_site))
            self.assertNotEqual(_site.lng, '', "Empty lng in "+str(_site))
            self.assertNotEqual(_site.name, '', "Empty name in "+str(_site))

    def test_location1_name(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 20
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        _found = False
        self.assertNotEqual(len(_sites), 0, "Wrong dive site count")        
        for _site in _sites:
            if _site.name == "100 Foot Rock":
                _found = True
        self.assertEqual(_found, True, "Dive spot '100 Foot Rock' not found")
        
    def test_location2_cnt1(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 200
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 12, "Wrong dive site count")

    def test_location2_cnt2(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 1
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 1, "Wrong dive site count")

    def test_location2_attributes(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 1
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        for _site in _sites:
            self.assertNotEqual(_site.ident, '', "Empty ident in "+str(_site))
            self.assertNotEqual(_site.lat, '', "Empty lat in "+str(_site))
            self.assertNotEqual(_site.lng, '', "Empty lng in "+str(_site))
            self.assertNotEqual(_site.name, '', "Empty name in "+str(_site))

            
    def test_location2_name(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 20
        _sites = dive_api.get_dive_sites(_lat, _lng, _dist) 
        _found = False
        self.assertNotEqual(len(_sites), 0, "Wrong dive site count")        
        for _site in _sites:
            if _site.name == "Shark point":
                _found = True
        self.assertEqual(_found, True, "Dive spot 'Shark point' not found")

# Execute main
if __name__ == '__main__':
    unittest.main()