#!/bin/zsh
set -eu
unsetopt bgnice
cd "$(dirname "$0")/prototype"
if ! python3 -c 'import requests' >/dev/null 2>&1; then
  echo 'The Python requests package is missing. Follow README.md to install the dependencies.'
  read -r '?Press Return to close.'
  exit 1
fi
if python3 - <<'PY'
import urllib.request,webbrowser
try:
    with urllib.request.urlopen('http://127.0.0.1:8765/api/state',timeout=1) as response:
        import json
        state=json.load(response)
        if state.get('profile')=='coordination_only':
            webbrowser.open('http://127.0.0.1:8765')
            raise SystemExit(0)
except (OSError,ValueError):
    pass
raise SystemExit(1)
PY
then
  exit 0
fi
(sleep 1; open 'http://127.0.0.1:8765') &
exec python3 server.py
