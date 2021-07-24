import pandas as pd
import numpy as np
from datetime import datetime

date = datetime.today().strftime("%m.%d.%y")
html_text = '<style type="text/css"> body { color: steelblue; background-color: #FDF5E6 } </style>'

'''Industry'''
html_text += '<h2 id="industry">Industry</h2>'

#SIA
html_text += '<li><strong>SIA</strong>: Date, URL, and title of all headlines for the Semiconductor Industry Association;  <em><a href="https://www.semiconductors.org/news-events/latest-news/">https://www.semiconductors.org/news-events/latest-news/</a></em></li>'

sia = pd.read_csv(rf'Industry\output\sia_'+ '07.21.21' + '.csv')
sia_html = sia.to_html()
html_text += sia_html

#FCC
html_text += '<li><strong>FCC</strong>: Date, URL, and title of all headlines for the Federal Communications Commission;  <em><a href="https://www.fcc.gov/news-events/headlines">https://www.fcc.gov/news-events/headlines</a></em></li>'

fcc = pd.read_csv(rf'Industry\output\fcc_'+ '07.21.21' + '.csv')
fcc_html = fcc.to_html()
html_text += fcc_html


Html_file= open("index.html","w")
Html_file.write(html_text)


Html_file.close()