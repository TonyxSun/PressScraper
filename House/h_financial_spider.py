import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
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
                date_obj = datetime.strptime(date, "%B %d, %Y").date()

                if check_date(date_obj):
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
                '//div[@class="newsie-details"]/text()[following-sibling::span[1]]').getall()  # this selector took me 2 hours ffs
            # clean list
            for i in range(len(date)):
                date[i] = date[i].strip("\r\n |")
            date = list(filter(None, date))
            title = response.css('li>h3.newsie-titler a::text').getall()
            summary = response.css('li>h4::text').getall()
            for i in range(len(date)):
                date_obj = datetime.strptime(date[i], "%B %d, %Y").date()

                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': date[i],
                        'title': title[i],
                        'url': response.urljoin(urls[i]),
                        'summary': summary[i]
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_financial_spider.py -O output/h_financial_" + date + ".csv"
cmdline.execute(execute.split())
