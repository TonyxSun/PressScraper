#!/bin/bash

# Run spiders
cd ./Senate
rm output/*
python sbanking_spider.py
python scommerce_spider.py
python sforeign_spider.py
python sfinance_spider.py
python shsgac_spider.py
python sjudiciary_spider.py
python sintelligence_spider.py
python senate_floor_spider.py
python senate_roll_call.py

cd ../House
rm output/*
python h_energy_spider.py
python h_financial_spider.py
python h_foreign_spider.py
python h_homeland_spider.py
python h_science_spider.py
python h_transportation_spider.py
python hgop_energy_spider.py
python hgop_foreign_spider.py
python hgop_homeland_spider.py
python hgop_science_spider.py
python h_intelligence_spider.py


cd ../Industry
rm output/*
python sia_spider.py
python fcc_spider.py
python wilson_spider.py
python brookings_spider.py
python csis_spider.py
python aspi_spider.py
python icas_spider.py
python atlantic_spider.py

cd ../Congress
rm output/*
python daily_digest_spider.py
python daily_bills.py
python all_bills_spider.py

cd ..

# Run exporter
python ./exporter_mac.py

# Upload to github
git pull
git add .
git commit -m "Update for $(date +'%b %d, %Y')" 
git push --set-upstream origin main

