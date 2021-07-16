import scrapy
import datetime
from datetime import timedelta
from scrapy import cmdline

# Program to crawl the HOUSE Energy and Commerce news webpage, and extract information about recent headlines.


class HouseCommerceSpider(scrapy.Spider):
    name = "henergy"

    def start_requests(self):
        urls = ["https://energycommerce.house.gov/newsroom/press-releases", "https://energycommerce.house.gov/committee-activity/hearings", "https://energycommerce.house.gov/committee-activity/markups"
                ]

        categories = ["Press Release", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        def get_past_days_1():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.

            Format: Jul 15, 2021
            """
            today = datetime.datetime.now().strftime("%b %d, %Y")
            yesterday = (datetime.datetime.now() -
                         timedelta(1)).strftime("%b %d, %Y")

            return [today, yesterday]

        def get_past_days_2():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.

            Format: 07/13/2021
            """
            today = datetime.datetime.now().strftime("%m/%d/%Y")
            yesterday = (datetime.datetime.now() -
                         timedelta(1)).strftime("%m/%d/%Y")
            daybefore = (datetime.datetime.now() -
                         timedelta(2)).strftime("%m/%d/%Y")

            return [today, yesterday, daybefore]
        # Obtains today and yesterday as a string
        past_dates_1 = get_past_days_1()
        past_dates_2 = get_past_days_2()

        # Recover category type found previously
        category = response.meta["category"]

        # Get all URLS
        urls = response.css(
            '[class^="views-row"]>div.views-field-title>h3>a::attr(href)').getall()

        # To iterate through urls
        i = -1

        # Iterate through each press release
        if category == "Press Release":
            for release in response.css('[class^="views-row"]'):
                i += 1

                # Obtain date and only continue if date was in past_dates
                date = release.css('span.views-field-created>span::text').get()
                # clean date format
                new_date = ""
                if len(date) == 11:
                    new_date = date[0:4] + "0" + date[4:]
                else:
                    new_date = date
                if new_date in past_dates_1:
                    yield {
                        'category': category,
                        'date': new_date,
                        'title': release.css('h3.field-content a::text').get(),
                        'url': response.urljoin(urls[i]),
                        'summary': release.css('div.views-field-body>div::text').get()
                    }

        # interate through hearings
        if category == "Hearings" or "Markups":
            for release in response.css('[class^="views-row"]'):
                i += 1

                # Obtain date and only continue if date was in past_dates
                date = release.css(
                    'div.views-field-field-congress-meeting-date span::text').get()
                # clean date format
                new_date = ""
                new_date = date[5:15]
                if new_date in past_dates_2:
                    yield {
                        'category': category,
                        'date': new_date,
                        'title': release.css('h3.field-content a::text').get(),
                        'url': response.urljoin(urls[i]),
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.datetime.now().strftime("%m.%d.%y")
execute = "scrapy runspider h_energy_spider.py -O output/h_energy_" + date + ".csv"
cmdline.execute(execute.split())
