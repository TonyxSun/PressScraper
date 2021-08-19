import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class NewAmericaSpider(scrapy.Spider):
    name = "america"
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.newamerica.org/publications/', callback=self.parse)
    
    
    def parse(self, response):
        
        text = response.css('[id="na-home"] *::text').extract()
        
        print (text)

        
        for item in response.css('[class~="col-6"]'):
            pass
            

# ALSO UPDATE ...
# script.bash
# exporter_mac.py
# README.md


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider new_america_spider.py -O output/new_america_" + date + ".csv"
cmdline.execute(execute.split())