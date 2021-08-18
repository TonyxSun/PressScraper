import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class CSISSpider(scrapy.Spider):
    name = "CSIS"
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.csis.org/analysis', callback=self.parse)
    
    def parse(self, response):
        
        # Otain URLs and count
        urls = response.css('[class="teaser__title"] a::attr(href)').extract()
        i = -1
        for item in response.css('[class="ds-right"]'):
            
            date = item.css('[class="date-display-single"] ::text').get()
            
            # Changes date if it exists
            if date != None:
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            if not check_date(date_obj):
                break
            
            yield {
                'date': date,
                'Type': item.css('[class="teaser__type"] ::text').get(),
                'title': item.css('[class="teaser__title"] a::text').get(),
                'url': response.urljoin(urls[i]),
                'description': item.css('[class="teaser__text"] ::text').get()
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider csis_spider.py -O output/csis_" + date + ".csv"
cmdline.execute(execute.split())