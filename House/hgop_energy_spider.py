import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline


# Program to crawl the Republican Energy and Commerce Committee webpage, and extract information about recent headlines.

class HouseGOPEnergySpider(scrapy.Spider):
    name = "h-gop-energy"
    
    def start_requests(self):
        urls = ["https://republicans-energycommerce.house.gov/news/press-release/",
                "https://republicans-energycommerce.house.gov/hearings/",
                "https://republicans-energycommerce.house.gov/markups/"
                ]

        categories = ["Press Releases", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})

    def parse(self, response):
        
        def get_date(date):
            
            """
            Extracted date includes time, want to remove

            """
            
            new_date = ""
            spaces = 0
            
            for char in date:
                if char == " ":
                    spaces += 1
                if spaces == 3:
                    return new_date
                new_date += char
        
        # Recover category type found previously
        category = response.meta["category"]
        
        for item in response.css('[class^="col-sm-"]'):
            
            # Get date
            date = item.css('[class="meta h4"] ::text').get()
            
            # Adjust format of date for hearings, markups
            # Change to date object
            if category in ["Hearings", "Markups"]:
                date = get_date(date)
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
            else:
                date_obj = datetime.strptime(date, "%m.%d.%Y").date()
            
            # Extract for valid dates
            if check_date(date_obj):
            
                yield {
                    'category': category,
                    'date': date,
                    'title': item.css('[class="headline"] ::text').get(),
                    'url': item.css('[class^="col-sm-"] a::attr(href)').get(),
                    'description': item.css('[class="description"] ::text').get()
                }
            
        



# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider hgop_energy_spider.py -O output/h_gop_energy_" + date + ".csv"
cmdline.execute(execute.split())