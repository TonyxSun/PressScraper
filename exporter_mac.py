
import pandas as pd
import numpy as np
from datetime import datetime

'''
list of not included items:

Congress: All Bills
Senate: Roll Call Votes
Senate: Floor Activity

USE FOR MAC OS

'''

date = datetime.today().strftime("%m.%d.%y")
#date = '07.21.21'
html_text = '<link rel="stylesheet" href="style.css">'
# html_text = '<style type="text/css"> body { color: steelblue; background-color: #FDF5E6 } </style>'

html_text += '<p> Last Updated ' + date
html_text += '<img src="2021_Aug_Calendar.jpg" alt="August 2021 Calendar">'

'''Industry'''
html_text += '<h2 id="industry">Industry</h2>'

#SIA
html_text += '<p></p><strong>SIA</strong>: Date, URL, and title of all headlines for the Semiconductor Industry Association;  <em><a href="https://www.semiconductors.org/news-events/latest-news/">https://www.semiconductors.org/news-events/latest-news/</a></em>'

try:
    sia = pd.read_csv(rf'Industry/output/sia_'+ date + '.csv')
    sia_html = sia.to_html()
except:
    sia_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sia_html

#FCC
html_text += '<p></p><strong>FCC</strong>: Date, URL, and title of all headlines for the Federal Communications Commission;  <em><a href="https://www.fcc.gov/news-events/headlines">https://www.fcc.gov/news-events/headlines</a></em>'

try: 
    fcc = pd.read_csv(rf'Industry/output/fcc_'+ date + '.csv')
    fcc_html = fcc.to_html()
except:
    fcc_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += fcc_html


'''Congress'''
html_text += '<h2 id="us-congress">US Congress</h2>'

#daily dIgest
html_text += '<p></p><strong>Daily Digests</strong>: Date, URL, and text providing details of legislation introduced, reported, passed, and considered by the full House or Senate each legislative day; <br> <em><a href="https://www.congress.gov/bills-with-chamber-action/browse-by-date">https://www.congress.gov/bills-with-chamber-action/browse-by-date</a></em>'

try: 
    digest = pd.read_csv(rf'Industry/output/digest_'+ date + '.csv')
    digest_html = digest.to_html()
except:
    digest_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += digest_html

#Daily Bills 
#NOTE: TO BE REMOVED IF TOO LONG A LIST??
# html_text += '<strong>Daily Bill Texts</strong>: Date, PDF file, and text providing detailed information on legislation considered in <strong>Daily Digests</strong>;  <br><em><a href="https://www.congress.gov/bill-texts-received-today">https://www.congress.gov/bill-texts-received-today</a></em>'

# bills = pd.read_csv(rf'Congress/output/daily_bills_'+ date + '.csv')
# bills_html = bills.to_html()
# html_text += bills_html

'''Senate'''
html_text += '<h2 id="us-senate">US Senate</h2>'

#floor
# html_text += '<strong>Floor Activity</strong>: Date, URL, and text providing details of senate floor proceedings;   <em><a href="https://floor.senate.gov/proceedings">https://floor.senate.gov/proceedings</a></em>'

# floor = pd.read_csv(rf'Senate/output/floor_'+ date + '.csv')
# floor_html = floor.to_html()
# html_text += floor_html

#Senate committees
html_text += '<h3 id="us-senate-committees">US Senate Committees</h3>'

#Commerce
html_text += '<p></p><strong>Commerce</strong>:  Date, URL. title, and summary of press releases, hearings, and markups from the US Senate Committee on Commerce, Science, and Transportation;  <em><a href="https://www.commerce.senate.gov/pressreleases">https://www.commerce.senate.gov/pressreleases</a></em>, <em><a href="https://www.commerce.senate.gov/hearings">https://www.commerce.senate.gov/hearings</a></em>, <em><a href="https://www.commerce.senate.gov/markups">https://www.commerce.senate.gov/markups</a></em>'

try: 
    scomm = pd.read_csv(rf'Industry/output/scomm_'+ date + '.csv')
    scomm_html =  scomm.to_html()
except:
    scomm_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += scomm_html

#Foreign
html_text += '<p></p><strong>Foreign</strong>:  Type of content (nomiations, treaties, legislation, hearing transcripts, business meeting transcripts, committee reports, other), date, URL (if given), and text for activities and reports from the US Senate Committee on Foreign Relations;  <em><a href="https://www.foreign.senate.gov/activities-and-reports">https://www.foreign.senate.gov/activities-and-reports</a></em>'

try: 
    sforeign = pd.read_csv(rf'Industry/output/sforeign_'+ date + '.csv')
    sforeign_html = sforeign.to_html()
except:
    sforeign_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sforeign_html

#Banking
html_text += '<p></p><strong>Banking</strong>: Date, URL, and title for press releases, hearings, and markups from the US Senate Committee on Banking, Housing, and Urban Affairs;  <em><a href="https://www.banking.senate.gov/newsroom/majority-press-releases">https://www.banking.senate.gov/newsroom/majority-press-releases</a></em>, <em><a href="https://www.banking.senate.gov/hearings">https://www.banking.senate.gov/hearings</a></em>, <em><a href="https://www.banking.senate.gov/markups">https://www.banking.senate.gov/markups</a></em>'

try: 
    sbanking = pd.read_csv(rf'Industry/output/sbanking_'+ date + '.csv')
    sbanking_html = sbanking.to_html()
except:
    sbanking_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sbanking_html

#Finance
html_text += '<p></p><strong>Finance</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Finance;  <em><a href="https://www.finance.senate.gov/chairmans-news">https://www.finance.senate.gov/chairmans-news</a></em>, <em><a href="https://www.finance.senate.gov/hearings">https://www.finance.senate.gov/hearings</a></em>'

try: 
    sfinance = pd.read_csv(rf'Industry/output/sfinance_'+ date + '.csv')
    sfinance_html = sfinance.to_html()
except:
    sfinance_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sfinance_html

#HSGAc
html_text += '<p></p><strong>HLSGA</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Homeland Security &amp; Government Affairs;  <em><a href="https://www.hsgac.senate.gov/media/majority-media">https://www.hsgac.senate.gov/media/majority-media</a></em>, <em><a href="https://www.hsgac.senate.gov/hearings">https://www.hsgac.senate.gov/hearings</a></em>'

try: 
    shsgac = pd.read_csv(rf'Industry/output/shsgac_'+ date + '.csv')
    shsgac_html = shsgac.to_html()
except:
    shsgac_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += shsgac_html

#judiciary
html_text += '<p></p><strong>Judiciary</strong>: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on the Judiciary;  <em><a href="https://www.judiciary.senate.gov/press/majority">https://www.judiciary.senate.gov/press/majority</a></em>, <em><a href="https://www.judiciary.senate.gov/hearings">https://www.judiciary.senate.gov/hearings</a></em>'

try: 
    sjudiciary = pd.read_csv(rf'Industry/output/sjudiciary_'+ date + '.csv')
    sjudiciary_html = sjudiciary.to_html()
except:
    sjudiciary_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sjudiciary_html

# Intelligence
html_text += '<p></p><strong>Intelligence</strong>: Date, URL, and title, for press releases and hearings from US Senate Select Committee on Intelligence;  <em><a href="https://www.intelligence.senate.gov/press">https://www.intelligence.senate.gov/press</a></em>,  <em><a href="ttps://www.intelligence.senate.gov/hearings">https://www.intelligence.senate.gov/hearings</a></em>'

try: 
    sintelligence = pd.read_csv(rf'Industry/output/sintelligence_'+ date + '.csv')
    sintelligence_html = sintelligence.to_html()
except:
    sintelligence_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += sintelligence_html

'''House'''
html_text += '<h2 id="House">House</h2>'

# Energy
html_text += '<p></p><strong>Energy</strong>: Date, URL, title, and summary of press releases, hearings, and markups from the US House Committee on Energy;  <em><a href="https://energycommerce.house.gov/newsroom/press-releases">https://energycommerce.house.gov/newsroom/press-releases</a></em>, <em><a href="https://energycommerce.house.gov/committee-activity/hearings">https://energycommerce.house.gov/committee-activity/hearings</a></em>, <em><a href="https://energycommerce.house.gov/committee-activity/markups">https://energycommerce.house.gov/committee-activity/markups</a></em>'

try: 
    h_energy = pd.read_csv(rf'Industry/output/h_energy_'+ date + '.csv')
    h_energy_html = h_energy.to_html()
except:
    h_energy_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_energy_html

# Financial Services
html_text += '<p></p><strong>Financial Services</strong>: Date, URL, title, and summary of press releases, hearings, and markups from the US House Committee on Financial Services;  <em><a href="https://financialservices.house.gov/news/">https://financialservices.house.gov/news/</a></em>, <em><a href="https://financialservices.house.gov/calendar/?EventTypeID=577&Congress=117">https://financialservices.house.gov/calendar/?EventTypeID=577&Congress=117</a></em>, <em><a href="https://financialservices.house.gov/calendar/?EventTypeID=575&Congress=117">https://financialservices.house.gov/calendar/?EventTypeID=575&Congress=117</a></em>'

try: 
    h_financial = pd.read_csv(rf'Industry/output/h_financial_'+ date + '.csv')
    h_financial_html = h_financial.to_html()
except:
    h_financial_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_financial_html

# Foreign
html_text += '<p></p><strong>Foreign</strong>: Date, time (if applicable), title, and URL for press releases, hearings, and markups from the US House Committee on Foreign Affairs;  <em><a href="https://foreignaffairs.house.gov/press-releases">https://foreignaffairs.house.gov/press-releases</a></em>, <em><a href="https://foreignaffairs.house.gov/hearings">https://foreignaffairs.house.gov/hearings</a></em>, <em><a href="https://foreignaffairs.house.gov/markups">https://foreignaffairs.house.gov/markups</a></em>'

try: 
    h_foreign = pd.read_csv(rf'Industry/output/h_foreign_'+ date + '.csv')
    h_foreign_html = h_foreign.to_html()
except:
    h_foreign_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_foreign_html


# Homeland
html_text += '<p></p><strong>Homeland</strong>: Date, title, and url for news, hearings, and markups from the US House Committee on Homeland Security;  <em><a href="https://homeland.house.gov/activities/hearings">https://homeland.house.gov/activities/hearings</a></em>, <em><a href="https://homeland.house.gov/activities/markups">https://homeland.house.gov/activities/markups</a></em>, <em><a href="https://homeland.house.gov/news">https://homeland.house.gov/news</a></em>'

try: 
    h_homeland = pd.read_csv(rf'Industry/output/h_homeland_'+ date + '.csv')
    h_homeland_html = h_homeland.to_html()
except:
    h_homeland_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_homeland_html


# Science, Space, and Technology
html_text += '<p></p><strong>Science, Space, and Technology</strong>: Date, URL, and title of press releases, hearings, and markups from the US House Committee on Science, Space, and Tech;  <em><a href="https://science.house.gov/news/press-releases">https://science.house.gov/news/press-releases</a></em>, <em><a href="https://science.house.gov/hearings">https://science.house.gov/hearings</a></em>, <em><a href="https://science.house.gov/markups">https://science.house.gov/markups</a></em>'

try: 
    h_science = pd.read_csv(rf'Industry/output/h_science_'+ date + '.csv')
    h_science_html = h_science.to_html()
except:
    h_science_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_science_html


# Transportation
html_text += '<p></p><strong>Transportation</strong>: Date, URL, and title of press releases, hearings, and markups from the US House Committee on Transportation (Both Majority and Minority sites);  <em><a href="https://republicans-transportation.house.gov/news/documentquery.aspx?DocumentTypeID=2545">https://republicans-transportation.house.gov/news/documentquery.aspx?DocumentTypeID=2545</a></em>, <em><a href="https://republicans-transportation.house.gov/calendar/?EventTypeID=542">https://republicans-transportation.house.gov/calendar/?EventTypeID=542</a></em>, <em><a href="https://republicans-transportation.house.gov/calendar/?EventTypeID=541">https://republicans-transportation.house.gov/calendar/?EventTypeID=541</a></em>, <em><a href="https://transportation.house.gov/news/press-releases">https://transportation.house.gov/news/press-releases</a></em>, <em><a href="https://transportation.house.gov/committee-activity/hearings">https://transportation.house.gov/committee-activity/hearings</a></em>, <em><a href="https://transportation.house.gov/committee-activity/markups">https://transportation.house.gov/committee-activity/markups</a></em>'

try: 
    h_transportation = pd.read_csv(rf'Industry/output/h_transportation_'+ date + '.csv')
    h_transportation_html = h_transportation.to_html()
except:
    h_transportation_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_transportation_html

# Intelligence
html_text += '<p></p><strong>Intelligence</strong>: Date, URL, title, and summary for news from US House Permanent Select Committee on Intelligence;  <em><a href="https://intelligence.house.gov/news/documentquery.aspx?DocumentTypeID=27">https://intelligence.house.gov/news/documentquery.aspx?DocumentTypeID=27</a></em>'

try: 
    h_intelligence = pd.read_csv(rf'Industry/output/h_intelligence_'+ date + '.csv')
    h_intelligence_html = h_intelligence.to_html()
except:
    h_intelligence_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += h_intelligence_html


# Energy, Republican
html_text += '<p></p><strong>Energy, Republican</strong>: Date, URL, title, and summary of press releases, hearings, and markups from the US Republican Committee on Energy and Commerce;  <em><a href="https://republicans-energycommerce.house.gov/news/">https://republicans-energycommerce.house.gov/news/</a></em>, <em><a href="https://republicans-energycommerce.house.gov/hearings/">https://republicans-energycommerce.house.gov/hearings/</a></em>, <em><a href="https://republicans-energycommerce.house.gov/markups/">https://republicans-energycommerce.house.gov/markups/</a></em>'

try: 
    hgop_energy = pd.read_csv(rf'Industry/output/hgop_energy_'+ date + '.csv')
    hgop_energy_html = hgop_energy.to_html()
except:
    hgop_energy_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += hgop_energy_html


# Foreign, Republican
html_text += '<p></p><strong>Foreign, Republican</strong>: Date, URL, title, and summary of updates, hearings, and markups from the US Republican Committee on Foreign Affairs;  <em><a href="https://gop-foreignaffairs.house.gov/updates/">https://gop-foreignaffairs.house.gov/updates/</a></em>, <em><a href="https://gop-foreignaffairs.house.gov/hearing/">https://gop-foreignaffairs.house.gov/hearing/</a></em>, <em><a href="https://gop-foreignaffairs.house.gov/markup/">https://gop-foreignaffairs.house.gov/markup/</a></em>'

try: 
    hgop_foreign = pd.read_csv(rf'Industry/output/hgop_foreign_'+ date + '.csv')
    hgop_foreign_html = hgop_foreign.to_html()
except:
    hgop_foreign_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += hgop_foreign_html

# Homeland, Republican
html_text += '<p></p><strong>Homeland, Republican</strong>: Date, title, URL, and description for press releases from the US House Committee on Homeland Security;  <em><a href="https://republicans-homeland.house.gov/committee-activity/press-releases/">https://republicans-homeland.house.gov/committee-activity/press-releases/</a></em>'

try: 
    hgop_homeland = pd.read_csv(rf'Industry/output/hgop_homeland_'+ date + '.csv')
    hgop_homeland_htmlv = hgop_homeland.to_html()
except:
    hgop_homeland_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += hgop_homeland_html

# Science, Republican
html_text += '<p></p><strong>Science, Republican</strong>: Date, title, and url for news, hearings, and markups from the US House Committee on Science, Space, and Technology;  <em><a href="https://republicans-science.house.gov/news">https://republicans-science.house.gov/news</a></em>, <em><a href="https://republicans-science.house.gov/legislation/hearings">https://republicans-science.house.gov/legislation/hearingss</a></em>, <em><a href="https://republicans-science.house.gov/legislation/markups">https://republicans-science.house.gov/legislation/markups</a></em>'

try: 
    hgop_science = pd.read_csv(rf'Industry/output/hgop_science_'+ date + '.csv')
    hgop_science_html = hgop_science.to_html()
except:
    hgop_science_html = "<br><i>No recent output from the past week or in the future</i>" 
html_text += hgop_science_html



with open('index.html', "w", encoding="utf-8") as f:
    f.write(html_text)

f.close()