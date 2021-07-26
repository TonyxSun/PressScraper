import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline

# scrapes the Semiconductor Industry Association's press releases


class PressSpider(scrapy.Spider):
    name = 'sia'
    start_urls = [
        'https://www.semiconductors.org/news-events/latest-news/',
    ]

    def parse(self, response):
        
        # Removes "Blog:" and "Press Release" before obtained date
        def cleanDate(date):
            
            new_date = ""
            
            for i in range(len(date)):
                if date[i] == ":":
                    break
            i += 2

            while i < len(date):
                new_date += date[i]
                i += 1
            
            return new_date

        
        for block in response.css('div.resource-item'):
            
            # Only continues if date is today or yesterday
            date = cleanDate(block.xpath('div/div/div/text()').get())
            date_obj = datetime.strptime(date, "%m/%d/%y").date()
            if check_date(date_obj):
                yield {
                    'date': date,
                    'link': block.css('div.row>div.col-sm-8>a::attr(href)').get(),
                    'title': block.css('div.row>div.col-sm-8>a>h3::text').get()

                }


# write to a csv file
# os.system("touch SIA_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider sia_spider.py -O output/sia_" + date + ".csv"
cmdline.execute(execute.split())
