import scrapy
import os
from datetime import date as d
from datetime import timedelta
from scrapy import cmdline

# Program to crawl Congress "Action on Legislation" page and extract all bills information.


class AllBillsSpider(scrapy.Spider):
    name = "bills"

    def start_requests(self):
        yield scrapy.Request(url='https://www.congress.gov/bills-with-chamber-action/browse-by-date', callback=self.parse)

    def parse(self, response):
        
        def get_past_days():
            """
            Returns list of strings containing dates for today and yesterday's updates as a string formatted
            exactly as produced by the webpage. Can use obtained list so that only recent content is outputted.
                    0123456789
            Format: 07/13/2021
            """
            today = d.today().strftime("%m/%d/%Y")
            yesterday = ( d.today()-timedelta(1) ).strftime("%m/%d/%Y")
            
            return [yesterday, today]
        
        def reformat_date(date):
            return date[6:10] + "-" + date[0:2] + "-" + date[3:5]
        
        
        
        # Dates we'd like to crawl to
        past_dates = get_past_days()
        
        # All URLs on the page
        all_urls = response.css('[id^="tbody"] a::attr(href)').extract()
        
                
        # Collect all dates
        all_dates = response.css("td[rowspan='3'] ::text").getall()
        dates = []
        # Dates contain "/", so filter so dates list only contains actual dates
        for date in all_dates:
            if "/" in date:
                dates.append(date)
        
        
        # All total will contain this part
        key1 = "/search?q=%7B%22congress%22%3A%22all%22%2C%22source%22%3A%22legislation%22%2C%22search%22%3A%22actionDate%3A%5C%22117%7C"
        key2 = "%5C%22+AND+%28billIsReserved%3A%5C%22N%5C%22+OR+type%3A%5C%22AMENDMENT%5C%22%29%22%7D&pageSort=documentNumber%3Aasc"

        urls = []
        req_dates = []
        
        # Iterate through dates
        for i in range(len(dates)):
            
            # Obtain the key - the exact URL to expect to access the right page
            key = key1 + reformat_date(dates[i]) + key2
            
            # Double check key URL actually exists on the page (some dates do not have total URL)
            if key in all_urls and dates[i] in past_dates:
                urls.append(key)
                req_dates.append(dates[i])
        
        # Crawls to page for each valid URL
        for i in range(len(urls)):
            url = response.urljoin(urls[i])
            yield scrapy.Request(url, callback=self.get_bills, meta={'date': req_dates[i], 'url': url})
      
    
    
    def get_bills(self, response):
    
        """
        Extracts text for each date about bills.
        
        """
        
        # Obtains date and url information from before
        date = response.meta["date"]
        url = response.meta['url']
        
        # Iterates through each bill for that day
        for result in response.css('[class="expanded"]'):
            
            # Obtains all text assoc. with the bill
            text = result.css('[class="result-item"] *::text').getall()
            
            # Identifies the sponsor, committees, and latest action
            for part in text:
                if "[" in part:
                    sponsor = part
                if " - " in part and "/" not in part:
                    committees = part
                if " - " in part and "/" in part:
                    latest_action = part

            # CSS Selectors to find stage of tracker
            tracker_selectors = '[class="selected"]::text, [class="selected last"]::text, [class="first selected"]::text '

            # Produce the following
            yield {
                'date': date,
                'type': result.css('[class="visualIndicator"]::text').get().strip("\n "),
                'title': result.css('[class="result-title"]::text').get(),
                'sponsor': result.css('[target="_blank"]::text').get(),
                'committees': committees,
                'latest_action': latest_action,
                'tracker':  result.css(tracker_selectors).get(),
                'url': response.urljoin(result.css('[class="result-heading"] a::attr(href)').get()),  
                
            }
        
        




# Creates file with date and writes content to the file
# os.system("touch digest_$(date +%m.%d.%y).csv")
date = d.today().strftime("%m.%d.%y")
# execute = "scrapy crawl digest -O digest_" + date + ".csv"
execute = "scrapy runspider all_bills_spider.py -O output/all_bills_" + date + ".csv"

cmdline.execute(execute.split())
