import scrapy
from scrapy import cmdline
import os
from datetime import date

# program to crawl "Daily Bills page on Senate"


class spider(scrapy.Spider):
    name = 'dailybills'
    start_urls = [
        'https://www.congress.gov/bill-texts-received-today',
    ]

    def parse(self, response):
        for block in response.css('tr'):
            yield {
                'name': block.css('td>strong::text').get(),
                'text': block.css('td::text').get(),
                'date': block.xpath('td[2]/text()').get(),
                'pdf_link': block.xpath('td[2]/a[3]/@href').get(),
                # 'date': block.css('span.text::text').get(),
            }


# write to a csv file
os.system("touch dailyBills_Senate_$(date +%m.%d.%y).csv")
date = date.today().strftime("%m.%d.%y")
execute = "scrapy crawl dailybills -O dailyBills_Senate_" + date + ".csv"
cmdline.execute(execute.split())
