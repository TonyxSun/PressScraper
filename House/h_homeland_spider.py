import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline


class HouseForeignSpider(scrapy.Spider):
    name = "hforeign"
    
    def start_requests(self):
        
        urls = ['https://homeland.house.gov/news/press-releases/table/',
                'https://homeland.house.gov/activities/hearings',
                'https://homeland.house.gov/activities/markups']
        
        categories = ["Press Release", "Hearing", "Markup"]
        
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': categories[i]})
            
            
        
    def parse(self, response):
        
        def get_past_days1():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: Jul 16 2021
            """
            today = d.today().strftime("%b %-d %Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%b %-d %Y")
            
            return [today, yesterday]
        
        def get_past_days2():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 07/13/21
            """
            today = d.today().strftime("%m/%d/%y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%y")
            
            return [today, yesterday]
        
        # Obtain category passed through meta
        category = response.meta["category"]
        
        # Obtain only past dates
        past_dates = get_past_days1()


        # MARKUPS and HEARINGS
        for entry in response.css('[class="vevent"]'):
            
            # Obtain URL
            url = entry.css('[class="faux-col"] a::attr(href)').get()
            
            # Use URL as css selector for the title
            title_selector = '[href="' + url + '"]::text'
            
            # Get date
            date = entry.css('[class="dtstart"] ::text').get()
            
            if date in past_dates:
                
                yield {
                    'category': category,
                    'date': date,
                    'title': entry.css(title_selector).get().strip("\n\t"),
                    'url': response.urljoin(url)  
                }
        
        # Obtain only past dates
        past_dates = get_past_days2()
        
        # PRESS RELEASES
        all_dates = response.css('[class="date"] ::text').getall()
        urls = response.css('[class="table"] a::attr(href)').getall()

        
        dates = []
        for date in all_dates:
            if "\t" not in date:
                dates.append(date)
                
                
        title_selectors = []
        
        for url in urls:
            
            selector = "[href='" + url + "'] ::text"
            
            title_selectors.append(selector)
        
        for i in range(len(dates)):
            
            if dates[i] in past_dates:
                
                yield {
                    'category': category,
                    'date': dates[i],
                    'title': response.css(title_selectors[i]).get().strip('\t\n'),
                    'url': urls[i]
                }
            
            
        
        
        



# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_homeland_spider.py -O output/h_homeland_" + date + ".csv"
cmdline.execute(execute.split())   
        