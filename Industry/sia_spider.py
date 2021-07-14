import scrapy
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

# scrapes the Semiconductor Industry Association's press releases


class PressSpider(scrapy.Spider):
    name = 'sia'
    start_urls = [
        'https://www.semiconductors.org/news-events/latest-news/',
    ]

    def parse(self, response):
        
        def getPastDays():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
            
            Format: 07/13/21
            """
            today = d.today().strftime("%m/%d/%y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%y")
            
            return [today, yesterday]

        
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
            
        # Obtains today and yesterday as a string
        past_dates = getPastDays()
        
        for block in response.css('div.resource-item'):
            
            # Only continues if date is today or yesterday
            date = cleanDate(block.xpath('div/div/div/text()').get())
        
            if date in past_dates:
                yield {
                    'date': date,
                    'link': block.css('div.row>div.col-sm-8>a::attr(href)').get(),
                    'title': block.css('div.row>div.col-sm-8>a>h3::text').get()

                }


# write to a csv file
# os.system("touch SIA_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
execute = "scrapy runspider sia_spider.py -O output/SIA_" + date + ".csv"
cmdline.execute(execute.split())
