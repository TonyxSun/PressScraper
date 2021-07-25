import scrapy
from datetime import datetime
import sys
sys.path.insert(1, '../.')
from check_date import check_date
from scrapy import cmdline
import time

# Program to crawl the HOUSE Energy and Commerce news webpage, and extract information about recent headlines.


class HouseRollCallVotesSpider(scrapy.Spider):
    name = "HRollCallVotes"

    def start_requests(self):
        yield scrapy.Request(url='https://clerk.house.gov/Votes', callback=self.parse)

    def parse(self, response):
            # time.sleep(5)
            for vote in response.css('div.role-call-vote'):
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                date = vote.css('div[class="first-row]::text').get()
                date = date[1:13]
                print(date)
                print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                date_obj = datetime.strptime(date, "%b %d, %Y").date()

                if check_date(date_obj):
                    yield {
                        'date': date,
                        'Roll Call Number': vote.css('div.heading >a[href^="/Votes"]::text').get(),
                        'Roll Call url': vote.css('div.heading >a[href^="/Votes"]::attr(href)').get(),
                        'question': vote.xpath('//div[@class="row"]/div[@class="col-lg-9"]/descendant::p[@class="roll-call-descritption"][1]/text()]').get()
                    }

        


# Creates file with date and writes content to the file
# os.system("touch scommerce_$(date +%m.%d.%y).csv")
date = datetime.today().strftime("%m.%d.%y")
execute = "scrapy runspider h_roll_call_votes.py -O output/h_roll_call_votes_" + date + ".csv"
cmdline.execute(execute.split())
