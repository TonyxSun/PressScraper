import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

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
        category = ["Kajority Press Release", "Minority Press Release", "Hearings", "Markups"]

        # Go into majority and minority webpages
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': category[i]})

    def parse(self, response):
        
        def get_past_days():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 07/13/21
            """
            today = d.today().strftime("%m/%d/%y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%y")
            
            return [today, yesterday, "05/19/21"]
        
        def get_date_only(date):
            
            return date[0:8]

        # Obtain category passed through meta
        category = response.meta["category"]
        
        

        
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

        # Obtains today and yesterday as a string
        past_dates = get_past_days()
        
        # Iterates through dates, urls, and titles
        for i in range(len(dates)):
            
            # Only continues if date is today or yesterday
            if dates[i] in past_dates:
                # Extract the following information
                yield {
                    'category': category,
                    'date': dates[i],
                    'url': urls[i],
                    'title': response.css(title_selectors[i]).get().strip("\n\t")
                }
    
        # MARKUP
        for markup in response.css('[class="vevent"]'):
    
            date = get_date_only(markup.css('[class="dtstart"]::text').get())
            
            if date in past_dates:
                title_list = markup.css('[class="url summary pull-left"]::text').getall()
                title = ""
                
                for part in title_list:
                    title = title + part.strip("\n\t")
                    
                print ()
                
                yield {
                    'category': category,
                    'date': markup.css('[class="dtstart"]::text').get(),
                    'url': response.urljoin(markup.css('[class="faux-col"] a::attr(href)').get()),
                    'title': title
                }


# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider sbanking_spider.py -O output/sbanking_" + date + ".csv"
cmdline.execute(execute.split())
