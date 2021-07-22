import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
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
                date_obj = datetime.strptime(new_date, "%b %d, %Y").date()

                if check_date(date_obj):
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
                date_obj = datetime.strptime(new_date, "%m/%d/%Y").date()

                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': new_date,
                        'title': release.css('h3.field-content a::text').get(),
                        'url': response.urljoin(urls[i]),
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_energy_spider.py -O output/h_energy_" + date + ".csv"
cmdline.execute(execute.split())
