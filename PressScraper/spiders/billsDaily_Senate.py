import scrapy
from scrapy import cmdline


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

# execute = "scrapy crawl dailybills -O dailyBills_Senate.csv"
# cmdline.execute(execute.split())
