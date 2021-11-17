# FRITZ!Box 6490 Cable - Reconnect Script

This script uses UPnP to reconnect the FRITZ!Box.

Tested with FRITZ!OS 7.12 on FRITZ!Box 6490 Cable and FRITZ!OS 7.27 on FRITZ!Box 6591 Cable.

## Preparation

Either install the `requests` library manually by running `pip install requests`. Or in case you have `pipenv` installed run `pipenv install` in the project folder (ideally in a _virtualenv_ managed by `pyenv`):

    $ pipenv install
    Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
    Pipfile.lock (b1592e) out of date, updating to (a290a1)...
    Locking [dev-packages] dependencies...
    Locking [packages] dependencies...
    Building requirements...
    Resolving dependencies...
    ✔ Success!
    Updated Pipfile.lock (a290a1)!
    Installing dependencies from Pipfile.lock (a290a1)...
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 4/4 — 00:00:00
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

## Execution

```
% python reconnect.py
<?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <s:Body>
    <u:ForceTerminationResponse xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:2"></u:ForceTerminationResponse>
  </s:Body>
</s:Envelope>
```
Idea from Ferry Boender: https://www.electricmonk.nl/log/2016/07/05/exploring-upnp-with-python/
