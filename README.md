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
