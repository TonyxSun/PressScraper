import scrapy
import os
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date


# Program to crawl Congress "Action on Legislation" page and extract the daily digest.


class DailyDigestSpider(scrapy.Spider):
    name = "digest"

    def start_requests(self):
        yield scrapy.Request(url='https://www.congress.gov/bills-with-chamber-action/browse-by-date', callback=self.parse)

    def parse(self, response):
        """
        Finds recent daily digests, and crawls to each page.
        """
        
        # Iterates through each entry/date
        for day in response.css('[class="tablesorter-infoOnly"]'):

            # Obtains url and date
            url = response.urljoin(
                day.css("td[rowspan='3'] a::attr(href)").get())
            date = day.css("td[rowspan='3'] ::text").get()
            
            # Obtain date as object
            date_obj = datetime.strptime(date, "%m/%d/%Y").date()

            # Only continues if date is today or yesterday
            if check_date(date_obj):

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
date = datetime.today().strftime("%m.%d.%y")
# execute = "scrapy crawl digest -O digest_" + date + ".csv"
execute = "scrapy runspider daily_digest_spider.py -O output/digest_" + date + ".csv"

cmdline.execute(execute.split())
