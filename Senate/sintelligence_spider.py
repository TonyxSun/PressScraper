import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date


# Program to crawl the Senate Commerce news webpage, and extract information about recent headlines.


class SenateIntelligenceSpider(scrapy.Spider):
    name = "sintelligence"

    def start_requests(self):
        urls = ["https://www.intelligence.senate.gov/press",
                "https://www.intelligence.senate.gov/hearings"]
        
        categories = ["Press Release", "Hearings"]
        
        for i in range(len(urls)):
            
            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        # Recover category type found previously
        category = response.meta["category"]

        # # Get all URLS
        # urls = response.css('[class^="views-row-title"] a::attr(href)').getall()
        
        # # To iterate through urls
        # i = -1

        # Iterate through each press release 
        if category == "Press Release":
            
            for release in response.css('[class^="views-row"]'):
                
                # Obtain date and only continue if date was in past_dates
                date = release.css('div.views-field-created > span::text').get()
                
                date_obj = datetime.strptime(date, "%m/%d/%Y").date()
                
                if check_date(date_obj):
                
                    yield {
                        'category': category,
                        'date': date,
                        'title': release.css('[class="views-field-title"] a::text').get(),
                        'url': response.urljoin(response.css('[class^="views-row-title"] a::attr(href)').get())
                    }

       # Iterate through each hearing
        if category == "Hearings":
            # print(len(urls))
            for release in response.css('[class^="views-row"]'):
                
                # Obtain date and only continue if date was in past_dates
                date = release.css('div.views-field-field-hearing-date  span::text').get()
                if len(date) > 10:
                    date = date[:10]
                date_obj = datetime.strptime(date, "%m/%d/%Y").date()
                
                if check_date(date_obj):
                
                    yield {
                        'category': category,
                        'date': date,
                        'title': release.css('div.views-field-title>span>a::text').get(),
                        'url': response.urljoin(response.css('[class^="views-row-title"] a::attr(href)').get()),
                        'video' : release.css('[class^="views-row-hearing-video"] a::attr(href)').get()
                    }
        
        

# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider sintelligence_spider.py -O output/sintelligence_" + date + ".csv"
cmdline.execute(execute.split())
