# -*- coding: utf-8 -*-
""" 
whale_api.py
@author: Clara
Module to retrieve data from the hotline.whalemuseum.org API
"""

import urllib
import json

class WhaleSighting:
    """ Properties of a whale sighting """
    def __str__(self):
        """ Convert object to string """
        return "Class WhaleSighting:" + '\n' + \
            'longitude = ' + str(self.longitude) + '\n' + \
            'latitude = ' + str(self.latitude) + '\n' + \
            'species = ' + str(self.species) + '\n' + \
            'sighted_at = ' + str(self.sighted_at)
    
    species = None
    sighted_at = None
    longitude = None
    latitude = None

def get_whale_sightings(lat, lng, dist, limit):
    """ Request whale sightings around lat and long within radius dist (nautical miles). Limit result to limit items"""
    # Request data 
    _url="http://hotline.whalemuseum.org/api.json?near="+str(lat)+","+str(lng)+"&radius="+str(dist)+"&limit="+str(limit)
    _req = urllib.request.Request(_url, headers={'User-Agent': 'Mozilla/5.0'})
    _response = urllib.request.urlopen(_req)
    
    # Create result
    _whale_sightings = []
    if _response.getcode() == 200:
        _html = _response.read()
        _json_response = json.loads(_html.decode('latin-1'))   
        for _whale in  _json_response:
            _whaleSighting = WhaleSighting()
            _whaleSighting.longitude = _whale['longitude']
            _whaleSighting.latitude = _whale['latitude']
            _whaleSighting.species = _whale['species']
            _whaleSighting.sighted_at = _whale['sighted_at']
            _whale_sightings.append(_whaleSighting)
    
    return _whale_sightings
    
def whale_sightingss_string_R(lat, lng, dist, limit):
    """ Return whale sightings in R format"""
    s = "lat,lng, species, sighted_at\n"
    for _whale in get_whale_sightings(lat, lng, dist, limit):
        s += str(_whale.latitude) + "," +str(_whale.longitude) + "," + str(_whale.species) + "," + str(_whale.sighted_at) + "\n"

    return s
    
