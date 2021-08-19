import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date



class CATOSpider(scrapy.Spider):
    name = "CATO"
    headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

    def start_requests(self):
        yield scrapy.Request(url='https://www.cato.org/blog', callback=self.parse, headers = self.headers)
    
    def parse(self, response):
        
        # Otain URLs and count
        print("opened")
        urls = response.css('[class="h2"] a::attr(href)').extract()
        print("len = "+str(len(urls))) #does not work... :(
        i = -1
        for item in response.css('article[class="blog-page"]'):
            date = item.css('[class="date-time__date date-time__date--default"] ::text').get()
            print("opened x2")

            # Changes date if it exists
            if date != None:
                date_obj = datetime.strptime(date, "%B %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            if not check_date(date_obj):
                break
            
            yield {
                'date': date,
                'Tags': item.css('[class="content-reference-link fs-xs"] *::text').get(),
                'title': item.css('h1 a span::text').get(),
                'url': response.urljoin(urls[i]),
                # 'description': item.css('[class="teaser-text"]>div::text').get()
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider cato_spider.py -O output/cato_" + date + ".csv"
cmdline.execute(execute.split())