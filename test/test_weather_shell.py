from unittest import TestCase

from py3status_modules.weather_shell import Py3status


class TestWeatherShell(TestCase):

  def test_output(self):
    weather = Py3status()

    print weather._get_weather()

