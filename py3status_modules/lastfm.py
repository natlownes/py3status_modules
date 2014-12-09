import os
import requests
from time import time


class Py3status(object):
  '''
  http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=crabwhittaker&api_key=6760190ec250ec3382636898fc4e53e0&format=json&now_playing=true&limit=2
  '''
  index    = 0
  disabled = False
  base_uri = 'http://ws.audioscrobbler.com/2.0/'
  api_key  = '6760190ec250ec3382636898fc4e53e0'
  user     = 'crabwhittaker'

  def now_playing(self, json, i3status_config):
    full_text = ''
    if not self.disabled:
      full_test = self._now_playing_formatted()
    response = {
      'cached_until':  self._cached_until(),
      'full_text':     full_text,
      'name':          'last.fm'
    }

    return (self.index, response)

  def on_click(self, i3status_output_json, i3status_config, event):
    os.system("killall -USR1 py3status")

  def _params(self):
    return {
      'api_key':      self.api_key,
      'format':       'json',
      'limit':        2,
      'method':       'user.getrecenttracks',
      'now_playing':  True,
      'user':         self.user,
    }

  def _cached_until(self):
    return time() + 120

  def _is_currently_playing(self):
    '''
    if the "currently playing" song was started more than 20 minutes ago,
    assume that we've stopped listening/are listening to Iron Butterfly
    '''
    now_playing = self._get_now_playing().get('@attr')
    return now_playing and now_playing.get('nowplaying')

  def _get_now_playing(self):
    request = requests.get(self.base_uri, params=self._params())
    request.json()

    now_playing = request.json()['recenttracks']['track'][0]
    return {
      'artist':     now_playing['artist']['#text'],
      'track':      now_playing['name'],
      '@attr':      now_playing.get('@attr')
    }

  def _now_playing_formatted(self):
    now_playing = self._get_now_playing()
    playing = '%s - %s' % (now_playing['artist'], now_playing['track'],)
    if not self._is_currently_playing():
      return ''
    else:
      return playing
