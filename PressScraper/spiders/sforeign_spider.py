import scrapy
import os
from datetime import date
from scrapy import cmdline

# Program to crawl the Senate Foreign "Activities and Reports" section.

class SenateForeignSpider(scrapy.Spider):
    name = "sforeign"
    
    # Begin crawling!
    def start_requests(self):
        yield scrapy.Request(url='https://www.foreign.senate.gov/activities-and-reports', callback=self.parse)

    
    def parse(self, response):
        """
        Crawls to each type of news / report given

        """
        
        # Collects all urls for type of news/report
        urls = response.css('[id="sam-main"] a::attr(href)').getall()
        
        # Iterates through urls
        for i in range(len(urls)):
            url = urls[i]
            
            # Obtains category name
            selector = "[href='" + url + "']::text"
            category = response.css(selector).get()
            
            # Joins url with beginning part ig nrrfrf
            if url == "/nominations":
                url = response.urljoin(url)
            
            # Skips unnecessary parts
            if url == "https://www.congress.gov//" or category == None:
                continue
            
            yield scrapy.Request(url, callback=self.get_news, meta={'category':category})
        
        
    def get_news(self, response):
        """

        Obtains latest headlines.

        """
        
        # Recover category type found previously
        category = response.meta["category"]
                
        # NOMINATIONS
        for headline in response.css('[class="panel-title"]'):
            
            yield {
                'category' : category,
                'date': headline.css('[class="pull-left date"]::text').get(),
                'url': None,
                'content' : headline.css('[class="title pull-right"]::text').get()
             }
        
        # TREATIES, LEGISLATION
        # Obtain urls and dates
        urls = response.css('[class="bill-title"] a::attr(href)').getall()
        dates = response.css('[class="date"] *::text').getall()
        i = -1
        
        # Iterates through headlines and uses i to iterate through urls/dates
        for headline in response.css('[class="bill-title"]'):
            i += 1

            yield {
                'category': category,
                'date': dates[i],
                'url': urls[i],
                'content' : headline.css('[target="_blank"]::text').get()
            }
        
        # BUSINESS MEETINGS TRANSCRIPTS, COMMITTEE REPORTS, HEARING TRANSCRIPTS, COMMITTEE PRINTS
        
        # No Conference Reports on the webpage, and did not obtain Other
        
        # Obtain following parts
        dates = response.css('[class="date"] *::text').getall()
        titles = response.css('[class="acrobat"] *::text').getall()
        urls = response.css('[class="acrobat"] a::attr(href)').getall()
        
        # Skips empty pagges
        if len(titles) == 0:
            return
        
        # Iterates through dates, titles, and urls
        for i in range(len(dates)):
            
            # Skips unnecessary part
            if titles[i] == "acrobat":
                continue
            
            yield {
                'category': category,
                'date': dates[i],
                'url': response.urljoin(urls[i]),
                'content' : titles[i]
            }
            

# Creates file with date and writes content to the file
os.system("touch sforeign_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
execute = "scrapy crawl sforeign -O sforeign_" + date + ".csv"
cmdline.execute(execute.split())












