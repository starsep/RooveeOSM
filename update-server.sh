#!/usr/bin/env bash
set -eu
date=$(/bin/date '+%Y%m%d')
git pull
rm -rf cache/overpass
source .venv/bin/activate
pip install -r requirements.txt
cd output
git pull
cd ..
python main.py
cd output
git config user.name "RooveeOSMBot"
git config user.email "<>"
git add .
git commit -m "Update $date"
git push origin gh-pages
cd ..
