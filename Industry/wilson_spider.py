import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class WilsonSpider(scrapy.Spider):
    name = "wilson"
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.wilsoncenter.org/insight-analysis?_page=1&keywords=&_limit=10&programs=109', callback=self.parse)
    
    
    def parse(self, response):
        
        # Otain URLs and count
        urls = response.css('[class="faceted-search-results"] a::attr(href)').extract()
        i = -1
        for item in response.css('[class="teaser"]'):
            
            
            date = item.css('[class="teaser-byline-text-date"] ::text').get()
            
            # Changes date if it exists
            if date != None:
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            if not check_date(date_obj):
                break
            
            
            yield {
                'date': date,
                'topic': item.css('[class="teaser-topic"] ::text').get(),
                'title': item.css('[class="teaser-title-text"] ::text').get(),
                'url': response.urljoin(urls[i])
    
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider wilson_spider.py -O output/wilson_" + date + ".csv"
cmdline.execute(execute.split())