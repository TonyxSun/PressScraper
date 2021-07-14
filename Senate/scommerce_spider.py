import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

# Program to crawl the Senate Commerce news webpage, and extract information about recent headlines.


class SenateCommerceSpider(scrapy.Spider):
    name = "scommerce"

    def start_requests(self):
        yield scrapy.Request(url='https://www.commerce.senate.gov/news', callback=self.parse)

    def parse(self, response):
        
        def getPastDays():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: July 13, 2021
            """
            today = d.today().strftime("%B %-d, %Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%B %-d, %Y")
            
            return [today, yesterday]
        
        # Obtains today and yesterday as a string
        past_dates = getPastDays()
        
        # Iterate through headlines on the page
        for headline in response.css('[class="even"], [class^="odd"]'):
            
            date = headline.css("[class='element-date']::text").get()
            
            # Only continues if date is today or yesterday
            if date in past_dates:

                # Extract the following information
                yield {
                    'date': date,
                    'title': headline.css("h1[class='element-title'] *::text").get(),
                    'url': response.urljoin(headline.css("h1.element-title a::attr(href)").get()),
                    'text': headline.css("[class='element-content'] *::text").getall()
                }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider scommerce_spider.py -O output/scommerce_" + date + ".csv"
cmdline.execute(execute.split())
