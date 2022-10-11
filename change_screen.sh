#!/bin/bash
cd /home/tony/python/maps-browser/
source .venv/bin/activate
python3 initial_pages.py twitch
xdotool key Super+shift+Left
xdotool key alt+Tab
