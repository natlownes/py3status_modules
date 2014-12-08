import subprocess


class Py3status(object):
  '''
  for now just use shell script that gets weather
  information
  '''
  index = 0
  disabled = False


  def weather(self, json, i3status_config):
    full_text = subprocess.check_output(
      ["bash", "/home/nat/.weather/current.bash"])
    response = {
      'cached_until': 3600,
      'full_text': full_text,
      'name': 'weather'
    }
    return (self.index, response)
