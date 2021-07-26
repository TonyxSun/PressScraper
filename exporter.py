import pandas as pd
import numpy as np
from datetime import datetime

'''
list of not included items:

Congress: All Bills
Senate: Roll Call Votes
Senate: Floor ACtivity 

'''
date = datetime.today().strftime("%m.%d.%y")
date = '07.21.21'
html_text = '<link rel="stylesheet" href="style.css">'
# html_text = '<style type="text/css"> body { color: steelblue; background-color: #FDF5E6 } </style>'

'''Industry'''
html_text += '<h2 id="industry">Industry</h2>'

#SIA
html_text += '<strong>SIA</strong>: Date, URL, and title of all headlines for the Semiconductor Industry Association;  <em><a href="https://www.semiconductors.org/news-events/latest-news/">https://www.semiconductors.org/news-events/latest-news/</a></em>'

sia = pd.read_csv(rf'Industry\output\sia_'+ date + '.csv')
sia_html = sia.to_html()
html_text += sia_html

#FCC
html_text += '<strong>FCC</strong>: Date, URL, and title of all headlines for the Federal Communications Commission;  <em><a href="https://www.fcc.gov/news-events/headlines">https://www.fcc.gov/news-events/headlines</a></em>'

fcc = pd.read_csv(rf'Industry\output\fcc_'+ date + '.csv')
fcc_html = fcc.to_html()
html_text += fcc_html


'''Congress'''
html_text += '<h2 id="us-congress">US Congress</h2>'

#daily dIgest
html_text += '<strong>Daily Digests</strong>: Date, URL, and text providing details of legislation introduced, reported, passed, and considered by the full House or Senate each legislative day;<sub> <br> <em><a href="https://www.congress.gov/bills-with-chamber-action/browse-by-date">https://www.congress.gov/bills-with-chamber-action/browse-by-date</a></em></sub>'

digest = pd.read_csv(rf'Congress\output\digest_'+ date + '.csv')
digest_html = digest.to_html()
html_text += digest_html

#Daily Bills 
#NOTE: TO BE REMOVED IF TOO LONG A LIST??
html_text += '<strong>Daily Bill Texts</strong>: Date, PDF file, and text providing detailed information on legislation considered in <strong>Daily Digests</strong>;<sub>  <br><em><a href="https://www.congress.gov/bill-texts-received-today">https://www.congress.gov/bill-texts-received-today</a></em></sub>'

bills = pd.read_csv(rf'Congress\output\daily_bills_'+ date + '.csv')
bills_html = bills.to_html()
html_text += bills_html

'''Senate'''
html_text += '<h2 id="us-senate">US Senate</h2>'

#floor
# html_text += '<strong>Floor Activity</strong>: Date, URL, and text providing details of senate floor proceedings;<sub>   <em><a href="https://floor.senate.gov/proceedings">https://floor.senate.gov/proceedings</a></em>'

# floor = pd.read_csv(rf'Senate\output\floor_'+ date + '.csv')
# floor_html = floor.to_html()
# html_text += floor_html

#Senate committees
html_text += '<h3 id="us-senate-committees">US Senate Committees</h3>'

#Commerce
html_text += '<strong>Commerce</strong>:  Date, URL. title, and summary of press releases, hearings, and markups from the US Senate Committee on Commerce, Science, and Transportation;<sub>  <em><a href="https://www.commerce.senate.gov/pressreleases">https://www.commerce.senate.gov/pressreleases</a></em>, <em><a href="https://www.commerce.senate.gov/hearings">https://www.commerce.senate.gov/hearings</a></em>, <em><a href="https://www.commerce.senate.gov/markups">https://www.commerce.senate.gov/markups</a></em></sub>'

scomm = pd.read_csv(rf'Senate\output\scommerce_'+ date + '.csv')
scomm_html = scomm.to_html()
html_text += scomm_html

#Foreign
html_text += '<strong>Foreign</strong>:  Type of content (nomiations, treaties, legislation, hearing transcripts, business meeting transcripts, committee reports, other), date, URL (if given), and text for activities and reports from the US Senate Committee on Foreign Relations;<sub>  <em><a href="https://www.foreign.senate.gov/activities-and-reports">https://www.foreign.senate.gov/activities-and-reports</a></em></sub>'

sforeign_ = pd.read_csv(rf'Senate\output\sforeign_'+ date + '.csv')
sforeign_html = sforeign_.to_html()
html_text += sforeign_html

#Banking
html_text += '<strong>Banking</strong>: Date, URL, and title for press releases, hearings, and markups from the US Senate Committee on Banking, Housing, and Urban Affairs;<sub>  <em><a href="https://www.banking.senate.gov/newsroom/majority-press-releases">https://www.banking.senate.gov/newsroom/majority-press-releases</a></em>, <em><a href="https://www.banking.senate.gov/hearings">https://www.banking.senate.gov/hearings</a></em>, <em><a href="https://www.banking.senate.gov/markups">https://www.banking.senate.gov/markups</a></em></sub>'

sbanking_ = pd.read_csv(rf'Senate\output\sbanking_'+ date + '.csv')
sbanking_html = sbanking_.to_html()
html_text += sbanking_html

#Finance
html_text += '<strong>Finance</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Finance;<sub>  <em><a href="https://www.finance.senate.gov/chairmans-news">https://www.finance.senate.gov/chairmans-news</a></em>, <em><a href="https://www.finance.senate.gov/hearings">https://www.finance.senate.gov/hearings</a></em></sub>'

sfinance = pd.read_csv(rf'Senate\output\sfinance'+ date + '.csv')
sfinance_html = sfinance.to_html()
html_text += sfinance_html

#HSGAc
html_text += '<strong>HLSGA</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Homeland Security &amp; Government Affairs;<sub>  <em><a href="https://www.hsgac.senate.gov/media/majority-media">https://www.hsgac.senate.gov/media/majority-media</a></em>, <em><a href="https://www.hsgac.senate.gov/hearings">https://www.hsgac.senate.gov/hearings</a></em></sub>'

shsgac = pd.read_csv(rf'Senate\output\shsgac'+ date + '.csv')
shsgac_html = shsgac.to_html()
html_text += shsgac_html

#judiciary
html_text += '<strong>Judiciary</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on the Judiciary;<sub>  <em><a href="https://www.judiciary.senate.gov/press/majority">https://www.judiciary.senate.gov/press/majority</a></em>, <em><a href="https://www.judiciary.senate.gov/hearings">https://www.judiciary.senate.gov/hearings</a></em></sub>'

sjudiciary = pd.read_csv(rf'Senate\output\sjudiciary'+ date + '.csv')
sjudiciary_html = sjudiciary.to_html()
html_text += sjudiciary_html

with open('.\docs\index.html', "w", encoding="utf-8") as f:
    f.write(html_text)

f.close()