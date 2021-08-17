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
        
        for item in response.css('[]'):
            
                    
            date = item.css('[]::text').get()
            date_obj = datetime.strptime(date, "").date()
            
            if check_date(date):
                yield {
                    'date': date,
                    'title': item.css('[]::text').get(),
                    'url': item.css('[] a::attr(href)').get(),
                    
                }


# ALSO UPDATE ...
# script.bash
# exporter_mac.py
# README.md


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider template_spider.py -O output/template_" + date + ".csv"
cmdline.execute(execute.split())