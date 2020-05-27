# -*- coding: utf-8 -*-
""" 
whale_api.py
@author: Clara
Module to retrieve data from the hotline.whalemuseum.org API
"""

import requests
from datetime import datetime, timezone
from dateutil.parser import parse

class WhaleSighting:
    """ Properties of a whale sighting """
    def __str__(self):
        """ Convert object to string """
        return "Class WhaleSighting:" + '\n' + \
            'species = ' + str(self.species) + '\n' + \
            'sighted_at = ' + str(self.sighted_at)
    
    species = None
    sighted_at = None

def get_whale_sightings(lat, lng, dist, limit):
    """ Request whale sightings around lat and long within radius dist (nautical miles). Limit result to limit items"""
    # Request data 
    _response = requests.get("http://hotline.whalemuseum.org/api.json?near="+str(lat)+","+str(lng)+"&radius="+str(dist)+"&limit="+str(limit))
    
    # Create result
    _whale_sightings = []
    _now = datetime.now(timezone.utc)
    if _response.status_code == 200:
        _json_response = _response.json()
        for _whale in  _json_response:
            # Check only for sightings within the last 3 years
            _date_sighting = parse(_whale['sighted_at'])
            _delta = _now - _date_sighting
            _diff_days = _delta.days
            if (_diff_days < 3*365):
                _whaleSighting = WhaleSighting()
                _whaleSighting.species = _whale['species']
                _whaleSighting.sighted_at = _date_sighting
                _whale_sightings.append(_whaleSighting)
    
    return _whale_sightings
        