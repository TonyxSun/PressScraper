import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date

# Program to crawl the FSenate Banking Committee Press Releases webpage, and extract information about recent headlines.


class SenateBankingSpider(scrapy.Spider):
    name = "sbanking"

    def start_requests(self):

        # Urls for minority and majority press releases
        urls = ["https://www.banking.senate.gov/newsroom/majority-press-releases",
                "https://www.banking.senate.gov/newsroom/minority-press-releases",
                "https://www.banking.senate.gov/hearings",
                "https://www.banking.senate.gov/markups"]

        # Corresponding category information
        category = ["Majority Press Release", "Minority Press Release", "Hearings", "Markups"]

        # Go into each webpage
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': category[i]})

    def parse(self, response):
        
        def get_date_only(date):
            """
            Obtains only date given date + time
            """
            
            return date[0:8]

        # Obtain category passed through meta
        category = response.meta["category"]
        

        # PRESS RELEAQSES
        # Obtain all text under date class
        temp_dates = response.css("[class='date'] ::text").getall()
        
        # Will contain all actual dates
        dates = []
        
        # Adds actual dates to dates list
        for date in temp_dates:
            if "/" in date:
                dates.append(date)

        # Obtain all urls for headlines
        urls = response.css('[class="table"] a::attr(href)').getall()
        # Will store css selectors to obtain title of headlines
        title_selectors = []
        # Strips unneeded characters from the urls and obtains css selector to obtain the title
        for i in range(len(urls)):
            urls[i] = urls[i].strip("\n\t")
            title_selectors.append("[href~='" + urls[i] + "']::text")

        
        # Iterates through dates, urls, and titles
        for i in range(len(dates)):
            
            date_obj = datetime.strptime(dates[i], "%m/%d/%y").date()
            # Only continues if date is today or yesterday
            if check_date(date_obj):
                # Extract the following information
                yield {
                    'category': category,
                    'date': dates[i],
                    'url': urls[i],
                    'title': response.css(title_selectors[i]).get().strip("\n\t")
                }
                
                
    
        # MARKUP and HEARINGS
        for item in response.css('[class="vevent"]'):
    
            date = get_date_only(item.css('[class="dtstart"]::text').get())
            
            date_obj = datetime.strptime(date, "%m/%d/%y").date()
            
            
            if check_date(date_obj):
                title_list = item.css('[class="url summary pull-left"]::text').getall()
                title = ""
                
                for part in title_list:
                    title = title + part.strip("\n\t")
                    
                print ()
                
                yield {
                    'category': category,
                    'date': date,
                    'url': response.urljoin(item.css('[class="faux-col"] a::attr(href)').get()),
                    'title': title
                }


# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider sbanking_spider.py -O output/sbanking_" + date + ".csv"
cmdline.execute(execute.split())
