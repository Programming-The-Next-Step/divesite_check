""" diveAPI.py
Module to retrieve data from the divesites API
"""

import unittest
import requests
import json

class DiveSite:
    """ Properties of a dive site """
    def __str__(self):
        """ Convert object to string """
        return "Class DiveSite:" + '\n' + \
            'ident = ' + str(self.ident) + '\n' + \
            'lat = ' + str(self.lat) + '\n' + \
            'lng = ' + str(self.lng) + '\n' + \
            'name = ' + str(self.name) + '\n' + \
            'currents =  ' + str(self.currents) + '\n' + \
            'description =  ' + str(self.description) + '\n' + \
            'distance =  ' + str(self.distance) + '\n' + \
            'equipment =  ' + str(self.equipment) + '\n' + \
            'hazards =  ' + str(self.hazards) + '\n' + \
            'marinelife =  ' + str(self.marinelife) + '\n' + \
            'maxdepth =  ' + str(self.maxdepth) + '\n' + \
            'mindepth =  ' + str(self.mindepth) + '\n' + \
            'predive =  ' + str(self.predive) + '\n' + \
            'water =  ' + str(self.water) + '\n'
        
    ident = None
    lat = None
    lng = None
    name = None
    currents = None
    description = None
    distance = None
    equipment = None
    hazards = None
    marinelife = None
    maxdepth = None
    mindepth = None
    predive = None
    water = None

def dive_sites(lat, lng, dist):
    """ Request dive sites around lat and long within radius dist (nautical miles)"""
    # Request data 
    _response = requests.get("http://api.divesites.com/?mode=sites&lat="+str(lat)+"&lng="+str(lng)+"&dist="+str(dist))
    
    # Create result
    _diveSites = []
    if _response.status_code == 200:
        _json_response = _response.json()          
        # Parse sites
        for site in  _json_response['sites']:
            _diveSite = DiveSite()
            _diveSite.ident = site['id']
            _diveSite.lat = site['lat']
            _diveSite.lng = site['lng']
            _diveSite.name = site['name']
            _diveSite.currents = site['currents']
            _diveSite.description = site['description']
            _diveSite.equipment = site['equipment']
            _diveSite.hazards = site['hazards']
            _diveSite.marinelife = site['marinelife']
            _diveSite.maxdepth = site['maxdepth']
            _diveSite.mindepth = site['mindepth']
            _diveSite.predive = site['predive']
            _diveSites.append(_diveSite)
        
    return _diveSites


class TestDiveAPI(unittest.TestCase):
    """ Unit test cases"""
    def test_location1_cnt1(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 20
        _sites = dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 67, "Wrong dive site count")

    def test_location1_cnt2(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 1
        _sites = dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 1, "Wrong dive site count")

    def test_location1_attributes(self):
        """ Test case: Count dive sites"""
        _lat = 47.6031537682643
        _lng = -122.336164712906
        _dist = 20
        _sites = dive_sites(_lat, _lng, _dist) 
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
        _sites = dive_sites(_lat, _lng, _dist) 
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
        _sites = dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 12, "Wrong dive site count")

    def test_location2_cnt2(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 1
        _sites = dive_sites(_lat, _lng, _dist) 
        self.assertEqual(len(_sites), 1, "Wrong dive site count")

    def test_location2_attributes(self):
        """ Test case: Count dive sites"""
        _lat = -8.350785
        _lng = 116.038628
        _dist = 1
        _sites = dive_sites(_lat, _lng, _dist) 
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
        _sites = dive_sites(_lat, _lng, _dist) 
        _found = False
        self.assertNotEqual(len(_sites), 0, "Wrong dive site count")        
        for _site in _sites:
            if _site.name == "Shark point":
                _found = True
        self.assertEqual(_found, True, "Dive spot 'Shark point' not found")

# Execute main
if __name__ == '__main__':
    unittest.main()


