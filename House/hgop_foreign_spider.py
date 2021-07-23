import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline


# Program to crawl the Republican Energy and Commerce Committee webpage, and extract information about recent headlines.

class HouseGOPForeignSpider(scrapy.Spider):
    name = "h-gop-foreign"
    
    def start_requests(self):
        urls = ["https://gop-foreignaffairs.house.gov/press-release/",
                "https://gop-foreignaffairs.house.gov/markup/",
                "https://gop-foreignaffairs.house.gov/hearing/"
                ]

        categories = ["Press Releases", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):
        
        
        # Recover category type found previously
        category = response.meta["category"]
        
        
        # PRESS RELEASES
        
        # Get all text
        all_text = response.css('[class="post"] *::text').extract()
        
        # Will store dates
        dates = []
        
        # Iterate through all text and put dates in dates list
        for text in all_text:
            if len(text) == 8 and "." in text:
                dates.append(text)
        
        # Counter for dates list
        i = -1
        
        for item in response.css('[class="post"]'):
            
            i += 1

            date_obj = datetime.strptime(dates[i], "%m.%d.%y").date()
            
            if check_date(date_obj):
            
                yield {
                    'category': category,
                    'date': dates[i],
                    'title': item.css('[class="headline"] ::text').get(),
                    'url': item.css('[class="headline"] a::attr(href)').get(),
                    'summary': item.css('[class="post-content"] ::text').getall()[1],
                }
        
        
        # MARKUPS and HEARINGS
        
        for item in response.css('[class="event-day"]'):
            
            # Obtain date
            date = item.css('[class="event-date"] ::text').get()
            # Change to date obj
            date_obj = datetime.strptime(date, "%A, %B %d, %Y").date()
            
            # Continue if date is in past week or future
            if check_date(date_obj):
                
                yield {
                    'category': category,
                    'date': date,
                    'title': item.css('[class="event-preview"] ::text').get(),
                    'url': item.css('[class="event-preview"] a::attr(href)').get(),
                    'summary': None
                     
                }
        







# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider hgop_foreign_spider.py -O output/h_gop_foreign_" + date + ".csv"
cmdline.execute(execute.split())