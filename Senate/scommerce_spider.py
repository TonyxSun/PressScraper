import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

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
        
        def get_past_days():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 07/22/21
            """
            today = d.today().strftime("%m/%d/%Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%Y")
            
            return [today, yesterday]
        
        
        # Obtains today and yesterday as a string
        past_dates = get_past_days()
        
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
            
            if date in past_dates:
            
                yield {
                    'category': category,
                    'date': release.css('[class="element-datetime"] ::text').get(),
                    'title': release.css('[class="element-title"] ::text').get(),
                    'url': urls[i],
                    'summary': release.css('[class="element-abstract"] ::text').get()
                    
                }
        
        

# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider scommerce_spider.py -O output/scommerce_" + date + ".csv"
cmdline.execute(execute.split())
