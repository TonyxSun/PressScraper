import scrapy
import datetime
from datetime import timedelta
from scrapy import cmdline

# Program to crawl the HOUSE Energy and Commerce news webpage, and extract information about recent headlines.


class HouseCommerceSpider(scrapy.Spider):
    name = "science, space, and tech"

    def start_requests(self):
        urls = ["https://science.house.gov/news/press-releases", "https://science.house.gov/hearings", "https://science.house.gov/markups"
                ]

        categories = ["News", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        def get_past_days():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.

            Format: July 15, 2021
            """
            today = datetime.datetime.now().strftime("%B %d, %Y")
            yesterday = (datetime.datetime.now() -
                         timedelta(1)).strftime("%B %d, %Y")

            return [today, yesterday]

        def same_week(dateString):
            '''returns true if a dateString in %B %d, %Y fo rmat is part of the current week'''
            d1 = datetime.datetime.strptime(dateString, '%B %d, %Y')
            d2 = datetime.datetime.today()
            return (d1.isocalendar()[1] == d2.isocalendar()[1] or d1.isocalendar()[1] == d2.isocalendar()[1]-1) and d1.year == d2.year

        # Obtains today and yesterday as a string
        past_dates = get_past_days()

        # Recover category type found previously
        category = response.meta["category"]

        # scrape for news
        if category == "News":
            # Get all items
            urls = response.css(
                '[class^="media__title"]>a::attr(href)').getall()
            dates = response.css('[class^="media__date"]::text').getall()
            titles = response.css('[class^="media__title"] a::text').getall()
            summaries = response.css('p.media__summary::text').getall()
            for i in range(len(dates)):
                dates[i] = dates[i].strip("\t\n ")
                titles[i] = titles[i].strip("\t\n ")
            for i in range(len(summaries)):
                summaries[i] = summaries[i].replace('\n', '')
                summaries[i] = summaries[i].replace('\t', '')

            # Iterate through each press release
            for i in range(len(urls)):
                if same_week(dates[i]) or dates[i] in past_dates:
                    # if date in past_dates_1:
                    yield {
                        'category': category,
                        'date': dates[i],
                        'title': titles[i],
                        'url': response.urljoin(urls[i]),
                        'summary': summaries[i].strip("\t\n")
                    }

        # scrape for markups and hearings
        if category == "Markups" or "Hearings":
            # Get all items
            for release in response.css('[class="hearing"]'):
                date = release.css('p.hearing__date::text').get()
                date = date.strip("\t\n ")
                # Iterate through each press release
                if same_week(date) or date in past_dates:
                    # if date in past_dates_1:
                    yield {
                        'category': category,
                        'date': date,
                        'title': release.css('h3.hearing__title::text').get(),
                        'url': response.urljoin(release.css('a::attr(href)').get()),
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.datetime.now().strftime("%m.%d.%y")
execute = "scrapy runspider h_science_spider.py -O output/h_science_" + date + ".csv"
cmdline.execute(execute.split())
