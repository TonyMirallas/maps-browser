#!/bin/bash
killall firefox
cd /home/tony/python/maps-browser/
source .venv/bin/activate
python3 initial_pages.py guitar
xdotool key Super+shift+Left
xdotool key alt+Tab
