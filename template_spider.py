import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class TemplateSpider(scrapy.Spider):
    name = "template"
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.google.ca', callback=self.parse)
    
    
    def parse(self, response):
        
        for item in response.css("[class="x"]"):
            pass


# ALSO UPDATE ...
# script.bash
# exporter_mac.py


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider template_spider.py -O output/template_" + date + ".csv"
cmdline.execute(execute.split())