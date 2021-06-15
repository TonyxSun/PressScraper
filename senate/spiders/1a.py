import scrapy


class spider(scrapy.Spider):
    name = 'rollcall'
    start_urls = [
        'https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.htm',
    ]

    def parse(self, response):
        for block in response.css('tbody'):
            yield {
                'tally': block.css('tr>td.sorting_1>a::text').get(),
                'result': block.css('tr> td::text').get(),
                'description': block.xpath('tr/td[2]/text()').get(),
                # 'issue': block.css('span.text::text').get(),
                # 'date': block.css('span.text::text').get(),


            }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
