#!/bin/bash

cd ./Senate
python daily_digest_spider.py
python dailyBillsSenate.py
python sbanking_spider.py
python scommerce_spider.py
python sforeign_spider.py
python sfinance_spider.py
python shlsga_spider.py
python sjudiciary_spider.py
python floor_spider.py
python rollCallLists_Senate.py
cd ../Industry
python fcc_spider.py
python sia_spider.py
cd ..

