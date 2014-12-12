# -*- coding: utf-8 -*-
from time import time
import requests
from location import Location


def to_celsius(f_str):
  return round(((float(f_str) - 32) * 5 / 9), 1)


def azimuth_to_cardinal(azimuth):
  '''
  return a cardinal direction from an azimuth
  '''
  azimuth = float(azimuth)
  diff = 22.5
  cardinals = {
    'N':    0.0,
    'NNE':  22.5,
    'NE':   45.0,
    'ENE':  67.5,
    'E':    90.0,
    'ESE':  112.5,
    'SE':   135.0,
    'SSE':  157.5,
    'S':    180,
    'SSW':  202.5,
    'SW':   225.0,
    'WSW':  247.5,
    'W':    270.0,
    'WNW':  292.5,
    'NW':   315.0,
    'NNW':  337.5,
  }
  if azimuth == 360:
    return 'N'
  for k, v in cardinals.iteritems():
    if azimuth >= v and azimuth <= v + diff:
      return k


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
    wind_direction = azimuth_to_cardinal(weather['Windd'])
    output = u"%s: %s°F (%s°C), ☴%s@%sMPH" % (
      weather['zipcode'],
      float(weather['Temp']),
      to_celsius(weather['Temp']),
      wind_direction,
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
