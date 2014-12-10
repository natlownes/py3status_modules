# -*- coding: utf-8 -*-
from time import time
import requests
from location import Location


def to_celsius(f_str):
  return round(((float(f_str) - 32) * 5 / 9), 1)


class Py3status(Location):
  '''
  http://forecast.weather.gov/MapClick.php?lat=38.4247341&lon=-86.9624086&FcstType=json
  icons = ['☀', '☁', '☂', '☃']
  current observations reference:
    - http://w1.weather.gov/xml/current_obs/weather.php
  '''
  index    = 1
  disabled = False
  base_uri = 'http://forecast.weather.gov/MapClick.php'

  def show(self, json, i3status_config):
    full_text = ''
    if not self.disabled:
      full_text = self._formatted()
    response = {
      'cached_until':  self._cached_until(),
      'full_text':     full_text,
      'name':          'weather_noaa'
    }
    return (self.index, response,)

  def _cached_until(self):
    return time() + 60 * 30

  def _formatted(self):
    weather = self._get()
    output = u"%s: %s°F (%s°C), wind @ %sMPH" % (
      weather['zipcode'],
      float(weather['Temp']),
      to_celsius(weather['Temp']),
      weather['Winds'],
    )
    return output

  def _get(self):
    params = self._params()
    r = requests.get(self.base_uri, params=params)
    observation = r.json()['currentobservation']
    # replace the observations lat/lng with our lat/lng/zip
    observation['latitude']  = params['lat']
    observation['longitude'] = params['lon']
    observation['zipcode']   = params['zipcode']
    return observation

  def _params(self):
    location = self._get_location()
    return {
      'lat':       location['latitude'],
      'lon':       location['longitude'],
      'zipcode':   location['zipcode'],
      'FcstType':  'json',
    }
