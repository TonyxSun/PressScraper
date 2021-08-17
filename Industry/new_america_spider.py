import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class NewAmericaSpider(scrapy.Spider):
    name = "america"
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.newamerica.org/the-thread/', callback=self.parse)
    
    
    def parse(self, response):

        
        for item in response.css('[class="col-6 col-md-4"]'):
 
                    
            date = item.css('[class="margin-top-10"] *::text').get()
  
            if date != None:
                date_obj = datetime.strptime(date, "%b. %d, %Y").date()
            
            #if check_date(date):
            yield {
                'date': date,
                'title': item.css('[class="margin-15"] *::text').getall(),
                'url': item.css('[class="weekly-edition__articles__article margin-bottom-60"] a::attr(href)').getall(),
                
            }


# ALSO UPDATE ...
# script.bash
# exporter_mac.py
# README.md


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider new_america_spider.py -O output/new_america_" + date + ".csv"
cmdline.execute(execute.split())