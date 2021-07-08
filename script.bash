#!/bin/bash

cd ./Senate
python3 daily_digest_spider.py
python3 dailyBillsSenate.py
python3 sbanking_spider.py
python3 scommerce_spider.py
python3 sforeign_spider.py
python3 sfinance_spider.py
python3 shlsga_spider.py
python3 sjudiciary_spider.py
python3 floor_spider.py
python3 rollCallLists_Senate.py
cd ../Industry
python3 fcc_spider.py
python3 sia_spider.py
cd ..

