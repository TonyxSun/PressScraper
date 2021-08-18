import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class ASPISpider(scrapy.Spider):
    name = "ASPI"
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.asiasociety.org/policy-institute/publications', callback=self.parse)
    
    def parse(self, response):
        
        # Otain URLs and count
        urls = response.css('[class="card-title"] a::attr(href)').extract()
        i = -1
        for item in response.css('[class="column-block"]'):
            
            # date = item.css('[class="date-display-single"] ::text').get()
            
            # Changes date if it exists
            # if date != None:
            #     date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            # if not check_date(date_obj):
            #     break
            
            yield {
                # 'date': date,
                'Type': item.css('[class="field--name-field-article-type"] ::text').get(),
                'title': item.css('[class="card-title"] span::text').get(),
                'url': response.urljoin(urls[i]),
                'description': item.css('[class="teaser-text"] ::text')
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider aspi_spider.py -O output/aspi_" + date + ".csv"
cmdline.execute(execute.split())