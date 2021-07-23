import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline

# Program to crawl the HOUSE Science news webpage, and extract information about recent headlines.


class HouseScienceSpider(scrapy.Spider):
    name = "science, space, and tech"

    def start_requests(self):
        urls = ["https://science.house.gov/news/press-releases", "https://science.house.gov/hearings", "https://science.house.gov/markups"
                ]

        categories = ["News", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):
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
                date_obj = datetime.strptime(dates[i], "%B %d, %Y").date()

                if check_date(date_obj):
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
                date_obj = datetime.strptime(date, "%B %d, %Y").date()

                if check_date(date_obj):
                    # if date in past_dates_1:
                    yield {
                        'category': category,
                        'date': date,
                        'title': release.css('h3.hearing__title::text').get(),
                        'url': response.urljoin(release.css('a::attr(href)').get()),
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_science_spider.py -O output/h_science_" + date + ".csv"
cmdline.execute(execute.split())
