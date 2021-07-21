import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date


class FloorSpider(scrapy.Spider):
    name = "floor"

    # Begin crawling!
    def start_requests(self):
        yield scrapy.Request(url='https://floor.senate.gov/proceedings', callback=self.parse)

    def parse(self, response):
        """
        Recent entries of senate floor proceedings, and crawls to their respective urls.

        """
        # Counts number of entries crawled
        first = True

        # Finds all entries, which have a class name of either "even" or "odd"
        for day in response.css('[class="even"], [class="odd"]'):


            # Skips first iteration (not an entry)
            if first:
                first = False
                continue

            # Identifies url and date of each entry
            url = response.urljoin(
                day.css("td[headers='Summary Senate-Floor-Proceedings'] a::attr(href)").get())
            date = day.css(
                "[headers='Date Senate-Floor-Proceedings']::text").get()

            # Skips if date is None
            if date == None:
                continue
            
            # Obtain date as object
            date_obj = datetime.strptime(date, "%a, %b %d, %Y").date()
            
            # Only continues if date is today or yesterday
            if check_date(date_obj):
                

                # Crawls to obtain summary of the entry by following the url found
                yield scrapy.Request(url, callback=self.get_summary, meta={'date': date, 'url': url})

    def get_summary(self, response):
        """

        Obtains summary of given entry.

        """

        # Recover date found previously
        date = response.meta["date"]
        url = response.meta["url"]

        # Possible css selectors
        selectors = '[style^="padding-b"]::text, [class="headings"]::text, [class="docnum"]::text, [class="status"]::text, div.docnum ::text'

        # List will contain all text
        all_text_list = response.css(selectors).extract()

        # Creates string of all text, removing unnecessary blank lines and characters
        all_text = ""
        for text in all_text_list:
            if text != "\n":
                new_text = ""
                for char in text:
                    if char == "\n" or char == ":":
                        continue
                    new_text = new_text + char
                all_text = all_text + new_text + "\n"
        # Produce output with date and content
        yield {
            'date': date,
            'url': url,
            'content': all_text
        }


# Creates file with date and writes content to the file
# os.system("touch floor_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider senate_floor_spider.py -O output/floor_" + date + ".csv"
cmdline.execute(execute.split())
