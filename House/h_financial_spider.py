import scrapy
import datetime
from datetime import timedelta
from scrapy import cmdline

# Program to crawl the HOUSE Energy and Commerce news webpage, and extract information about recent headlines.


class HouseCommerceSpider(scrapy.Spider):
    name = "financialservices"

    def start_requests(self):
        urls = ["https://financialservices.house.gov/news/", "https://financialservices.house.gov/calendar/?EventTypeID=577&Congress=117", "https://financialservices.house.gov/calendar/?EventTypeID=575&Congress=117"
                ]

        categories = ["Press Release", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        def get_past_days_1():
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
            return d1.isocalendar()[1] == d2.isocalendar()[1] and d1.year == d2.year

        # Obtains today and yesterday as a string
        past_dates_1 = get_past_days_1()

        # Recover category type found previously
        category = response.meta["category"]

        # Get all URLS
        urls = response.css(
            '[class^="newsie-titler"]>a::attr(href)').getall()

        # To iterate through urls
        i = -1

        # Iterate through each press release
        if category == "Press Release":
            for release in response.css('[class^="newsblocker"]'):
                i += 1

                # Obtain date and only continue if date was in past_dates
                date = release.css('time::text').get()
                # clean date format

                if same_week(date) or date in past_dates_1:
                    # if date in past_dates_1:
                    yield {
                        'category': category,
                        'date': date,
                        'title': release.css('h2.newsie-titler a::text').get(),
                        'url': response.urljoin(urls[i]),
                        'summary': release.css('div.newsbody>p::text').get()
                    }

        # interate through hearings
        if category == "Hearings" or "Markups":
            # for release in response.css('[class^="future"],[class^="past"]'):
            # i += 1

            # Obtain date and only continue if date was in past_dates
            date = response.xpath(
                '//div[@class="newsie-details"]/text()[following-sibling::span[1]]').getall()
            # date = dates[2]
            for i in range(len(date)):
                date[i] = date[i].strip("\r\n |")
            date = list(filter(None, date))
            title = response.css('li>h3.newsie-titler a::text').getall()
            summary = response.css('li>h4::text').getall()
            print(title)
            # clean date format
            # print("date is " + date + ".")
            print(date)
            for i in range(len(date)):
                if date[i] in past_dates_1:
                    yield {
                        'category': category,
                        'date': date[i],
                        'title': title[i],
                        'url': response.urljoin(urls[i]),
                        'summary': summary[i]
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.datetime.now().strftime("%m.%d.%y")
execute = "scrapy runspider h_financial_spider.py -O output/h_financial_" + date + ".csv"
cmdline.execute(execute.split())
