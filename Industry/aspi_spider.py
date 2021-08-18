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
        print("len = "+str(len(urls)))
        i = -2
        for item in response.css('[role="article"]'):
            
            if i < -1:
                i += 1
                continue

            i += 1
            
            yield {
                # 'date': date,
                'Type': item.css('[class="meta-category"] div::text').get(),
                'title': item.css('[class="card-title"]>a span::text').get(),
                'url': response.urljoin(urls[i]),
                'description': item.css('[class="teaser-text"]>div::text').get()
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider aspi_spider.py -O output/aspi_" + date + ".csv"
cmdline.execute(execute.split())