import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date

# Program to crawl the Republican's House committee on homeland

class HouseGOPHomelandSpider(scrapy.Spider):
    name = "h-gop-homeland"
    
    def start_requests(self):
        urls = ["https://republicans-homeland.house.gov/committee-activity/press-releases/",
                ]

        categories = ["Press Releases"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):
        
        # Recover category type found previously
        category = response.meta["category"]
        
        for item in response.css('[id^="post-"]'):
                
                # Get date
                date = item.css('[class="entry-date"] ::text').get()
                
                # Skip if date is None
                if date == None:
                    continue
                
                # Get date as object
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
                
                # If date is valid, extract data
                if check_date(date_obj):
            
                    yield {
                        'category': category,
                        'date': date,
                        'title': item.css('[class="post-title entry-title"] ::text').get(),
                        'url': response.css('[class="post-title entry-title"] a::attr(href)').get(),
                        'description': item.css('[class="entry-summary"] *::text').getall()[1]
                    }
                
        



# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider hgop_homeland_spider.py -O output/h_homeland_energy_" + date + ".csv"
cmdline.execute(execute.split())