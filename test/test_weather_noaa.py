from unittest import TestCase

from py3status_modules.weather_noaa import Py3status
from py3status_modules.weather_noaa import azimuth_to_cardinal


class TestWeatherNoaa(TestCase):

  def test_azimuth_to_cardinal(self):
    print azimuth_to_cardinal(12.5)

  def test_azimuth_to_cardinal_with_variable_wind_direction(self):
    '''
    NOAA seems to send the 'windd' value as 999 if wind is variable
    '''
    print azimuth_to_cardinal('999')

  def test_current_location(self):
    weather = Py3status()
    print weather._get_location()

  def test_get_weather(self):
    weather = Py3status()
    print weather._get()

  def test_formatted(self):
    weather = Py3status()
    print weather._formatted()

