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

py3_modules will go in this directory:

```
~/.i3/py3status
```

this means that the actual python files go in that directory.  I symlink the
`py3status_modules` directory to `~/.i3/py3status`

### Example output

in the i3bar, clicking the text of any of these modules will refresh the output

##### Weather

Your current zipcode will be detected from your IP address, as will your
latitude and longitude, which will be used in the request to the NOAA.  Results
may vary.  Temperatures, wind direction and wind speed will be displayed.
Depends on the `location.py` file and the `requests` library.

```
19125: 36.0°F (2.2°C), ☴WNW@7MPH
```

##### last.fm

Yep.  Depends on `requests`.

```
Run the Jewels – Crown (feat. Diane Coffee)
```
