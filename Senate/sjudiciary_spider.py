import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline

# Program to crawl the FSenate Banking Committee Press Releases webpage, and extract information about recent headlines.


class SenateBankingSpider(scrapy.Spider):
    name = "sjudiciary"

    def start_requests(self):

        # Urls for minority and majority press releases
        urls = ["https://www.judiciary.senate.gov/press/majority",
                "https://www.judiciary.senate.gov/press/minority-press", "https://www.judiciary.senate.gov/hearings"]

        # Corresponding category information
        category = ["majority", "minority", "hearings"]

        # Go into majority and minority webpages
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': category[i]})

    def parse(self, response):

        # Obtain category passed through meta
        category = response.meta["category"]

        # NEWS RELEASES

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


        # Will store css selectors to obtain title of headlines
        title_selectors = []
        # Strips unneeded characters from the urls and obtains css selector to obtain the title
        for i in range(len(urls)):
            urls[i] = urls[i].strip("\n\t")
            title_selectors.append("[href~='" + urls[i] + "']::text")


        # Iterates through dates, urls, and titles
        for i in range(len(dates)):
            date_obj = datetime.strptime(dates[i], "%m/%d/%y").date()
            if check_date(date_obj):

                # Extract the following information
                # Only continues if date is today or yesterday
                yield {
                    'category': category,
                    'date': dates[i],
                    'url': urls[i],
                    'title': response.css(title_selectors[i]).get().strip()
                }

        # HEARINGS
        if category == "hearings":
            for hearing in response.css('tr.vevent'):
                date = hearing.css('time.dtstart::text').get()
                date = date[0:8]
                title = hearing.css('div.faux-col>a.url::text').get()
                date_obj = datetime.strptime(date, "%m/%d/%y").date()

                if check_date(date_obj):
                    yield{
                        'category': category,
                        'date': date,
                        'url': response.urljoin(hearing.css('div.faux-col a::attr(href)').get()),
                        'title': title.strip()
                    }


# Creates file with date and writes content to the file
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider sjudiciary_spider.py -O output/sjudiciary_" + date + ".csv"
cmdline.execute(execute.split())
