# About

A simple scraper for crawling US Congress press releases and industry tycoons for analytical purposes. [ongoing]

# Contents


## Industry

*  __SIA__：Date, URL, and title of all headlines for the Semiconductor Industry Association;  _https://www.semiconductors.org/news-events/latest-news/_
* __FCC__: Date, URL, and title of all headlines for the Federal Communications Commission;  _https://www.fcc.gov/news-events/headlines_


## US Congress
* __Daily Digests__: Date, URL, and text providing details of legislation introduced, reported, passed, and considered by the full House or Senate each legislative day; _https://www.congress.gov/bills-with-chamber-action/browse-by-date_
* __Daily Bill Texts__: Date, PDF file, and text providing detailed information on legislation considered in __Daily Digests__; _https://www.congress.gov/bill-texts-received-today_


## US Senate

* __Roll Call Votes__: Date, name, and vote results of ALL Senate legislation passing through the 117th Congress; _https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.htm_
* __Floor Activity__: Date, URL, and text providing details of senate floor proceedings;  _https://floor.senate.gov/proceedings_

### US Senate Committees
* __Commerce__:  Date, URL. title, and summary of press releases from the US Senate Committee on Commerce, Science, and Transportation; _https://www.commerce.senate.gov/news_
* __Foreign__:  Type of content (nomiations, treaties, legislation, hearing transcripts, business meeting transcripts, committee reports, other), date, URL (if given), and text for activities and reports from the US Senate Committee on Foreign Relations; _https://www.foreign.senate.gov/activities-and-reports_
* __Banking__: Source of content (majority, minority), date, URL, and title for press releases from the US Senate Committee on Banking, Housing, and Urban Affairs; _https://www.banking.senate.gov/newsroom/majority-press-releases_
* __Finance__: Source of content (majority, minority), date, URL, and title for press releases from the US Senate Committee on Finance; _https://www.finance.senate.gov/chairmans-news_
* __HLSGA__: Source of content (majority, minority), date, URL, and title for press releases from the US Senate Committee on Homeland Security & Government Affairs; _https://www.hsgac.senate.gov/media/majority-media_
* __Judiciary__: Source of content (majority, minority), date, URL, and title for press releases from the US Senate Committee on the Judiciary; _https://www.judiciary.senate.gov/press/majority_


# How to run:
1. Clone repository.
2. Append all necessary executables as bash commands in `script.bash`.
3. Run `./script.bash` in the terminal.
4. Using [Crontab](https://man7.org/linux/man-pages/man5/crontab.5.html)(Mac/Linux) or [Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)(Windows), set up execution schedule to automatically run scraping job.
