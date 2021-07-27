#!/bin/bash

cd ./Senate
rm output/*
python3 sbanking_spider.py
python3 scommerce_spider.py
python3 sforeign_spider.py
python3 sfinance_spider.py
python3 shsgac_spider.py
python3 sjudiciary_spider.py
python3 senate_floor_spider.py
python3 senate_roll_call.py

cd ../House
rm output/*
python3 h_energy_spider.py
python3 h_financial_spider.py
python3 h_foreign_spider.py
python3 h_homeland_spider.py
python3 h_science_spider.py
python3 h_transportation_spider.py
python3 hgop_energy_spider.py
python3 hgop_foreign_spider.py
python3 hgop_homeland_spider.py
python3 hgop_science_spider.py

cd ../Industry
rm output/*
python3 sia_spider.py
python3 fcc_spider.py

cd ../Congress
rm output/*
python3 daily_digest_spider.py
python3 daily_bills.py
python3 all_bills_spider.py

cd ..

python3 ./exporter2.py

