import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date

# Program to crawl the Senate Select Committee on Intelligence, and extract information about press releases.

class SenateIntelligenceSpider(scrapy.Spider):
    name = "sintelligence"

    def start_requests(self):

        # Urls for minority and majority press releases
        urls = ["https://intelligence.house.gov/news/"]

        # Go into each webpage
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse)

    def parse(self, response):
        
        for item in response.css('[class="newsblocker"]'):
            
            date = item.css('[class="newsie-details"] ::text').getall()[1]
            
            date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            if check_date(date_obj):
                
                yield {
                    'date' : date,
                    'title': item.css('[class="newsie-titler"] *::text').get(),
                    'url' : response.urljoin(item.css('[class="newsie-titler"] a::attr(href)').get()),
                    'summary': item.css('[class="newsbody"] ::text').getall()[1],
                    
                
                }
            
    
# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider sintelligence_spider.py -O output/sintelligence_" + date + ".csv"
cmdline.execute(execute.split())
        