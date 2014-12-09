from unittest import TestCase

from py3status_modules.lastfm import Py3status


class TestLastfm(TestCase):

  def test_now_playing(self):
    lastfm = Py3status()
    now_playing = lastfm._get_now_playing()
    print now_playing

  def test_now_playing_formatted(self):
    lastfm = Py3status()
    now_playing = lastfm._now_playing_formatted()
    print now_playing

  def test_is_probably_not_still_playing(self):
    lastfm = Py3status()
    not_still_playing = lastfm._is_probably_not_still_playing()
    print not_still_playing
