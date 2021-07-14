import scrapy
import os
from datetime import date as d
from datetime import timedelta
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
        
        def getPastDays():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 07/13/2021
            """
            today = d.today().strftime("%m/%d/%Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%Y")
            
            return [today, yesterday]

        # Counts number of entries parsed, ends at 10
        count = 0
        
        # Obtains today and yesterday as a string
        past_dates = getPastDays()

        # Iterates through each entry/date
        for day in response.css('[class="tablesorter-infoOnly"]'):

            count += 1

            if count == 10:
                break

            # Obtains url and date
            url = response.urljoin(
                day.css("td[rowspan='3'] a::attr(href)").get())
            date = day.css("td[rowspan='3'] ::text").get()

            # Only continues if date is today or yesterday
            if date in past_dates:

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
date = d.today().strftime("%m.%d.%y")
# execute = "scrapy crawl digest -O digest_" + date + ".csv"
execute = "scrapy runspider daily_digest_spider.py -O output/digest_" + date + ".csv"

cmdline.execute(execute.split())
