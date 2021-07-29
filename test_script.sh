#!/bin/sh

# Run exporter
python3 ./exporter_mac.py

# Upload to github
git add .
git commit -m "Update for $(date +'%b %d, %Y')"
git push