import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date_30



class ICASSpider(scrapy.Spider):
    name = "ICAS"
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.chinaus-icas.org/research-main/', callback=self.parse)
    
    def parse(self, response):
        
        # Otain URLs and count
        # urls = response.css('h3[class="elementor-heading-title elementor-size-default"] a::attr(href)').extract()
        urls = response.css('article div[class="elementor-button-wrapper"] a::attr(href)').extract()

        i = -1
        used_urls = []
        for item in response.css('article'):
            
            date = item.css('span[class="elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-custom"]::text').get()
            
            # # Changes date if it exists
            if date != None:
                date = date.strip()
                print(date)
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            if not check_date_30(date_obj):
                continue
            
            if urls[i] in used_urls:
                continue
            used_urls.append(urls[i])

            type = item.css('[class="elementor-button-text"] ::text').get()
            type = type[5:]
            yield {
                'date': date,
                'Type': type,
                'title': item.css('h3[class="elementor-heading-title elementor-size-default"] a::text').get(),
                'url': response.urljoin(urls[i]),
                'description': item.css('h2[class="elementor-heading-title elementor-size-default"] a::text').get()
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider icas_spider.py -O output/icas_" + date + ".csv"
cmdline.execute(execute.split())