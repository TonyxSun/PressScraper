import scrapy
import os
from datetime import date
from scrapy import cmdline

# Program to crawl the Senate Commerce news webpage, and extract information about recent headlines.


class SenateCommerceSpider(scrapy.Spider):
    name = "scommerce"

    def start_requests(self):
        yield scrapy.Request(url='https://www.commerce.senate.gov/news', callback=self.parse)

    def parse(self, response):

        # Iterate through headlines on the page
        for headline in response.css('[class="even"], [class^="odd"]'):

            # Extract the following information
            yield {
                'date': headline.css("[class='element-date']::text").get(),
                'title': headline.css("h1[class='element-title'] *::text").get(),
                'url': response.urljoin(headline.css("h1.element-title a::attr(href)").get()),
                'text': headline.css("[class='element-content'] *::text").getall()
            }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
execute = "scrapy runspider sen_commerce_spider.py -O scommerce_" + date + ".csv"
cmdline.execute(execute.split())
