import subprocess

from time import time


class Py3status(object):
  '''
  for now just use shell script that gets weather
  information
  '''
  index = 1
  disabled = False

  def weather(self, json, i3status_config):
    if self.disabled:
      return
    response = {
      'cached_until':  time() + 3600,
      'full_text':     self._get_weather(),
      'name':          'weather'
    }
    return (self.index, response)

  def _get_weather(self):
    return subprocess.check_output(
      ["bash", "/home/nat/.weather/current.bash"]).strip()
