import scrapy


class QuotesSpider(scrapy.Spider):
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
