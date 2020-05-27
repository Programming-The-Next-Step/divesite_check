# -*- coding: utf-8 -*-
""" 
dive_api.py
@author: Clara
Module to retrieve data from the divesites.com API
"""

import requests

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

def get_dive_sites(lat, lng, dist):
    """ Request dive sites around lat and long within radius dist (nautical miles)"""
    # Request data 
    _response = requests.get("http://api.divesites.com/?mode=sites&lat="+str(lat)+"&lng="+str(lng)+"&dist="+str(dist))
    
    # Create result
    _diveSites = []
    if _response.status_code == 200:
        _json_response = _response.json()          
        # Parse sites
        for _site in  _json_response['sites']:
            _diveSite = DiveSite()
            _diveSite.ident = _site['id']
            _diveSite.lat = _site['lat']
            _diveSite.lng = _site['lng']
            _diveSite.name = _site['name']
            _diveSite.currents = _site['currents']
            _diveSite.description = _site['description']
            _diveSite.equipment = _site['equipment']
            _diveSite.hazards = _site['hazards']
            _diveSite.marinelife = _site['marinelife']
            _diveSite.maxdepth = _site['maxdepth']
            _diveSite.mindepth = _site['mindepth']
            _diveSite.predive = _site['predive']
            _diveSites.append(_diveSite)
        
    return _diveSites
