import requests

from json import loads
from os import path


class Location(object):
  '''
  use the ipinfo.io service to return a location object
  if a $HOME/.location.json exists, just return that
  '''

  def _get_location(self):
    url                = 'http://ipinfo.io/json'
    home_dir           = path.expanduser("~")
    location_file_path = path.join(home_dir, ".location.json")
    '''
    return object:
      {
        'latitude':   40,
        'longitude':  -75,
        'zipcode':    19125,
      }
    '''

    def has_location_file():
      return path.isfile(location_file_path)

    def request():
      r = requests.get(url)
      response = r.json()
      latitude, longitude = response['loc'].split(',')
      return {
        'latitude':   latitude,
        'longitude':  longitude,
        'zipcode':    response.get('postal', '')
      }

    def read_local():
      with open(location_file_path, 'r') as f:
        return loads(f.read())

    if has_location_file():
      return read_local()
    else:
      return request()
