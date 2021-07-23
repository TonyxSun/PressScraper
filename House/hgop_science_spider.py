import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date

# Program to crawl the Republican's House committee on homeland

class HouseGOPScienceSpider(scrapy.Spider):
    name = "h-gop-science"
    
    def start_requests(self):
        urls = ["https://republicans-science.house.gov/news",
                "https://republicans-science.house.gov/legislation/hearings",
                "https://republicans-science.house.gov/legislation/markups"
                ]

        categories = ["News", "Hearings", "Markups"]

        for i in range(len(urls)):

            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})


    def parse(self, response):
        
        def get_date(date):
            new_date = ""
            
            extract = False
            count = 0
            
            for char in date:
                if char == " ":
                    extract = True
                    continue
                if count == 10:
                    return new_date
                if extract:
                    new_date += char
                    count += 1
            
        
        # Recover category type found previously
        category = response.meta["category"]
        
        for item in response.css('[class^="views-row"]'):

            # Get all text
            all_content = item.css('[class="field-content"] *::text').getall()
            
            # For news, get date as an object
            if category == "News":
                date = all_content[1]
                date_obj = datetime.strptime(date, "%b %d, %Y").date()
            
            # For hearings and markups, get date as an object
            elif category in ["Hearings", "Markups"]:
                date = get_date(all_content[1])
                date_obj = datetime.strptime(date, "%m/%d/%Y").date()
            
            # Continue and extract if date is valid
            if check_date(date_obj):
                
                yield {
                    'category': category,
                    'date': date,
                    'title': all_content[0],
                    'url': response.urljoin(item.css('[class="field-content"] a::attr(href)').get()),
                }
                        
        



# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider hgop_science_spider.py -O output/h_gop_science_" + date + ".csv"
cmdline.execute(execute.split())