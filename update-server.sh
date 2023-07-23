#!/usr/bin/env bash
set -eu
date=$(/bin/date '+%Y%m%d')
pip install -r requirements.txt
git clone https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/starsep/RooveeOSM --depth 1 --branch gh-pages output
rm -rf cache/overpass
python main.py
cd output
git config user.name "RooveeOSMBot"
git config user.email "<>"
git add .
git commit -m "Update $date"
git push origin gh-pages
