import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date


# Program to crawl the Senate Commerce news webpage, and extract information about recent headlines.


class SenateCommerceSpider(scrapy.Spider):
    name = "scommerce"

    def start_requests(self):
        urls = ["https://www.commerce.senate.gov/pressreleases",
                "https://www.commerce.senate.gov/hearings",
                "https://www.commerce.senate.gov/markups"]
        
        categories = ["Press Release", "Hearings", "Markups"]
        
        for i in range(len(urls)):
            
            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        # Recover category type found previously
        category = response.meta["category"]
        
        # Get all URLS
        urls = response.css('[class^="element odd"] a::attr(href),[class^="element even"] a::attr(href)').getall()
        
        # To iterate through urls
        i = -1

            
        # Iterate through each press release / hearing / markup
        for release in response.css('[class^="element odd"],[class^="element even"]'):
            
            i += 1
            
            # Obtain date and only continue if date was in past_dates
            date = release.css('[class="element-datetime"] ::text').get()
            
            date_obj = datetime.strptime(date, "%m/%d/%Y").date()
            
            if check_date(date_obj):
            
                yield {
                    'category': category,
                    'date': release.css('[class="element-datetime"] ::text').get(),
                    'title': release.css('[class="element-title"] ::text').get(),
                    'url': urls[i],
                    'summary': release.css('[class="element-abstract"] ::text').get()
                    
                }
        
        

# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider scommerce_spider.py -O output/scommerce_" + date + ".csv"
cmdline.execute(execute.split())
