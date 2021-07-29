#!/bin/bash

#for alternate use 

cd ./Senate
rm output/*
python sbanking_spider.py
python scommerce_spider.py
python sforeign_spider.py
python sfinance_spider.py
python shsgac_spider.py
python sjudiciary_spider.py
python senate_floor_spider.py
python senate_roll_call.py
Python sintelligence_spider.py

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

cd ../Industry
rm output/*
python sia_spider.py
python fcc_spider.py

cd ../Congress
rm output/*
python daily_digest_spider.py
python daily_bills.py
python all_bills_spider.py

cd ..

python ./exporter_win.py

# Upload to github
git add .
git commit -m "Update for $(date +'%b %d, %Y')"
git push

