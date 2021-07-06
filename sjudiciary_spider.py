import scrapy
from datetime import date
from scrapy import cmdline

# Program to crawl the FSenate Banking Committee Press Releases webpage, and extract information about recent headlines.


class SenateBankingSpider(scrapy.Spider):
    name = "sjudiciary"

    def start_requests(self):

        # Urls for minority and majority press releases
        urls = ["https://www.judiciary.senate.gov/press/majority",
                "https://www.judiciary.senate.gov/press/minority-press"]

        # Corresponding category information
        category = ["majority", "minority"]

        # Go into majority and minority webpages
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': category[i]})

    def parse(self, response):

        # Obtain category passed through meta
        category = response.meta["category"]

        # Obtain all text under date class
        temp_dates = response.css("[class='date'] ::text").getall()

        # Will contain all actual dates
        dates = []
        # Adds actual dates to dates list
        for date in temp_dates:
            if "/" in date:
                dates.append(date)

        # Obtain all urls for headlines
        urls = response.css('[class="table"] a::attr(href)').getall()
        print(len(urls))

        # Will store css selectors to obtain title of headlines
        title_selectors = []
        # Strips unneeded characters from the urls and obtains css selector to obtain the title
        for i in range(len(urls)):
            urls[i] = urls[i].strip("\n\t")
            title_selectors.append("[href~='" + urls[i] + "']::text")
        print(len(urls))
        # Iterates through dates, urls, and titles
        for i in range(len(dates)):

            # Extract the following information
            yield {
                'category': category,
                'date': dates[i],
                'url': urls[i],
                'title': response.css(title_selectors[i]).get().strip()
            }


# Creates file with date and writes content to the file
date = date.today().strftime("%m.%d.%y")
execute = "scrapy runspider sjudiciary_spider.py -O output/sjudiciary" + date + ".csv"
cmdline.execute(execute.split())
