from scrapy import cmdline
import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date



# Program to crawl the HOUSE Energy and Commerce news webpage, and extract information about recent headlines.


class HouseCommerceSpider(scrapy.Spider):
    name = "transportation"

    def start_requests(self):
        urls = ["https://republicans-transportation.house.gov/news/documentquery.aspx?DocumentTypeID=2545", "https://republicans-transportation.house.gov/calendar/?EventTypeID=542", "https://republicans-transportation.house.gov/calendar/?EventTypeID=541", "https://transportation.house.gov/news/press-releases", "https://transportation.house.gov/committee-activity/hearings", "https://transportation.house.gov/committee-activity/markups"
                ]

        categories = ["Minority Press Releases",
                      "Minority Markups", "Minority Hearings", "Majority Press Releases",
                      "Majority Hearings", "Majority Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):

        # Recover category type found previously
        category = response.meta["category"]

        # Iterate through each PRESS RELEASE
        if category == "Majority Press Releases":
            # Get all URLS
            urls = response.css(
                '[class^="title"]>a::attr(href)').getall()
            titles = response.css('h2.title>a::text').getall()
            # Obtain date and only continue if date was in past_dates
            dates = response.css('span.date::text').getall()
            summaries = response.css('p.summary::text').getall()
            for i in range(len(summaries)):
                summaries[i] = summaries[i].strip("\r\n")
                summaries[i] = summaries[i].replace('\r\n', '')

            for i in range(len(dates)):
                date_obj = datetime.strptime(dates[i], "%B %d, %Y").date()
                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': dates[i],
                        'title': titles[i],
                        'url': response.urljoin(urls[i]),
                        'summary': summaries[i]
                    }

        # interate through hearings
        if category == "Majority Hearings" or "Majority Markups":
            for entry in response.css('[class="vevent"]'):

                # Obtain URL
                url = entry.css('[class="faux-col"] a::attr(href)').get()

                # Use URL as css selector for the title
                title_selector = '[href="' + url + '"]::text'

                # Get date
                date = entry.css('[class="dtstart"] ::text').get().rstrip(" ")
                if len(date) == 10:
                    date = date[:4] + "0" + date[4:]
                date_obj = datetime.strptime(date, "%b %d %Y").date()

                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': date,
                        'title': entry.css(title_selector).get().strip("\n\t"),
                        'url': response.urljoin(url)
                    }

        if category == "Minority Press Releases":
            dates = response.css('li::text').getall()
            for i in range(len(dates)):
                dates[i] = dates[i].strip("\r\n\t ,Tags:|")
                dates[i] = dates[i][28:]
            dates = list(filter(None, dates))
            titles = response.css("li>a.middleheadline::text").getall()
            for i in range(len(titles)):
                titles[i] = titles[i].strip("\r\n\t")
            urls = response.css('li>a.middleheadline::attr(href)').getall()
            for i in range(len(dates)):
                date_obj = datetime.strptime(dates[i], "%B %d, %Y").date()
                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': dates[i],
                        'title': titles[i],
                        'url': response.urljoin(urls[i]),
                    }
        if category == "Minority Hearings" or "Minority Markups":
            dates = response.xpath(
                '//b/text()[following-sibling::span[1]]').getall()
            for i in range(len(dates)):
                dates[i] = dates[i].replace("\r\n", "").strip()
            dates = list(filter(None, dates))
            titles = response.css("li>a.middleheadline>b::text").getall()
            for i in range(len(titles)):
                titles[i] = titles[i].strip("\r\n\t")
            urls = response.css('li>a.middleheadline::attr(href)').getall()
            for i in range(len(dates)):
                date_obj = datetime.strptime(dates[i], "%B %d, %Y").date()

                if check_date(date_obj):
                    yield {
                        'category': category,
                        'date': dates[i],
                        'title': titles[i],
                        'url': response.urljoin(urls[i]),
                    }


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_transportation_spider.py -O output/h_transportation_" + date + ".csv"
cmdline.execute(execute.split())
