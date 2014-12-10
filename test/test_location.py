from unittest import TestCase

from py3status_modules.location import Location


class TestLocation(TestCase):

  def test_get_location(self):
    location = Location()._get_location()
    assert location['longitude']
    assert location['latitude']
    assert location['zipcode']
