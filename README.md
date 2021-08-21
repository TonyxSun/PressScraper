![GitHub last commit](https://img.shields.io/github/last-commit/tonyxsun/PressScraper) 
![Website](https://img.shields.io/website?label=website%3A&up_message=online&url=https%3A%2F%2Ftonyxsun.github.io%2FPressScraper)

### **Quick Navigation**

- [About](#about)
- [Contents](#contents)
- [How to run/update:](#how-to-run-update)

  
# About

A scraper application for crawling US Congress, industry associations, and think tanks press releases, hearings, markups, and bills for analytical purposes. 

**Time Range**: Past content within one week (for most sources) and all future content. 

**Export Format**: CSV, [US Government](https://tonyxsun.github.io/PressScraper/), [Think Tanks](https://tonyxsun.github.io/PressScraper/think_tank.html)

> *Note: For easier navigation, think tank press content are located on a seperate page from the US Government releases.*

# Contents
* [Think Tanks](#think-tanks)
* [US Congress](#us-congress)
* [US Senate](#us-senate)
    + [US Senate Committees](#us-senate-committees)
* [US House](#us-house)
    + [US House Committees](#us-house-committees)
    + [US Republican Committees](#us-republican-committees)
* [Industry](#industry)
## Think Tanks

* __Wilson__: Date, URL, and title of insight and analysis for the Wilson Center's Insights & Analysis page; <sub><br>  _https://www.wilsoncenter.org/insight-analysis?_page=1&keywords=&_limit=10&programs=109_
* __Brookings__: Date, URL, and title of insight and analysis for all content produced by the Brookings Institution page; <sub><br>  _https://www.brookings.edu/search/?s=&post_type%5B%5D=&topic%5B%5D=&pcp=&date_range=&start_date=&end_date=_
* __CSIS__: Date, type, title, URL, and description of insight and analysis for all content by the Center For Strategic & International Studies; <sub><br>  _https://www.csis.org/analysis_
* __Asia Society__: Title, URL, and description of insight and analysis for all publications by the Asia Society Policy Institute; <sub><br>  _https://www.asiasociety.org/policy-institute/publications_
* __ICAS__: Date, type, title, URL, and description of insight and analysis for all content by the Institute for China-America Studies; <sub><br>  _https://www.chinaus-icas.org/research-main/_
* __Atlantic Council__: Date, category, title, URL, description, and tags of insight and analysis for all content by the Atlantic Council; <sub><br>  _https://www.atlanticcouncil.org/insights-impact/research/_, _https://www.atlanticcouncil.org/insights-impact/commentary/_


## US Congress
* __Daily Digests__: Date, URL, and text providing details of legislation introduced, reported, passed, and considered by the full House or Senate each legislative day;<sub> <br> _https://www.congress.gov/bills-with-chamber-action/browse-by-date_
* __Daily Bill Texts__: Date, PDF file, and text providing detailed information on legislation considered in __Daily Digests__;<sub>  <br>_https://www.congress.gov/bill-texts-received-today_
* __All Bills__: Date, URL, and other details (eg. title, sponsor, committees, latest action) for all bills under total of "All Bills, Resolutions, and Amendments";<sub>   <br>_https://www.congress.gov/bills-with-chamber-action/browse-by-date_


## US Senate

* __Roll Call Votes__: Date, name, and vote results of ALL Senate legislation passing through the 117th Congress;<sub>  <br> _https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.htm_
* __Floor Activity__: Date, URL, and text providing details of senate floor proceedings;<sub>    <br>_https://floor.senate.gov/proceedings_

### US Senate Committees
* __Commerce__:  Date, URL. title, and summary of press releases, hearings, and markups from the US Senate Committee on Commerce, Science, and Transportation;<sub>  <br> _https://www.commerce.senate.gov/pressreleases_, _https://www.commerce.senate.gov/hearings_, _https://www.commerce.senate.gov/markups_
* __Foreign__:  Type of content (nomiations, treaties, legislation, hearing transcripts, business meeting transcripts, committee reports, other), date, URL (if given), and text for activities and reports from the US Senate Committee on Foreign Relations;<sub>  <br> _https://www.foreign.senate.gov/activities-and-reports_
* __Banking__: Date, URL, and title for press releases, hearings, and markups from the US Senate Committee on Banking, Housing, and Urban Affairs;<sub>  <br> _https://www.banking.senate.gov/newsroom/majority-press-releases_, _https://www.banking.senate.gov/hearings_, _https://www.banking.senate.gov/markups_
* __Finance__: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Finance;<sub>  <br> _https://www.finance.senate.gov/chairmans-news_, _https://www.finance.senate.gov/hearings_
* __HLSGA__: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on Homeland Security & Government Affairs;<sub>  <br> _https://www.hsgac.senate.gov/media/majority-media_, _https://www.hsgac.senate.gov/hearings_
* __Judiciary__: Source of content (majority, minority), date, URL, and title for press releases and hearings from the US Senate Committee on the Judiciary;<sub> <br>  _https://www.judiciary.senate.gov/press/majority_, _https://www.judiciary.senate.gov/hearings_
* __Intelligence__: Date, URL, title, and summary for news from US Senate Select Committee on Intelligence; <sub> <br> _https://www.intelligence.senate.gov/press_, _https://www.intelligence.senate.gov/hearings_

## US House

### US House Committees
* __Energy__: Date, URL, title, and summary of press releases, hearings, and markups from the US House Committee on Energy;<sub>  <br>_https://energycommerce.house.gov/newsroom/press-releases_, _https://energycommerce.house.gov/committee-activity/hearings_, _https://energycommerce.house.gov/committee-activity/markups_ 
* __Financial Services__: Date, URL, title, and summary of press releases, hearings, and markups from the US House Committee on Financial Services; <sub> <br> _https://financialservices.house.gov/news/_, _https://financialservices.house.gov/calendar/?EventTypeID=577&Congress=117_, _https://financialservices.house.gov/calendar/?EventTypeID=575&Congress=117_
* __Foreign__:  Date, time (if applicable), title, and URL for press releases, hearings, and markups from the US House Committee on Foreign Affairs; <sub> <br> _https://foreignaffairs.house.gov/press-releases_, _https://foreignaffairs.house.gov/hearings_, _https://foreignaffairs.house.gov/markups_
* __Homeland__: Date, title, and url for news, hearings, and markups from the US House Committee on Homeland Security; <sub> <br> _https://homeland.house.gov/activities/hearings_. _https://homeland.house.gov/activities/markups_, _https://homeland.house.gov/news_
* __Science, Space, and Tech__: Date, URL, and title of press releases, hearings, and markups from the US House Committee on Science, Space, and Tech; <sub> <br> _https://science.house.gov/news/press-releases_, _https://science.house.gov/hearings_, _https://science.house.gov/markups_
* __Transportation__: Date, URL, and title of press releases, hearings, and markups from the US House Committee on Transportation (Both Majority and Minority sites);<sub> <br>_https://republicans-transportation.house.gov/news/documentquery.aspx?DocumentTypeID=2545_, _https://republicans-transportation.house.gov/calendar/?EventTypeID=542_, _https://republicans-transportation.house.gov/calendar/?EventTypeID=541_, _https://transportation.house.gov/news/press-releases_, _https://transportation.house.gov/committee-activity/hearings_, _https://transportation.house.gov/committee-activity/markups_
* __Intelligence__: Date, URL, title, and summary for news from US Permanent Select Committee on Intelligence; <sub> <br> _https://intelligence.house.gov/_
  
### US Republican Committees
* __Energy__: Date, URL, title, and summary of press releases, hearings, and markups from the US Republican Committee on Energy and Commerce;<sub>  <br>_https://republicans-energycommerce.house.gov/news/_, _https://republicans-energycommerce.house.gov/hearings/_, _https://republicans-energycommerce.house.gov/markups/_ 
* __Foreign__: Date, URL, title, and summary of updates, hearings, and markups from the US Republican Committee on Foreign Affairs; <sub> <br> _https://gop-foreignaffairs.house.gov/updates/_, _https://gop-foreignaffairs.house.gov/hearing/_, _https://gop-foreignaffairs.house.gov/markup/_
* __Homeland__:  Date, title, URL, and description for press releases from the US House Committee on Homeland Security; <sub> <br> _https://republicans-homeland.house.gov/committee-activity/press-releases/_
* __Science__: Date, title, and url for news, hearings, and markups from the US House Committee on Science, Space, and Technology; <sub> <br> _https://republicans-science.house.gov/news_. _https://republicans-science.house.gov/legislation/hearings_, _https://republicans-science.house.gov/legislation/markups_

## Industry

*  __SIA__：Date, URL, and title of all headlines for the Semiconductor Industry Association; <sub><br> _https://www.semiconductors.org/news-events/latest-news/_
* __FCC__: Date, URL, and title of all headlines for the Federal Communications Commission; <sub><br>  _https://www.fcc.gov/news-events/headlines_


# How to run/update
1. Clone repository.
2. Run `./script.bash` in the terminal.
3. Using [Crontab](https://man7.org/linux/man-pages/man5/crontab.5.html)(Mac/Linux) or [Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)(Windows), set up execution schedule to automatically run scraping job.
