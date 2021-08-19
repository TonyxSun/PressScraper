import scrapy
from datetime import datetime
from scrapy import cmdline

import sys
sys.path.insert(1, '../.')
from check_date import check_date_14



class AtlanticSpider(scrapy.Spider):
    name = "atlantic"
    def start_requests(self):
        urls = ["https://www.atlanticcouncil.org/insights-impact/research/","https://www.atlanticcouncil.org/insights-impact/commentary/"]

        categories = ["Research and Reports",
                        "Commentary and Analysis"]

        for i in range(len(urls)):
            yield scrapy.Request(url=urls[i], callback=self.parse, meta={'category': categories[i]})
    
    def parse(self, response):
        # Recover category type found previously
        category = response.meta["category"]

        # Otain URLs and count
        print("opened")
        urls = response.css('[class="gta-post-embed--title gta-embed--title"] a::attr(href)').extract()
        print("len = "+str(len(urls))) 
        i = -1
        for item in response.css('[class="gta-post-embed--container gta-embed--container thumbnail"]'):
            date = item.css('[class="gta-post-embed--heading gta-embed--heading s-tag-button"] ::text').get()
            print("opened x2")

            # Changes date if it exists
            if date != None:
                date = date.strip()
                date = date[5:]
                date_obj = datetime.strptime(date, "%b %d, %Y").date()
            
            i += 1
            
            # If date does not exist, continues scraping until date outside of range hit
            if not check_date_14(date_obj):
                break
            
            yield {
                'date': date,
                'category': category,
                'title': (item.css('[class="gta-post-embed--title gta-embed--title"] a::text').get()).strip(),
                'Tag1': (item.css('[class="s-pill large"]::text').get()),
                'Tag2': (item.css('[class="s-pill large"]:nth-child(2)::text').get()),
                'url': response.urljoin(urls[i]),
                'description': (item.css('[class="gta-post-embed--excerpt gta-embed--excerpt"]::text').get()).strip(),
            }

# Creates file with date and writes content to the file
# os.system("touch fcc_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider atlantic_spider.py -O output/atlantic_" + date + ".csv"
cmdline.execute(execute.split())