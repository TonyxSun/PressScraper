import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

# Program to crawl the FCC Headlines webpage, and extract information about recent headlines.


class FCCSpider(scrapy.Spider):
    name = "fcc"

    def start_requests(self):
        yield scrapy.Request(url='https://www.fcc.gov/news-events/headlines', callback=self.parse)

    def parse(self, response):
        
        
        def getPastDays():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: July 6, 2021
            """
            today = d.today().strftime("%B %-d, %Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%B %-d, %Y")
            
            return [today, yesterday]
        

        # Helper function to identify date, as when extracted, the date is followed by unrecognized characters
        def fix_date(date):
            new = ""

            # Iterate through letter until '-' is reached (end of date)
            for letter in date:
                if letter == "-":
                    # Strip remaining unneeded characters
                    return new[:len(new)-1]
                new = new + letter
        
        # Obtains today and yesterday as a string
        past_dates = getPastDays()
        
        # Using regex, recognize headlines as those with a class that begin with "views-row"
        for headline in response.css('[class^="views-row"]'):
            
            date = fix_date(headline.css("span.released-date::text").get())
            
            # Only continues if date is today or yesterday
            if date in past_dates:
                # Extract the following information
                yield {
                    'date': date,
                    'url': response.urljoin(headline.css("h3.block__title a::attr(href)").get()),
                    'title': headline.css("h3.block__title ::text").get(),
                }


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider fcc_spider.py -O output/fcc_" + date + ".csv"
cmdline.execute(execute.split())
