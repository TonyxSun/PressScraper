import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class HouseHomelandSpider(scrapy.Spider):
    name = "hhomeland"
    
    def start_requests(self):
        
        urls = ['https://homeland.house.gov/news/press-releases/table/',
                'https://homeland.house.gov/activities/hearings',
                'https://homeland.house.gov/activities/markups']
        
        categories = ["Press Release", "Hearing", "Markup"]
        
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': categories[i]})
            
            
        
    def parse(self, response):
        
        
        # Obtain category passed through meta
        category = response.meta["category"]


        # MARKUPS and HEARINGS
        for entry in response.css('[class="vevent"]'):
            
            # Obtain URL
            url = entry.css('[class="faux-col"] a::attr(href)').get()
            
            # Use URL as css selector for the title
            title_selector = '[href="' + url + '"]::text'
            
            # Get date
            date = entry.css('[class="dtstart"] ::text').get()
            
            # Obtain date as object
            date_obj = datetime.strptime(date, "%b %d %Y").date()
            
            if check_date(date_obj):
                
                yield {
                    'category': category,
                    'date': date,
                    'title': entry.css(title_selector).get().strip("\n\t"),
                    'url': response.urljoin(url)  
                }
        
        
        # PRESS RELEASES
        all_dates = response.css('[class="date"] ::text').getall()
        urls = response.css('[class="table"] a::attr(href)').getall()

        # Obtain only actual dates
        dates = []
        for date in all_dates:
            if "\t" not in date:
                dates.append(date)
        
                
        # To store CSS selectors to obtain the title
        title_selectors = []
        
        # Create and add selectors to title_selectors
        for url in urls:
            selector = "[href='" + url + "'] ::text"
            title_selectors.append(selector)
        
        # Iterating through indexes
        for i in range(len(dates)):
            
            
            # Obtain date as object
            date_obj = datetime.strptime(dates[i], "%m/%d/%y").date()
            
            # Continue is date is yesterday or today
            if check_date(date_obj):
                
                yield {
                    'category': category,
                    'date': dates[i],
                    'title': response.css(title_selectors[i]).get().strip('\t\n'),
                    'url': urls[i]
                }
            
            
        
        
        



# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_homeland_spider.py -O output/h_homeland_" + date + ".csv"
cmdline.execute(execute.split())   
        