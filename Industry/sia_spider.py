import scrapy
import os
from datetime import date
from scrapy import cmdline

# scrapes the Semiconductor Industry Association's press releases


class PressSpider(scrapy.Spider):
    name = 'sia'
    start_urls = [
        'https://www.semiconductors.org/news-events/latest-news/',
    ]

    def parse(self, response):
        for block in response.css('div.resource-item'):
            yield {
                'date': block.xpath('div/div/div/text()').get(),
                'link': block.css('div.row>div.col-sm-8>a::attr(href)').get(),
                'title': block.css('div.row>div.col-sm-8>a>h3::text').get()

            }


# write to a csv file
# os.system("touch SIA_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
execute = "scrapy runspider sia_spider.py -O output/SIA_" + date + ".csv"
cmdline.execute(execute.split())
