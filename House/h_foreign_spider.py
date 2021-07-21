import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date


class HouseForeignSpider(scrapy.Spider):
    name = "hforeign"
    
    def start_requests(self):
        
        urls = ['https://foreignaffairs.house.gov/press-releases',
                'https://foreignaffairs.house.gov/hearings',
                'https://foreignaffairs.house.gov/markups']
        
        categories = ["Press Release", "Hearing", "Markup"]
        
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': categories[i]})
            
            
        
    def parse(self, response):
        
        # Obtain category passed through meta
        category = response.meta["category"]
        
        
        # Obtain the following
        dates = response.css('[class="col-xs-1 recordListDate"]::text').getall()
        times = response.css('[class="col-xs-1 recordListTime"]::text').getall()
        titles = response.css('[class="ContentGrid"]::text').getall()
        urls = response.css('[class="recordListTitle"] a::attr(href)').getall()
        
        # For Press Releases, no time is given, so replace with None
        if len(times) == 0:
            for i in range(len(dates)):
                times.append(None)
        
        # For each entry, obtain and produce output
        for i in range(len(dates)):
            
            date = datetime.strptime(dates[i], "%m/%d/%y").date()
            # Continue is date was today or yesterday
            if check_date(date):
                
                yield {
                    'category': category,
                    'date': dates[i],
                    'time': times[i],
                    'title': titles[i],
                    'urls': response.urljoin(urls[i])
                    
                }
            
            
        
# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_foreign_spider.py -O output/h_foreign_" + date + ".csv"
cmdline.execute(execute.split())   
        
        
        