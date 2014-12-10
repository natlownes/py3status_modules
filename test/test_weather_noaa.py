from unittest import TestCase

from py3status_modules.weather_noaa import Py3status


class TestWeatherNoaa(TestCase):

  def test_current_location(self):
    weather = Py3status()
    print weather._get_location()

  def test_get_weather(self):
    weather = Py3status()
    print weather._get()

  def test_formatted(self):
    weather = Py3status()
    print weather._formatted()

