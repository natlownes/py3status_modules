import requests


class Location(object):
  url = 'http://ipinfo.io/json'

  def _get_location(self):
    '''
    return object:
      {
        'latitude':   40,
        'longitude':  -75,
        'zipcode':    19125,
      }
    '''
    r = requests.get(self.url)
    response = r.json()
    latitude, longitude = response['loc'].split(',')
    return {
      'latitude':   latitude,
      'longitude':  longitude,
      'zipcode':    response['postal']
    }
