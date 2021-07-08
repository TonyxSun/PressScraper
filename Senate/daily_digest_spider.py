import scrapy
import os
from datetime import date
from scrapy import cmdline

# Program to crawl Congress "Action on Legislation" page and extract the daily digest.


class DailyDigestSpider(scrapy.Spider):
    name = "digest"

    def start_requests(self):
        yield scrapy.Request(url='https://www.congress.gov/bills-with-chamber-action/browse-by-date', callback=self.parse)

    def parse(self, response):
        """
        Finds the ten most recent daily digests, and crawls to each page.
        """

        # Counts number of entries parsed, ends at 10
        count = 0

        # Iterates through each entry/date
        for day in response.css('[class="tablesorter-infoOnly"]'):

            count += 1

            if count == 10:
                break

            # Obtains url and date
            url = response.urljoin(
                day.css("td[rowspan='3'] a::attr(href)").get())
            date = day.css("td[rowspan='3'] ::text").get()

            # Crawls each link with the daily digest
            yield scrapy.Request(url, callback=self.get_digest, meta={'date': date, 'url': url})

    def get_digest(self, response):
        """
        Extracts text for each daily digest.

        """

        # Obtains date and url information from before
        date = response.meta["date"]
        url = response.meta['url']

        """
        text = response.css("[id='daily-digest-content'] ::text").getall()
        
        content = '"'
        
        for part in text:
            content = content + part
        
        content = content + '"'
        """

        # prodcues output with date, url, and text fpr the given date
        yield {
            'date': date,
            'url': url,
            # 'content': content
        }


# Creates file with date and writes content to the file
# os.system("touch digest_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
# execute = "scrapy crawl digest -O digest_" + date + ".csv"
execute = "scrapy runspider daily_digest_spider.py -O output/digest_" + date + ".csv"

cmdline.execute(execute.split())
