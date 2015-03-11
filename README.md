# py3status modules

~/.i3status.conf should include:

```
general {
    colors = true
    interval = 5
    output_format = "i3bar"
}
```

~/.i3/config should include:

```
bar {
  status_command py3status
}
```

the py3status_modules directory should be copied to or symlinked to:

```
~/.i3/py3status/py3status_modules
```

### Example output

in the i3bar, clicking the text of any of these modules will refresh the output

##### Weather

Displays weather for your current location.

Your current location can be detected from your IP address, which may or may not be
accurate enough.  You can manually set your latitude, longitude, and zipcode in
a `~/.location.json` file:

```
{
  "latitude":   39.9491605,
  "longitude":  -75.1658003,
  "zipcode":    "19102"
}
```

these parameters will be used in the request to the NOAA.  Temperatures, wind
direction and wind speed will be displayed.  Depends on the `location.py` file
and the `requests` library.

```
19125: 36.0°F (2.2°C), ☴WNW@7MPH
```

##### last.fm

Yep.  Depends on `requests`.

```
Run the Jewels – Crown (feat. Diane Coffee)
```
