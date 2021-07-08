# this code cannot access hyperlinks

from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import numpy as np
import requests

final_data = pd.DataFrame()
# scrapes list of legislations and roll call votes for session 117
url = "https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.xml"
# uses BS and xml to scrape
xml_data = requests.get(url).content

soup = BeautifulSoup(xml_data, "xml")

# Find all text in the data
texts = str(soup.findAll(text=True)).replace('\\n', '')

# Find the tag/child
child = soup.find("vote")

votenumber = []
yeas = []
nays = []
date = []
issue = []
question = []
result = []
Title = []

while True:
    try:
        votenumber.append(" ".join(child.find('vote_number')))
    except:
        votenumber.append(" . ")

    try:
        Title.append(" ".join(child.find('title')))
    except:
        Title.append(" . ")

    try:
        yeas.append(" ".join(child.find('yeas')))
    except:
        yeas.append(" . ")

    try:
        nays.append(" ".join(child.find('nays')))
    except:
        nays.append(" . ")

    try:
        question.append(" ".join(child.find('question')))
    except:
        question.append(" . ")

    try:
        issue.append(" ".join(child.find('issue')))
    except:
        issue.append(" . ")

    try:
        date.append(" ".join(child.find('vote_date')))
    except:
        date.append(" . ")

    try:
        result.append(" ".join(child.find('result')))
    except:
        result.append(" ")

    try:
        # Next sibling of child, here: entry
        child = child.find_next_sibling('vote')
    except:
        break

data = []
data = pd.DataFrame({"question": question,
                     "Title": Title,
                     "votenumber": votenumber,
                     "yeas": yeas,
                     "nays": nays,
                     "date": date,
                     "issue": issue,
                     "result": result})
final_data = final_data.append(data, ignore_index=True)
final_data.to_csv("output/rollcall.csv")


# run with python main.py
