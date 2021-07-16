import scrapy
from datetime import date as d
from datetime import timedelta
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

        def getPastDays():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.

            Format: 07/13/21
            """
            today = d.today().strftime("%m/%d/%y")
            yesterday = (d.today()-timedelta(1)).strftime("%m/%d/%y")

            return [today, yesterday]

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
        print(len(urls))

        # Will store css selectors to obtain title of headlines
        title_selectors = []
        # Strips unneeded characters from the urls and obtains css selector to obtain the title
        for i in range(len(urls)):
            urls[i] = urls[i].strip("\n\t")
            title_selectors.append("[href~='" + urls[i] + "']::text")
        print(len(urls))

        # Obtains today and yesterday as a string
        past_dates = getPastDays()

        # Iterates through dates, urls, and titles
        for i in range(len(dates)):

            if dates[i] in past_dates:

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
                if date in past_dates:
                    yield{
                        'category': category,
                        'date': date,
                        'url': response.urljoin(hearing.css('div.faux-col a::attr(href)').get()),
                        'title': title.strip()
                    }


# Creates file with date and writes content to the file
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider sjudiciary_spider.py -O output/sjudiciary" + date + ".csv"
cmdline.execute(execute.split())
