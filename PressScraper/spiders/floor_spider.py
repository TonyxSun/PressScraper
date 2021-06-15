import scrapy
import os
from datetime import date
from scrapy import cmdline


class FloorSpider(scrapy.Spider):
    name = "floor"
    
    # Begin crawling!
    def start_requests(self):
        yield scrapy.Request(url='https://floor.senate.gov/proceedings', callback=self.parse)

    

    def parse(self, response):
        """

        Identifies 10 newest entries of senate floor proceedings, and crawls to
        their respective urls.

        """
        
        # Counts number of entries crawled
        count = 0
        
        # Finds all entries, which have a class name of either "even" or "odd"
        for day in response.css('[class="even"], [class="odd"]'):
            
                        
            # Increases count for each iteration
            count += 1
        
            # Stops once a few entries have been crawled. Otherwise,
            # would crawl to all entries dating back to 2012.
            if count == 13:
                break
            
            # Skips first iteration (not an entry)
            if count == 1:
                continue

            # Identifies url and date of each entry
            url = response.urljoin(day.css("td[headers='Summary Senate-Floor-Proceedings'] a::attr(href)").get())
            date = day.css("[headers='Date Senate-Floor-Proceedings']::text").get()
            
            """
            
            # Extract the following information
            yield {
                'date' : day.css("[headers='Date Senate-Floor-Proceedings']::text").get(),
                'url': response.urljoin(day.css("td[headers='Summary Senate-Floor-Proceedings'] a::attr(href)").get())
            }
            
            """
            
            # Crawls to obtain summary of the entry by following the url found
            yield scrapy.Request(url, callback=self.get_summary, meta={'date': date})
        
        
    def get_summary(self, response):
        """

        Obtains summary of given entry.

        """
        
        # Recover date found previously
        date = response.meta["date"]
        
        # List will all text
        # MISSING TEXT THAT IS IN SUBCLASSES
        all_text_list = response.css('[style="padding-bottom:20px"]::text').extract()
        
        # Creates string of all text, removing unnecessary blank lines
        all_text = ""
        for text in all_text_list:
            if text != "\n":
                all_text = all_text + text + "\n"
                
        
        # Produce output with date and content
        yield {
            'date': date,
            'content' : all_text  
         }
            

# Creates file with date and writes content to the file
os.system("touch floor_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
execute = "scrapy crawl floor -O floor_" + date + ".csv"
cmdline.execute(execute.split())











