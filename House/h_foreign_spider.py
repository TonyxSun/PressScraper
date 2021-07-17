import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline


class HouseForeignSpider(scrapy.Spider):
    name = "hforeign"
    
    def start_requests(self):
        
        urls = ['https://foreignaffairs.house.gov/press-releases',
                'https://foreignaffairs.house.gov/hearings',
                'https://foreignaffairs.house.gov/markups']
        
        categories = ["Press Release", "Hearing", "Markup"]
        
        for i in range(len(urls)):
            yield scrapy.Request(urls[i], callback=self.parse, meta={'category': categories[i]})
            
            
        
    def parse(self, response):
        
        def get_past_days():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 7/13/21
            """
            today = d.today().strftime("%-m/%d/%y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%-m/%d/%y")
            
            return [today, yesterday]
        
        # Obtain category passed through meta
        category = response.meta["category"]
        
        dates = response.css('[class="col-xs-1 recordListDate"]::text').getall()
        times = response.css('[class="col-xs-1 recordListTime"]::text').getall()
        titles = response.css('[class="ContentGrid"]::text').getall()
        urls = response.css('[class="recordListTitle"] a::attr(href)').getall()
        
        if len(times) == 0:
            for i in range(len(dates)):
                times.append(None)
        
        for i in range(len(dates)):
            yield {
                'category': category,
                'date': dates[i],
                'time': times[i],
                'title': titles[i],
                'urls': response.urljoin(urls[i])
                
            }
        
            
        
# Creates file with date and writes content to the file
# os.system("touch sbanking_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_foreign_spider.py -O output/h_foreign_" + date + ".csv"
cmdline.execute(execute.split())   
        
        
        