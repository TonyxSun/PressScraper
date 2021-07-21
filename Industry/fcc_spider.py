import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date

# Program to crawl the FCC Headlines webpage, and extract information about recent headlines.


class FCCSpider(scrapy.Spider):
    name = "fcc"

    def start_requests(self):
        yield scrapy.Request(url='https://www.fcc.gov/news-events/headlines', callback=self.parse)

    def parse(self, response):
        

        # Helper function to identify date, as when extracted, the date is followed by unrecognized characters
        def fix_date(date):
            new = ""

            # Iterate through letter until '-' is reached (end of date)
            for letter in date:
                if letter == "-":
                    # Strip remaining unneeded characters
                    return new[:len(new)-1]
                new = new + letter

        
        # Using regex, recognize headlines as those with a class that begin with "views-row"
        for headline in response.css('[class^="views-row"]'):
            
            date = fix_date(headline.css("span.released-date::text").get())
            
            # Obtain date as object
            date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            # Only continues if date is today or yesterday
            if check_date(date_obj):
                # Extract the following information
                yield {
                    'date': date,
                    'url': response.urljoin(headline.css("h3.block__title a::attr(href)").get()),
                    'title': headline.css("h3.block__title ::text").get(),
                }


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider fcc_spider.py -O output/fcc_" + date + ".csv"
cmdline.execute(execute.split())
