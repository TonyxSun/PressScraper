import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class BrookingsSpider(scrapy.Spider):
    name = "brookings"
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.brookings.edu/search/?s=&post_type%5B%5D=&topic%5B%5D=&pcp=&date_range=&start_date=&end_date=', callback=self.parse)
    
    
    def parse(self, response):
        
        for item in response.css('[class~="archive-view"]'):
            
            all_date = item.css('[class="meta"] *::text').extract()
            
            for date in all_date:
                if "day" in date:
                    break
            

            date_obj = datetime.strptime(date, "%A, %B %d, %Y").date()
            
            if check_date(date_obj):
                
                yield {
                    'date': date,
                    'label': item.css('[class="label"] ::text').get(),
                    'title': item.css('[class="title"] ::text').get(),
                    'url': item.css('[class="title"] a::attr(href)').get(),
                    
                    
                }


# ALSO UPDATE ...
# script.bash
# exporter_mac.py


# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider brookings_spider.py -O output/brookings_" + date + ".csv"
cmdline.execute(execute.split())