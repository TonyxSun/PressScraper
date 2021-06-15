# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import pandas as pd
# import numpy as np
# import requests

# url = "https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_117_1.xml".format(
#     i+1)

# xml_data = requests.get(url).content

# soup = BeautifulSoup(xml_data, "xml")

# # Find all text in the data
# texts = str(soup.findAll(text=True)).replace('\\n', '')

# # Find the tag/child
# child = soup.find("vote")

# Title = []
# yeas = []
# nays = []
# result = []

# date = []

#   while True:
#        try:
#             updated.append(" ".join(child.find('updated')))
#         except:
#             updated.append(" ")

#         try:
#             Title.append(" ".join(child.find('title')))
#         except:
#             Title.append(" ")

#         try:
#             content_type.append(" ".join(child.find('content')))
#         except:
#             content_type.append(" ")

#         try:
#             rating.append(" ".join(child.find('im:rating')))
#         except:
#             rating.append(" ")

#         try:
#             user_name.append(" ".join(child.find('name')))
#         except:
#             user_name.append(" ")

#         try:
#             # Next sibling of child, here: entry
#             child = child.find_next_sibling('entry')
#         except:
#             break
